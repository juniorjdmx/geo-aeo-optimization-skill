# Camada 1 — Infraestrutura Técnica (IA-Ready)

Esta é a camada fundamental. Se o motor generativo não consegue **alcançar, renderizar e recuperar** o site rápido e com segurança, nenhuma otimização de conteúdo importa. Resolva isto primeiro.

## Checklist

- [ ] Configurar `llms.txt` e `llms-full.txt` na raiz do site
- [ ] Garantir Server-Side Rendering (SSR)
- [ ] Latência de resposta abaixo de 200ms
- [ ] Auditar `robots.txt` para liberar bots de recuperação
- [ ] Revisar regras de WAF / Cloudflare Bot Fight Mode
- [ ] Verificar indexação no Bing
- [ ] Protocolo HTTPS ativo e válido
- [ ] URLs estáveis e semânticas
- [ ] Implementar canonical tags
- [ ] Sitemap.xml atualizado
- [ ] Core Web Vitals otimizados (LCP, INP)

---

## 1.1 Arquivos llms.txt e llms-full.txt

Arquivos Markdown na raiz do domínio (`https://site.com/llms.txt`) que dão aos crawlers de IA um mapa curado do conteúdo e da hierarquia do site. Funcionam como um índice editorial legível por máquina.

- `llms.txt` — índice enxuto: visão geral do site + links para as páginas mais importantes, com uma frase descrevendo cada uma.
- `llms-full.txt` — documentação completa do site em Markdown simplificado, para processamento massivo: o modelo consome o conteúdo das páginas-chave sem precisar fazer fetch de cada URL.

Use o template em `assets/llms.txt.template`. Estrutura:

```markdown
# Nome do Site

> Descrição em uma frase do que o site/empresa faz e para quem.

## Páginas principais
- [Título](https://site.com/pagina): descrição de uma linha.

## Documentação
- [Guia X](https://site.com/docs/x): o que o leitor encontra aqui.

## Opcional
- [Páginas secundárias](https://site.com/secundaria): conteúdo de menor prioridade.
```

Regras: cada link com descrição curta; a seção `## Opcional` sinaliza conteúdo dispensável em contexto limitado; mantenha atualizado quando a estrutura mudar.

---

## 1.2 Server-Side Rendering (SSR)

Muitos crawlers de IA **não executam JavaScript** ou o fazem de forma limitada. Um SPA (React, Vue, Angular) que monta o conteúdo só no cliente pode aparecer **vazio** para esses bots.

Diagnóstico — o conteúdo precisa estar no HTML inicial:

```bash
curl -s https://site.com/pagina | grep -i "trecho-do-texto-principal"
```

Se o `curl` não retorna o texto principal, o site está invisível para crawlers sem renderização.

Soluções, em ordem de preferência: SSR nativo (Next.js, Nuxt, SvelteKit, Astro); Static Site Generation; pré-renderização (snapshot HTML para bots); dynamic rendering. O conteúdo crítico — resposta principal, dados, schema — **nunca** deve depender de interação ou chamada client-side.

---

## 1.3 Latência abaixo de 200ms

Motores generativos montam o conjunto de recuperação em tempo real e são "impacientes": se o site demora, é descartado do retrieval set. Meta: **TTFB < 200ms**.

```bash
curl -o /dev/null -s -w "TTFB: %{time_starttransfer}s | Total: %{time_total}s\n" https://site.com
```

Alavancas: CDN na frente de tudo; cache agressivo de HTML; edge rendering; reduzir trabalho síncrono no servidor; compressão (Brotli/gzip); HTTP/2 ou HTTP/3. A meta é para o **HTML inicial**, não para todos os assets.

---

## 1.4 Auditoria de robots.txt

O erro clássico: tentar bloquear bots de treinamento e, sem querer, bloquear os bots de **busca e recuperação** — os que trazem visibilidade nas respostas.

- **Bots de treinamento** (coletam dados para treinar modelos) — bloquear é decisão legítima de negócio. Ex: `GPTBot`, `Google-Extended`, `CCBot`.
- **Bots de busca/recuperação** (buscam conteúdo em tempo real para responder) — **nunca bloquear** se o objetivo é aparecer nas respostas. Ex: `OAI-SearchBot`, `PerplexityBot`, `Perplexity-User`, `ClaudeBot`.

Configuração que **libera explicitamente** os agentes de recuperação:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: ClaudeBot
Allow: /

# Bloqueio de treinamento (opcional, decisão do negócio)
User-agent: GPTBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: *
Allow: /
```

Cuidados: nunca use `Disallow: /` em `User-agent: *` achando que afeta só treinamento; os nomes de user-agents mudam, então quando o usuário pedir **verifique a documentação oficial atual** de OpenAI, Perplexity, Google e Anthropic antes de finalizar.

---

## 1.5 Regras de WAF / Cloudflare Bot Fight Mode

Muitos bloqueios de bot acontecem **fora do robots.txt**, na camada de firewall. O "Bot Fight Mode" do Cloudflare e regras de WAF podem barrar crawlers legítimos de IA mesmo com o robots.txt liberado.

Verifique e ajuste:
- No Cloudflare, revise "Bot Fight Mode" e "Super Bot Fight Mode" — eles podem desafiar ou bloquear `OAI-SearchBot`, `PerplexityBot` e similares.
- Crie regras de exceção (allowlist) para os user-agents de busca de IA legítimos.
- Em outros WAFs, procure regras de rate limiting ou de challenge baseadas em user-agent.
- Teste fazendo requests com o user-agent do bot e confirmando que recebem `200`, não `403` nem um challenge JS.

Um robots.txt perfeito não adianta se o WAF barra o crawler antes.

---

## 1.6 Indexação no Bing

O ChatGPT usa o índice do **Bing** para buscas em tempo real. Estar fora do Bing significa estar fora de uma parcela relevante das buscas de IA.

- Cadastre o site no **Bing Webmaster Tools**.
- Submeta o sitemap.xml lá.
- Verifique a contagem de páginas indexadas e corrija erros de rastreamento.
- Não basta estar no Google: trate o Bing como índice de primeira classe para GEO.

---

## 1.7 Protocolo HTTPS ativo

IAs **despriorizam ou ignoram** sites sem certificado de segurança válido. HTTPS é pré-requisito básico de confiança.

- Certificado válido, sem expiração e sem erro de cadeia.
- Redirecionamento 301 de `http://` para `https://`.
- Sem conteúdo misto (mixed content) — todos os assets servidos por HTTPS.

```bash
curl -sI https://site.com | head -1
curl -sI http://site.com | grep -i location
```

---

## 1.8 URLs estáveis e semânticas

URLs limpas ajudam o modelo a compreender a hierarquia e o tema de cada página.

- Use caminhos descritivos: `/servicos/implantacao-crm` vence `/p?id=8472`.
- Evite parâmetros aleatórios, IDs de sessão e tracking na URL canônica.
- URLs estáveis: uma vez publicada, não mude a URL; se precisar, use 301.
- Estrutura de pastas que reflita a hierarquia de topic clusters (ver Camada 4).

---

## 1.9 Canonical tags

Conteúdo duplicado ou similar dilui autoridade e citações entre várias URLs. A tag canonical consolida o sinal numa única página.

```html
<link rel="canonical" href="https://site.com/pagina-preferida" />
```

- Toda página deve declarar sua canonical (mesmo que aponte para si mesma).
- Variações com parâmetros, paginação ou versões mobile devem apontar para a URL principal.
- A canonical deve estar no HTML servido pelo servidor (ver 1.2 — se injetada via JS, o crawler pode não ver).

---

## 1.10 Sitemap.xml atualizado

O sitemap garante que as páginas prioritárias para citação sejam descobertas rápido.

- Liste as URLs canônicas, não as duplicadas.
- Mantenha `lastmod` real e atualizado — conecta com freshness (Camada 6).
- Submeta no Google Search Console e no Bing Webmaster Tools.
- Referencie o sitemap no robots.txt: `Sitemap: https://site.com/sitemap.xml`.
- Remova URLs mortas (404) do sitemap.

---

## 1.11 Core Web Vitals

Métricas de experiência da página afetam elegibilidade em recursos do Google, incluindo AI Overviews. Foco especial:

- **LCP (Largest Contentful Paint) < 2,5s** — o maior elemento visível carrega rápido.
- **INP (Interaction to Next Paint) < 200ms** — a página responde rápido à interação.
- **CLS (Cumulative Layout Shift) baixo** — layout estável, sem saltos.

Meça com PageSpeed Insights / Lighthouse e dados de campo (CrUX). Otimize imagens, reduza JS bloqueante, reserve espaço para elementos que carregam depois.

---

## Saída esperada desta camada

Ao trabalhar a Camada 1, entregue ao usuário:
- O `llms.txt` (e `llms-full.txt` se fizer sentido) gerado e pronto para subir.
- Diagnóstico de SSR, HTTPS, latência e Core Web Vitals, com rota de correção para cada falha.
- Um `robots.txt` revisado e a recomendação de ajuste no WAF/Cloudflare.
- Confirmação de presença no Bing Webmaster Tools.
- Revisão de URLs, canonical e sitemap.xml.
