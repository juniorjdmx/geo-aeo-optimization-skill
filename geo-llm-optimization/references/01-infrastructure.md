# Layer 1 — Technical Infrastructure (AI-Ready)

This is the foundational layer. If the generative engine cannot **reach, render, and retrieve** the site quickly and safely, no content optimization matters. Fix this first.

## Checklist

- [ ] Set up `llms.txt` and `llms-full.txt` at the site root
- [ ] Ensure Server-Side Rendering (SSR)
- [ ] Response latency below 200ms
- [ ] Audit `robots.txt` to allow retrieval bots
- [ ] Review WAF / Cloudflare Bot Fight Mode rules
- [ ] Verify Bing indexing
- [ ] Active and valid HTTPS protocol
- [ ] Stable, semantic URLs
- [ ] Implement canonical tags
- [ ] Up-to-date sitemap.xml
- [ ] Optimized Core Web Vitals (LCP, INP)

---

## 1.1 llms.txt and llms-full.txt files

Markdown files at the domain root (`https://site.com/llms.txt`) that give AI crawlers a curated map of the site's content and hierarchy. They act as a machine-readable editorial index.

- `llms.txt` — lean index: site overview + links to the most important pages, with one sentence describing each.
- `llms-full.txt` — complete site documentation in simplified Markdown, for bulk processing: the model consumes the content of key pages without needing to fetch each URL.

Use the template at `assets/llms.txt.template`. Structure:

```markdown
# Site Name

> One-sentence description of what the site/company does and for whom.

## Main pages
- [Title](https://site.com/page): one-line description.

## Documentation
- [Guide X](https://site.com/docs/x): what the reader will find here.

## Optional
- [Secondary pages](https://site.com/secondary): lower-priority content.
```

Rules: every link has a short description; the `## Optional` section signals content that can be skipped under limited context; keep it updated whenever the structure changes.

---

## 1.2 Server-Side Rendering (SSR)

Many AI crawlers **do not execute JavaScript** or do so in a limited way. An SPA (React, Vue, Angular) that mounts content only on the client may appear **empty** to those bots.

Diagnosis — the content must be in the initial HTML:

```bash
curl -s https://site.com/page | grep -i "snippet-of-main-text"
```

If `curl` does not return the main text, the site is invisible to non-rendering crawlers.

Solutions, in order of preference: native SSR (Next.js, Nuxt, SvelteKit, Astro); Static Site Generation; pre-rendering (HTML snapshot for bots); dynamic rendering. Critical content — main answer, data, schema — must **never** depend on interaction or client-side calls.

---

## 1.3 Latency below 200ms

Generative engines build the retrieval set in real time and are "impatient": if the site is slow, it gets dropped from the retrieval set. Target: **TTFB < 200ms**.

```bash
curl -o /dev/null -s -w "TTFB: %{time_starttransfer}s | Total: %{time_total}s\n" https://site.com
```

Levers: CDN in front of everything; aggressive HTML caching; edge rendering; reduce synchronous work on the server; compression (Brotli/gzip); HTTP/2 or HTTP/3. The target applies to the **initial HTML**, not to every asset.

---

## 1.4 robots.txt audit

The classic mistake: trying to block training bots and accidentally blocking **search and retrieval** bots — the ones that bring visibility into answers.

- **Training bots** (collect data to train models) — blocking is a legitimate business decision. Examples: `GPTBot`, `Google-Extended`, `CCBot`.
- **Search/retrieval bots** (fetch content in real time to answer) — **never block** these if the goal is to appear in answers. Examples: `OAI-SearchBot`, `PerplexityBot`, `Perplexity-User`, `ClaudeBot`.

Configuration that **explicitly allows** retrieval agents:

```
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: ClaudeBot
Allow: /

# Training block (optional, business decision)
User-agent: GPTBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: *
Allow: /
```

Caveats: never use `Disallow: /` under `User-agent: *` thinking it only affects training; user-agent names change, so when the user asks, **check the current official documentation** of OpenAI, Perplexity, Google, and Anthropic before finalizing.

---

## 1.5 WAF / Cloudflare Bot Fight Mode rules

Many bot blocks happen **outside of robots.txt**, at the firewall layer. Cloudflare's "Bot Fight Mode" and WAF rules can stop legitimate AI crawlers even with robots.txt open.

Check and adjust:
- In Cloudflare, review "Bot Fight Mode" and "Super Bot Fight Mode" — they may challenge or block `OAI-SearchBot`, `PerplexityBot`, and similar agents.
- Create allowlist rules for the legitimate AI search user-agents.
- In other WAFs, look for rate-limiting or challenge rules based on user-agent.
- Test by sending requests with the bot's user-agent and confirming a `200` response, not `403` or a JS challenge.

A perfect robots.txt is useless if the WAF blocks the crawler first.

---

## 1.6 Bing indexing

ChatGPT uses the **Bing** index for real-time searches. Being absent from Bing means being absent from a meaningful share of AI searches.

- Register the site in **Bing Webmaster Tools**.
- Submit the sitemap.xml there.
- Verify the count of indexed pages and fix crawl errors.
- Being on Google is not enough: treat Bing as a first-class index for GEO.

---

## 1.7 Active HTTPS protocol

AIs **deprioritize or ignore** sites without a valid security certificate. HTTPS is a baseline trust requirement.

- Valid certificate, not expired, no chain errors.
- 301 redirect from `http://` to `https://`.
- No mixed content — every asset served over HTTPS.

```bash
curl -sI https://site.com | head -1
curl -sI http://site.com | grep -i location
```

---

## 1.8 Stable, semantic URLs

Clean URLs help the model understand the hierarchy and topic of each page.

- Use descriptive paths: `/services/crm-implementation` beats `/p?id=8472`.
- Avoid random parameters, session IDs, and tracking on the canonical URL.
- Stable URLs: once published, do not change the URL; if you must, use a 301.
- Folder structure that reflects the topic-cluster hierarchy (see Layer 4).

---

## 1.9 Canonical tags

Duplicate or near-duplicate content dilutes authority and citations across multiple URLs. The canonical tag consolidates the signal into a single page.

```html
<link rel="canonical" href="https://site.com/preferred-page" />
```

- Every page must declare its canonical (even self-referential).
- Variants with parameters, pagination, or mobile versions must point to the main URL.
- The canonical must be in the server-rendered HTML (see 1.2 — if injected via JS, the crawler may miss it).

---

## 1.10 Up-to-date sitemap.xml

The sitemap ensures that pages prioritized for citation are discovered quickly.

- List canonical URLs, not duplicates.
- Keep `lastmod` real and current — it ties into freshness (Layer 6).
- Submit it to Google Search Console and Bing Webmaster Tools.
- Reference the sitemap in robots.txt: `Sitemap: https://site.com/sitemap.xml`.
- Remove dead URLs (404s) from the sitemap.

---

## 1.11 Core Web Vitals

Page-experience metrics affect eligibility for Google features, including AI Overviews. Focus on:

- **LCP (Largest Contentful Paint) < 2.5s** — the largest visible element loads quickly.
- **INP (Interaction to Next Paint) < 200ms** — the page responds quickly to interaction.
- **CLS (Cumulative Layout Shift) low** — stable layout, no jumps.

Measure with PageSpeed Insights / Lighthouse and field data (CrUX). Optimize images, reduce blocking JS, reserve space for elements that load later.

---

## Expected output from this layer

When working on Layer 1, deliver to the user:
- The generated `llms.txt` (and `llms-full.txt` when relevant), ready to publish.
- A diagnosis of SSR, HTTPS, latency, and Core Web Vitals, with a fix path for each failure.
- A revised `robots.txt` and the recommended adjustment in the WAF/Cloudflare.
- Confirmation of presence in Bing Webmaster Tools.
- A review of URLs, canonical, and sitemap.xml.
