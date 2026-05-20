#!/usr/bin/env python3
"""
audit_geo.py - Auditoria automatica de infraestrutura GEO/AEO de um site.

Cobre a Camada 1 (infraestrutura) e sinais basicos das Camadas 2, 3 e 6:
  - Latencia / TTFB
  - SSR (conteudo no HTML inicial sem JS)
  - HTTPS valido e redirect de http
  - llms.txt e llms-full.txt
  - robots.txt: bots de IA bloqueados ou liberados, referencia a sitemap
  - sitemap.xml acessivel
  - canonical tag
  - JSON-LD / Schema markup e tipos presentes
  - Sinais answer-first (H1, primeiro paragrafo)
  - Tabelas HTML reais vs imagens
  - alt-text em imagens

Uso:
    python audit_geo.py https://site.com

Dependencias: apenas a biblioteca padrao do Python 3.
"""

import sys
import json
import re
import urllib.request
import urllib.error
import time
from urllib.parse import urljoin, urlparse

USER_AGENT = "Mozilla/5.0 (compatible; GEO-Audit/1.0)"
TIMEOUT = 15

AI_SEARCH_BOTS = ["OAI-SearchBot", "PerplexityBot", "Perplexity-User", "ClaudeBot"]
AI_TRAINING_BOTS = ["GPTBot", "CCBot", "Google-Extended"]
VALUABLE_SCHEMA = {"FAQPage", "QAPage", "Person", "Organization", "Article",
                   "Product", "HowTo", "LocalBusiness", "Review", "BreadcrumbList"}


def fetch(url, method="GET"):
    """Busca uma URL e retorna (status, headers, body, elapsed_seconds)."""
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, dict(resp.headers), body, time.time() - start
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), "", time.time() - start
    except Exception as e:
        return None, {}, str(e), time.time() - start


def check_https(url):
    parsed = urlparse(url)
    if parsed.scheme != "https":
        return {"check": "HTTPS", "valor": parsed.scheme, "ok": False,
                "nota": "Site nao usa HTTPS. IAs despriorizam sites sem TLS valido."}
    status, _, _, _ = fetch(url)
    ok = status is not None and status < 400
    http_url = "http://" + parsed.netloc
    h_status, h_headers, _, _ = fetch(http_url)
    redirects = h_status in (301, 302, 308) and "https" in h_headers.get("Location", "")
    if not ok:
        nota = "HTTPS retornou erro - verificar certificado e disponibilidade."
    elif redirects:
        nota = "HTTPS OK. Redirect http->https OK."
    else:
        nota = "HTTPS OK. Confirme manualmente o redirect 301 de http para https."
    return {"check": "HTTPS", "valor": "https", "ok": ok, "nota": nota}


def check_latency(url):
    status, _, _, elapsed = fetch(url)
    ms = round(elapsed * 1000)
    ok = ms < 200
    note = "OK" if ok else "ACIMA DE 200ms - reduzir TTFB (CDN, cache, edge)"
    if status is None:
        note = "FALHA ao acessar o site"
    return {"check": "Latencia / TTFB", "valor": f"{ms}ms", "ok": ok, "nota": note}


def check_ssr(body):
    text = re.sub(r"<script.*?</script>", "", body, flags=re.S | re.I)
    text = re.sub(r"<style.*?</style>", "", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    words = len(text.split())
    ok = words > 250
    nota = ("OK - conteudo presente no HTML inicial" if ok
            else "POUCO TEXTO no HTML inicial - possivel SPA sem SSR. "
                 "Crawlers de IA podem ver pagina vazia.")
    return {"check": "SSR / conteudo no HTML inicial",
            "valor": f"~{words} palavras", "ok": ok, "nota": nota}


def check_file(base, path):
    url = urljoin(base, path)
    status, _, body, _ = fetch(url)
    ok = status == 200 and len(body.strip()) > 0
    nota = "Encontrado" if ok else f"Ausente (status {status})"
    return {"check": path, "valor": url, "ok": ok, "nota": nota}


def check_robots(base):
    url = urljoin(base, "/robots.txt")
    status, _, body, _ = fetch(url)
    if status != 200:
        return [{"check": "robots.txt", "valor": url, "ok": False,
                 "nota": f"Nao encontrado (status {status})"}]
    results = []
    current_agents = []
    blocked = {}
    has_sitemap = False
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = [p.strip() for p in line.split(":", 1)]
        key_l = key.lower()
        if key_l == "user-agent":
            current_agents = [val]
        elif key_l == "disallow" and val == "/":
            for a in current_agents:
                blocked[a] = True
        elif key_l == "sitemap":
            has_sitemap = True

    for bot in AI_SEARCH_BOTS:
        is_blocked = blocked.get(bot, False) or blocked.get("*", False)
        results.append({
            "check": f"robots.txt - bot de busca '{bot}'",
            "valor": "BLOQUEADO" if is_blocked else "liberado",
            "ok": not is_blocked,
            "nota": ("CRITICO: bot de busca de IA bloqueado = some das respostas"
                     if is_blocked else "OK - liberado para recuperacao")
        })
    for bot in AI_TRAINING_BOTS:
        is_blocked = blocked.get(bot, False)
        results.append({
            "check": f"robots.txt - bot de treinamento '{bot}'",
            "valor": "bloqueado" if is_blocked else "liberado",
            "ok": True,
            "nota": "Decisao do negocio - nao afeta visibilidade nas respostas"
        })
    results.append({
        "check": "robots.txt - referencia a Sitemap",
        "valor": "presente" if has_sitemap else "ausente",
        "ok": has_sitemap,
        "nota": "OK" if has_sitemap else "Adicionar linha 'Sitemap:' no robots.txt"
    })
    return results


def check_schema(body):
    blocks = re.findall(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        body, flags=re.S | re.I)
    types = []
    has_graph = False
    for b in blocks:
        try:
            data = json.loads(b.strip())
            if isinstance(data, dict) and "@graph" in data:
                has_graph = True
                items = data["@graph"]
            else:
                items = data if isinstance(data, list) else [data]
            for it in items:
                t = it.get("@type")
                if t:
                    types.append(t if isinstance(t, str) else ",".join(t))
        except Exception:
            types.append("(JSON-LD invalido)")
    ok = len(blocks) > 0
    has_valuable = any(t in VALUABLE_SCHEMA for t in types)
    found = ", ".join(types) if types else "nenhum"
    nota = f"Tipos: {found}. " + ("Inclui schema relevante para GEO." if has_valuable
                                   else "Considere FAQPage, Person, Organization.")
    if has_graph:
        nota += " Usa @graph (bom)."
    if not ok:
        nota = "Nenhum JSON-LD encontrado. Adicionar schema markup (Camada 2)."
    return {"check": "Schema markup (JSON-LD)",
            "valor": f"{len(blocks)} bloco(s)", "ok": ok, "nota": nota}


def check_canonical(body):
    m = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*>', body, flags=re.I)
    ok = m is not None
    return {"check": "Canonical tag", "valor": "presente" if ok else "ausente",
            "ok": ok, "nota": "OK" if ok
            else "Sem <link rel=canonical>. Adicionar para consolidar autoridade."}


def check_answer_first(body):
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, flags=re.S | re.I)
    h1_text = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else None
    p = re.search(r"<p[^>]*>(.*?)</p>", body, flags=re.S | re.I)
    p_text = re.sub(r"<[^>]+>", "", p.group(1)).strip() if p else ""
    p_words = len(p_text.split())
    ok = h1_text is not None and 15 <= p_words <= 120
    nota = []
    if not h1_text:
        nota.append("Sem H1.")
    if p_words == 0:
        nota.append("Sem primeiro paragrafo de texto.")
    elif p_words < 15:
        nota.append("Primeiro paragrafo curto demais para conter a resposta.")
    nota.append("Verifique manualmente se a resposta direta esta nas "
                "primeiras 40-60 palavras (answer-first).")
    return {"check": "Sinais answer-first",
            "valor": f"H1: {'sim' if h1_text else 'nao'} | 1o paragrafo: ~{p_words} palavras",
            "ok": ok, "nota": " ".join(nota)}


def check_tables(body):
    tables = len(re.findall(r"<table", body, flags=re.I))
    return {"check": "Tabelas HTML",
            "valor": f"{tables} tabela(s)", "ok": True,
            "nota": ("Tabelas HTML reais detectadas (extraiveis pela IA)." if tables
                     else "Nenhuma <table>. Se ha dados comparativos, use tabela HTML, "
                          "nao imagem.")}


def check_alt_text(body):
    imgs = re.findall(r"<img[^>]*>", body, flags=re.I)
    if not imgs:
        return {"check": "Alt-text em imagens", "valor": "0 imagens",
                "ok": True, "nota": "Nenhuma imagem na pagina."}
    with_alt = sum(1 for i in imgs
                   if re.search(r'alt=["\'][^"\']+["\']', i, flags=re.I))
    pct = round(100 * with_alt / len(imgs))
    ok = pct >= 90
    return {"check": "Alt-text em imagens",
            "valor": f"{with_alt}/{len(imgs)} ({pct}%)", "ok": ok,
            "nota": "OK" if ok else "Adicionar alt-text descritivo as imagens sem alt."}


def main():
    if len(sys.argv) < 2:
        print("Uso: python audit_geo.py https://site.com")
        sys.exit(1)
    url = sys.argv[1]
    if not urlparse(url).scheme:
        url = "https://" + url
    base = f"{urlparse(url).scheme}://{urlparse(url).netloc}"

    print(f"\n=== Auditoria GEO/AEO: {url} ===\n")

    status, _, body, _ = fetch(url)
    if status is None:
        print(f"ERRO: nao foi possivel acessar {url}\nDetalhe: {body}")
        sys.exit(1)

    results = []
    results.append(check_https(url))
    results.append(check_latency(url))
    results.append(check_ssr(body))
    results.append(check_file(base, "/llms.txt"))
    results.append(check_file(base, "/llms-full.txt"))
    results.append(check_file(base, "/sitemap.xml"))
    results.extend(check_robots(base))
    results.append(check_canonical(body))
    results.append(check_schema(body))
    results.append(check_answer_first(body))
    results.append(check_tables(body))
    results.append(check_alt_text(body))

    for r in results:
        mark = "[ OK ]" if r["ok"] else "[FALHA]"
        print(f"{mark} {r['check']}")
        print(f"        valor: {r['valor']}")
        print(f"        nota:  {r['nota']}\n")

    falhas = [r for r in results if not r["ok"]]
    print("=" * 55)
    print(f"Resumo: {len(results) - len(falhas)}/{len(results)} checagens OK.")
    if falhas:
        print("\nPrioridades (resolver primeiro):")
        for r in falhas:
            print(f"  - {r['check']}: {r['nota']}")
    print("\nNota: este script cobre a Camada 1 e sinais basicos das Camadas")
    print("2, 3 e 6. As Camadas 4 e 5 (estrategia de conteudo, autoridade")
    print("externa) e o monitoramento continuo exigem analise manual seguindo")
    print("as referencias tematicas da skill (uma por camada).\n")


if __name__ == "__main__":
    main()
