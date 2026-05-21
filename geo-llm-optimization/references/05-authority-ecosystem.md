# Layer 5 — Authority, Entity, and External Ecosystem

Generative engines synthesize answers from **multiple sources**, not only the brand’s website. Being present and well-positioned outside your own domain is what makes you a citable reference. This layer is continuous.

## Checklist

- [ ] Presence in communities (Reddit, Quora)
- [ ] YouTube optimization (transcripts and timestamps)
- [ ] Digital PR for earned media
- [ ] Entity consistency across channels
- [ ] Listings in industry directories
- [ ] Google Knowledge Graph / Knowledge Panel claim (when applicable)

---

## 5.1 Presence in communities (Reddit/Quora)

Systems like Perplexity and Google AI Overviews often prioritize **human-validated discussions**. Reddit and Quora frequently appear as cited sources.

- **Be genuinely helpful.** Answer real questions in your domain. Spam and self-promotion are counterproductive — the model picks up the negative signal.
- Target questions that are **Golden Prompts** (Layer 4.3) when they exist on these platforms.
- Keep identity consistent with your other channels (strengthens entity reconciliation — see 5.4).
- Dense answers with data and concrete steps are more likely to be extracted.
- Follow each community’s rules — getting banned removes a valuable source.

---

## 5.2 YouTube optimization

Videos can be primary sources of authority for many AI systems, but the model reads **text** — it does not “watch”.

- **Publish a full transcript**, reviewed (not only auto-captions). Also include it in the description or on a page on your site.
- Add **timestamps / chapters** — they turn the video into navigable chunks.
- Use question-like language in titles and descriptions (Layer 3.2).
- Write a rich description with key points and the cited data spelled out in text.
- Add `VideoObject` schema to the page hosting the video (Layer 2.10).

```
00:00 Opening question
01:30 Second topic phrased as a question
04:15 Third topic
```

---

## 5.3 Digital PR for earned media

In GEO, third-party mentions (earned media) often carry **more weight** than content owned by the brand (owned media). AI systems tend to trust people talking about you more than you talking about yourself.

- Prioritize being **mentioned** by reputable outlets, industry blogs, podcasts, and newsletters — even without a classic backlink, the mention is a trust vector.
- A few high-trust sources beat many weak ones.
- Favor positive, factual context (connects with sentiment monitoring — Layer 6.2).
- Tactics: contributed articles, proprietary data that others want to cite, expert commentary, “best of” roundups, podcasts, interviews.

---

## 5.4 Entity consistency

AI reconciles your brand as **an entity** by cross-checking information across many sources. Inconsistencies confuse the knowledge graph and weaken the entity.

Keep the following **identical everywhere**: company name, description, address, phone number, founding date, leadership. Especially check:
- LinkedIn
- Crunchbase
- Wikidata (and Wikipedia, if applicable)
- Google Business Profile
- Your `Organization` schema on the site (Layer 2.1)

One contradictory detail across two channels can be enough for the model to hesitate.

---

## 5.5 Listings in industry directories

Active, up-to-date profiles in industry directories and review platforms reinforce the entity and provide sources the model can consult.

- For SaaS/software: **G2**, **Capterra**.
- General reviews: **Trustpilot**.
- Niche-specific directories for your market.
- Keep profiles complete with consistent NAP (Name/Address/Phone) and current information (see 5.4).

---

## 5.6 Google Knowledge Graph / Knowledge Panel claim

The Google Knowledge Panel is a structured source that can feed AI Overviews and other systems.

- Check whether the brand/person has a Knowledge Panel.
- If available, **claim** it (Google allows verified owners to suggest edits).
- Keep displayed information accurate.
- Connect with `sameAs` and Wikidata (Layer 2.1) — these signals help Google build confidence in the entity.

---

## Expected output from this layer

Because this layer is continuous, deliver an **ecosystem presence plan**: which videos to optimize/create; which communities and Golden Prompts to monitor; a digital PR plan; an entity-consistency audit across channels (highlighting discrepancies); directories to create/update; Knowledge Panel status. Include a recommended cadence for each track.

