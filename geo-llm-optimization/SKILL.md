---
name: geo-llm-optimization
description: Optimizes websites and content for the best possible organic positioning inside LLMs and generative search engines (ChatGPT, Perplexity, Google AI Overviews, Gemini, Claude). Covers GEO (Generative Engine Optimization) and AEO (Answer Engine Optimization) with a 58-point checklist. Use ALWAYS when the user asks to improve AI visibility, rank in ChatGPT/Perplexity, appear in AI Overviews, create llms.txt files, optimize content to be cited by models, run a GEO/AEO audit, write "answer-first" articles, apply AI-oriented schema markup, build topic clusters, or any variation of "how to appear in AI answers". Also activate when the user mentions Share of Model, Golden Prompts, dark queries, semantic chunking, citation rate, AI referral traffic, or brand mention monitoring across LLMs, even without explicitly saying "GEO".
---

# GEO / AEO: LLM Optimization

Position a website or brand to be **retrieved, cited, and recommended** by generative engines (ChatGPT, Perplexity, Google AI Overviews, Gemini, Claude). This is different from classic SEO: the goal is not to rank a blue URL — it is to become part of the answer the AI synthesizes.

## Mental model

An LLM answers in three stages. Optimizing means attacking each one:

1. **Retrieval** — the engine fetches relevant documents in real time. If the site is slow, blocks crawlers, lacks HTTPS, or relies on heavy JS, it never enters the retrieval set. Covered by **Layer 1**.
2. **Extraction and synthesis** — the model reads what it retrieved, interprets structured data, and extracts snippets to compose the answer. Poorly structured content is discarded. Covered by **Layers 2, 3, and 4**.
3. **Citation and recommendation** — the model decides which sources to cite and with what sentiment to position the brand. Covered by **Layers 5 and 6**.

Do not skip stages: perfect content (Layer 3) on a site the AI cannot retrieve (Layer 1) has zero visibility.

## How to use this skill

Identify what the user needs and read the matching reference file. **Do not try to do everything from memory** — each reference has checklists, code examples, and ready-to-use templates.

| User request | Read |
|---|---|
| llms.txt, SSR, latency, robots.txt, WAF, Bing, HTTPS, URLs, canonical, sitemap, Core Web Vitals | `references/01-infrastructure.md` |
| Schema FAQPage, Person, Organization, Product, HowTo, Article, LocalBusiness, Review, Breadcrumb, @graph, sameAs, Wikidata | `references/02-schema-markup.md` |
| Answer-first, headings as questions, TL;DR, chunking, citations, statistics, experts, tables, active voice, anti-fluff | `references/03-geo-content.md` |
| Topic clusters, search intent, Golden Prompts, dark queries, first-hand experience, author bylines | `references/04-semantics-intent.md` |
| YouTube, Reddit/Quora, digital PR, entity consistency, directories, Knowledge Graph | `references/05-authority-ecosystem.md` |
| Share of Model, sentiment, GA4, citation rate, referral ROI, freshness, factual integrity, multimodal, agentic commerce | `references/06-monitoring.md` |
| Automated site audit | `scripts/audit_geo.py` |

If the request is broad ("optimize my site for AI"), run a **full audit**: execute the audit script, then walk through the 6 references in order 1 → 6 — each one opens with its layer's checklist — and work item by item.

## Recommended workflow

1. **Diagnosis.** If there is a site, run `python scripts/audit_geo.py <url>` for an automated report (latency, SSR, HTTPS, robots.txt, llms.txt, sitemap, canonical, schema, tables, alt-text). Use the result to prioritize.
2. **Layer 1 first.** Without retrievable infrastructure, nothing else matters.
3. **Layers 2, 3, and 4 together.** Schema, answer-first content, and semantic architecture reinforce each other — work on them in the same pass.
4. **Layers 5 and 6 are continuous.** Ecosystem and monitoring are not one-off tasks; hand the user a recurring plan.
5. **Deliver a prioritized checklist.** Always close with an action plan ordered by impact/effort, not just a list of everything that exists.

## Principles that apply to every deliverable

- **Plain text wins.** Data, statistics, tables, and answers must be in extractable text, never trapped in images, non-OCR PDFs, or components that only render via client-side JS.
- **Every factual claim needs a source.** Models trust verifiable content more. Link data to primary and authoritative sources (.gov, .edu domains, papers, official bodies). Never make up numbers.
- **Self-contained blocks.** The AI extracts chunks, not the whole article. Each 100-300 token block must make sense read in isolation.
- **Freshness matters.** Generative models have a strong recency bias. Content with a visible date, updated roughly every 90 days, is favored.
- **The question is the heading.** H2/H3 written as natural questions match how people ask AI.
- **Entity consistency.** The brand's name, description, data, and profiles must be identical across all channels for the AI to reconcile the entity.

## Expected delivery format

When the user asks for an audit or a plan, deliver:

1. **Executive summary** — 3-5 lines on the current state and the biggest lever.
2. **Findings by layer** — what is OK, what is missing, organized across the 6 layers.
3. **Prioritized action plan** — table with task, layer, estimated impact (high/medium/low), and effort.
4. **Ready artifacts** — when applicable, generate the actual files (llms.txt, JSON-LD blocks, rewritten content) instead of just describing them.

For files like `llms.txt` and schema blocks, use the templates in `assets/`.

## Common mistakes to avoid

- Treating GEO as classic SEO. Keyword density and traditional link building are not the focus; extractable structure and entity authority are.
- Optimizing content on a site the AI cannot render, retrieve, or that lacks valid HTTPS.
- Hiding data in images "to look pretty" — the AI does not read them. Comparison tables must be real HTML.
- Citing statistics without a source. This lowers the model's trust in the entire document.
- Blocking `OAI-SearchBot`, `PerplexityBot`, or `ClaudeBot` in robots.txt — or in the WAF/Cloudflare Bot Fight Mode — by mistake.
- Ignoring Bing: ChatGPT uses the Bing index for real-time search.
- Leaving contradictory information about pricing, services, or leadership on the site — this triggers AI hallucinations about the brand.
- Delivering a generic best-practice list without prioritizing for the site's real context.
