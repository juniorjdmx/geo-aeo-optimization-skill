# Layer 4 — Semantics and Intent Strategy

Layers 2 and 3 handle individual pages. This layer handles the **strategy**: what content to create, for which questions, and how to organize it so the AI recognizes the site as the authority on an entire topic, not on isolated pages.

## Checklist

- [ ] Topic-cluster mastery (pillar pages + supporting content)
- [ ] Optimization for search intent (informational, consideration, transactional)
- [ ] Mapping of "Golden Prompts"
- [ ] Focus on "dark queries"
- [ ] Demonstrate first-hand experience
- [ ] Expert author bylines

---

## 4.1 Topic clusters

Instead of isolated articles, organize content into **clusters**: a comprehensive pillar page on a central topic, connected by links to several supporting pages that go deeper into subtopics.

- **Pillar page** — covers the broad topic comprehensively ("CRM guide for small businesses").
- **Supporting pages** — drill into subtopics ("How much does a CRM cost", "How to migrate data to a CRM", "CRM vs spreadsheet").
- **Internal links** — the pillar links out to every supporting page, and each supporting page links back to the pillar.

This signals deep topical coverage to the AI. The URL structure (Layer 1.8) and breadcrumbs (Layer 2.9) must mirror the cluster.

---

## 4.2 Search-intent optimization

Each piece of content must satisfy the **"why"** behind the question. Identify the intent and deliver what it asks for:

- **Informational** — the user wants to understand something ("what is", "how does it work"). Deliver a clear, complete explanation.
- **Consideration** — the user compares options ("X or Y", "best of", "is it worth it"). Deliver comparisons, tables, pros and cons.
- **Transactional** — the user wants to act ("buy", "hire", "price of"). Deliver commercial data, a clear CTA, Product schema.

Content that misses the intent does not get cited, no matter how well-written it is.

---

## 4.3 Golden Prompts mapping

**Golden Prompts** are the ~20 most valuable questions the target audience asks AIs and where the brand wants to be cited.

How to map them:
- Cover the journey: discovery, comparison, decision.
- Include questions where competitors are likely to appear.
- Prioritize by commercial value, not search volume.
- Keep the set fixed — it is the measurement baseline for Share of Model (Layer 6.1).

For each Golden Prompt, there must be content on the site that directly answers that question, in answer-first format (Layer 3.1).

---

## 4.4 Dark queries

"Dark queries" are questions with **zero volume** on Google — nobody types them there — but which AIs **generate internally** when decomposing a complex user question (the query fan-out process).

Example: the user asks "what is the best CRM for a clinic?". The AI may internally generate sub-questions like "CRMs with integrated scheduling", "HIPAA-compliant CRM for healthcare", "CRM cost for small clinics". Those sub-questions are dark queries.

Strategy: create content that answers the predictable sub-questions of your Golden Prompts, even when traditional keyword tools show zero volume. The traffic does not come from direct search — it comes from the AI retrieving that content while composing the answer.

---

## 4.5 First-hand experience

Models value the "E" for Experience in E-E-A-T. Show real engagement with the topic:

- Case studies with concrete results and numbers.
- Real photos (your own, not stock) with descriptive alt-text.
- Lessons learned "in the field": what went wrong, what you would adjust.
- Behind-the-scenes processes that only someone who has done the work knows.

Content that clearly comes from lived experience stands out from generic content and tends to be cited more often as an original source.

---

## 4.6 Expert author bylines

Make it **visible** who wrote each piece and why that person is qualified.

- Author signature visible on the page, with role and credential.
- Mini-bio explaining the expertise relevant to the topic.
- Link to a complete author page.
- Connect to the `Person` schema (Layer 2.2).

The AI uses the byline to assess source authority. Anonymous content conveys less trust.

---

## Expected output from this layer

Deliver: a topic-cluster map (pillars and supporting pages) with what already exists and what is missing; the Golden Prompts list defined together with the user; the predictable dark queries to cover; recommendations on where to add case studies and author bylines. This layer produces an **editorial plan**, not just page-level tweaks.
