#!/usr/bin/env python3
"""
audit_geo.py - Automated GEO/AEO infrastructure audit for a website.

Focuses on Layer 1 (infrastructure) and basic signals from Layers 2, 3, and 6:
  - Latency / TTFB
  - SSR (content present in initial HTML without JS)
  - Valid HTTPS and http->https redirect
  - llms.txt and llms-full.txt
  - robots.txt: AI bots allowed/blocked, sitemap reference
  - sitemap.xml accessible
  - canonical tag
  - JSON-LD / Schema markup and detected types
  - Answer-first signals (H1, first paragraph)
  - Real HTML tables vs images
  - Image alt-text

Usage:
    python audit_geo.py https://site.com

Dependencies: Python 3 standard library only.
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
    """Fetches a URL and returns (status, headers, body, elapsed_seconds)."""
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
        return {"check": "HTTPS", "value": parsed.scheme, "ok": False,
                "note": "Site is not using HTTPS. Generative engines deprioritize sites without valid TLS."}
    status, _, _, _ = fetch(url)
    ok = status is not None and status < 400
    http_url = "http://" + parsed.netloc
    h_status, h_headers, _, _ = fetch(http_url)
    redirects = h_status in (301, 302, 308) and "https" in h_headers.get("Location", "")
    if not ok:
        note = "HTTPS returned an error — check certificate and availability."
    elif redirects:
        note = "HTTPS OK. http->https redirect OK."
    else:
        note = "HTTPS OK. Manually confirm a 301 redirect from http to https."
    return {"check": "HTTPS", "value": "https", "ok": ok, "note": note}


def check_latency(url):
    status, _, _, elapsed = fetch(url)
    ms = round(elapsed * 1000)
    ok = ms < 200
    note = "OK" if ok else "ABOVE 200ms — reduce TTFB (CDN, cache, edge)"
    if status is None:
        note = "FAILED to access the site"
    return {"check": "Latency / TTFB", "value": f"{ms}ms", "ok": ok, "note": note}


def check_ssr(body):
    text = re.sub(r"<script.*?</script>", "", body, flags=re.S | re.I)
    text = re.sub(r"<style.*?</style>", "", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    words = len(text.split())
    ok = words > 250
    note = ("OK — content present in initial HTML" if ok
            else "LOW TEXT in initial HTML — possible SPA without SSR. "
                 "AI crawlers may see an empty page.")
    return {"check": "SSR / content in initial HTML",
            "value": f"~{words} words", "ok": ok, "note": note}


def check_file(base, path):
    url = urljoin(base, path)
    status, _, body, _ = fetch(url)
    ok = status == 200 and len(body.strip()) > 0
    note = "Found" if ok else f"Missing (status {status})"
    return {"check": path, "value": url, "ok": ok, "note": note}


def check_robots(base):
    url = urljoin(base, "/robots.txt")
    status, _, body, _ = fetch(url)
    if status != 200:
        return [{"check": "robots.txt", "value": url, "ok": False,
                 "note": f"Not found (status {status})"}]
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
            "check": f"robots.txt - search bot '{bot}'",
            "value": "BLOCKED" if is_blocked else "allowed",
            "ok": not is_blocked,
            "note": ("CRITICAL: blocking AI search bots can remove you from answers"
                     if is_blocked else "OK — allowed for retrieval")
        })
    for bot in AI_TRAINING_BOTS:
        is_blocked = blocked.get(bot, False)
        results.append({
            "check": f"robots.txt - training bot '{bot}'",
            "value": "blocked" if is_blocked else "allowed",
            "ok": True,
            "note": "Business decision — does not affect answer visibility (retrieval)"
        })
    results.append({
        "check": "robots.txt - Sitemap reference",
        "value": "present" if has_sitemap else "missing",
        "ok": has_sitemap,
        "note": "OK" if has_sitemap else "Add a 'Sitemap:' line to robots.txt"
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
            types.append("(invalid JSON-LD)")
    ok = len(blocks) > 0
    has_valuable = any(t in VALUABLE_SCHEMA for t in types)
    found = ", ".join(types) if types else "none"
    note = f"Types: {found}. " + ("Includes GEO-relevant schema." if has_valuable
                                   else "Consider FAQPage, Person, Organization.")
    if has_graph:
        note += " Uses @graph (good)."
    if not ok:
        note = "No JSON-LD found. Add schema markup (Layer 2)."
    return {"check": "Schema markup (JSON-LD)",
            "value": f"{len(blocks)} block(s)", "ok": ok, "note": note}


def check_canonical(body):
    m = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*>', body, flags=re.I)
    ok = m is not None
    return {"check": "Canonical tag", "value": "present" if ok else "missing",
            "ok": ok, "note": "OK" if ok
            else "Missing <link rel=canonical>. Add it to consolidate authority."}


def check_answer_first(body):
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, flags=re.S | re.I)
    h1_text = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else None
    p = re.search(r"<p[^>]*>(.*?)</p>", body, flags=re.S | re.I)
    p_text = re.sub(r"<[^>]+>", "", p.group(1)).strip() if p else ""
    p_words = len(p_text.split())
    ok = h1_text is not None and 15 <= p_words <= 120
    note = []
    if not h1_text:
        note.append("No H1.")
    if p_words == 0:
        note.append("No first text paragraph.")
    elif p_words < 15:
        note.append("First paragraph too short to contain the answer.")
    note.append("Manually verify the direct answer is in the first ~40–60 words (answer-first).")
    return {"check": "Answer-first signals",
            "value": f"H1: {'yes' if h1_text else 'no'} | 1st paragraph: ~{p_words} words",
            "ok": ok, "note": " ".join(note)}


def check_tables(body):
    tables = len(re.findall(r"<table", body, flags=re.I))
    return {"check": "HTML tables",
            "value": f"{tables} table(s)", "ok": True,
            "note": ("Real HTML tables detected (extractable by AI)." if tables
                     else "No <table> found. If you have comparison data, use an HTML table, not an image.")}


def check_alt_text(body):
    imgs = re.findall(r"<img[^>]*>", body, flags=re.I)
    if not imgs:
        return {"check": "Image alt-text", "value": "0 images",
                "ok": True, "note": "No images on the page."}
    with_alt = sum(1 for i in imgs
                   if re.search(r'alt=["\'][^"\']+["\']', i, flags=re.I))
    pct = round(100 * with_alt / len(imgs))
    ok = pct >= 90
    return {"check": "Image alt-text",
            "value": f"{with_alt}/{len(imgs)} ({pct}%)", "ok": ok,
            "note": "OK" if ok else "Add descriptive alt-text to images without alt."}


def main():
    if len(sys.argv) < 2:
        print("Usage: python audit_geo.py https://site.com")
        sys.exit(1)
    url = sys.argv[1]
    if not urlparse(url).scheme:
        url = "https://" + url
    base = f"{urlparse(url).scheme}://{urlparse(url).netloc}"

    print(f"\n=== GEO/AEO Audit: {url} ===\n")

    status, _, body, _ = fetch(url)
    if status is None:
        print(f"ERROR: could not access {url}\nDetails: {body}")
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
        mark = "[ OK ]" if r["ok"] else "[FAIL]"
        print(f"{mark} {r['check']}")
        print(f"        value: {r['value']}")
        print(f"        note:  {r['note']}\n")

    falhas = [r for r in results if not r["ok"]]
    print("=" * 55)
    print(f"Summary: {len(results) - len(falhas)}/{len(results)} checks OK.")
    if falhas:
        print("\nPriorities (fix first):")
        for r in falhas:
            print(f"  - {r['check']}: {r['note']}")
    print("\nNote: this script covers Layer 1 and basic signals from Layers")
    print("2, 3, and 6. Layers 4 and 5 (content strategy, external authority)")
    print("and continuous monitoring require manual analysis using the skill")
    print("reference docs (one per layer).\n")


if __name__ == "__main__":
    main()
