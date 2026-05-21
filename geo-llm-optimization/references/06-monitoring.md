# Layer 6 — Monitoring, Metrics, and Maintenance

Classic SEO measures rankings and clicks. GEO needs new metrics: whether the brand appears (or not) **inside a synthesized answer**. This layer is the feedback loop that validates everything else and keeps content alive.

## Checklist

- [ ] Measure Share of Model (SoM)
- [ ] Monitor AI sentiment about the brand
- [ ] Capture AI referral traffic in GA4
- [ ] Monthly citation audit
- [ ] Track citation rate
- [ ] Analyze ROI of AI referral traffic
- [ ] Recurring updates (freshness, ~every 90 days)
- [ ] Ensure factual integrity across the site
- [ ] Multimodal optimization (alt-text and metadata)
- [ ] Prepare for agentic commerce

Your measurement baseline is the set of **Golden Prompts** defined in Layer 4.3.

---

## 6.1 Share of Model (SoM)

Measure the **percentage of AI answers that cite your brand**, compared to competitors, across your Golden Prompts.

How to measure:
1. Run each Golden Prompt in each target engine (ChatGPT, Perplexity, Gemini, AI Overviews, Claude). Run each prompt multiple times (e.g., 3–5) and aggregate.
2. For each response, record whether your brand and competitors were mentioned.
3. **SoM** = responses that mention your brand / total responses.
4. Compare against competitors’ SoM.

Track SoM over time, by engine and by prompt. Prompts where the brand is absent become content priorities (Layer 4).

---

## 6.2 AI sentiment

It’s not enough to be mentioned — what matters is **how**. AI can position the brand positively, neutrally, or negatively. Repeated negative sentiment can create an implicit exclusion pattern: the model starts avoiding recommending the brand.

- For each response where the brand appears, classify sentiment and log the reason when negative.
- Track the trend over time.
- If negative sentiment repeats, investigate the root cause (reviews, forums, news) and address both the real issue and the narrative (Layer 5).

---

## 6.3 AI referral traffic in GA4

Configure **Google Analytics 4** to isolate visits coming from AI systems.

- Create a segment/channel for referrers such as `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`.
- Track volume, landing pages, and behavior separately.
- Without this, AI traffic often gets diluted into “referral” or “direct” and GEO impact becomes invisible.

---

## 6.4 Monthly citation audit

Each month, manually test your strategic prompts (Golden Prompts) and document:
- Did the brand appear? Where in the answer?
- In what context was it mentioned?
- Which sources were cited (your site, third parties, competitors)?

Keep a history to see progress and the impact of improvements.

---

## 6.5 Citation rate

Measure the **percentage of target queries where your domain shows up as a clickable link** in the AI answer. Unlike SoM (brand mention), citation rate counts **linked citations** to your domain. Track by engine over time.

---

## 6.6 ROI of AI referral traffic

AI-driven traffic often has higher intent because the user has already received a recommendation. Conversion rate can be significantly higher than traditional organic. Avoid quoting multipliers unless you have a verifiable source.

- Compare AI traffic conversion rate vs classic organic using your GA4 segments (6.3).
- Use the result to justify ongoing GEO investment.

---

## 6.7 Freshness — recurring updates

Generative models have a strong recency bias. Outdated content loses visibility. A ~**90-day** routine:

- Update stats and data to the latest values (with sources — Layer 3).
- Update visible “last updated” date and schema `dateModified` (Layer 2.6).
- Review references and broken links.
- Update `llms.txt` and `sitemap.xml` if structure changed.
- Reflect product/pricing/positioning changes consistently.

---

## 6.8 Factual integrity across the site

AI “hallucinates” about a brand when it finds **contradictory or imprecise** information on the site itself.

- Fix discrepancies about pricing, services, plans, and leadership across pages.
- Maintain a single source of truth for each fact.
- Pair this with entity consistency (Layer 5.4): coherence must hold within the site and across channels.

---

## 6.9 Multimodal optimization

Images and video can also be sources for AI — if the metadata is rich.

- Write **descriptive, factual alt-text** for every image (not “image1.jpg”).
- Use semantic filenames.
- Repeat in text any data shown in images (see Layer 3.4).
- For videos, publish transcripts and add `VideoObject` schema (Layer 5.2).

---

## 6.10 Preparation for agentic commerce

AI agents are starting to execute purchases and bookings autonomously. To participate:

- Maintain complete, up-to-date **product feeds** (price, availability, SKU).
- Implement `Product` schema with accurate commercial data (Layer 2.4).
- Keep price/stock consistent across page, schema, and feed.
- Ensure the purchase/booking flow is accessible and does not rely on interactions an agent cannot perform.

---

## Expected output from this layer

Deliver: the Golden Prompt list; a repeatable method/spreadsheet for SoM, sentiment, and citation rate; a current baseline vs competitors; GA4 AI segment configuration; a freshness calendar (~90 days); a factual-integrity audit; and a recommendation to re-measure after each optimization cycle.

