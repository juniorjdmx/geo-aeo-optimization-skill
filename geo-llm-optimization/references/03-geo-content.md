# Layer 3 — Content Architecture and Visibility (GEO)

After the AI retrieves the site (Layer 1) and reads its structured data (Layer 2), it needs to **extract useful snippets** from the content. Poorly structured content gets retrieved but never used. This layer makes content extractable and citable.

## Checklist

- [ ] "Answer-First" (BLUF) structure in the first 40-60 words
- [ ] H2/H3 headings written as questions
- [ ] TL;DR blocks with 4-6 bullets at the top of long pieces
- [ ] Statistics in plain text every 150-200 words
- [ ] Quotes from named experts
- [ ] Citations from high-trust sources
- [ ] Semantic chunking in 100-300 token blocks
- [ ] Real HTML tables for comparative data
- [ ] Numbered lists and bullets for scannable content
- [ ] Define technical terms on first use
- [ ] Sentences in active voice
- [ ] Conversational writing
- [ ] Contextual sufficiency in every paragraph
- [ ] Removal of "fluff"

---

## 3.1 Answer-First structure (BLUF)

BLUF = Bottom Line Up Front. The direct answer to the main question must appear in the **first 40 to 60 words**, right below the H1 or H2. Models extract the start of the block as the candidate answer.

```
## How much does it cost to implement a CRM for small businesses?

[Direct answer, 40-60 words] Implementing a CRM for a small business
costs, on average, between X and Y, including license, setup, and training.
The price varies with the number of users and the level of automation.

[After that: development, context, nuance.]
```

The opening answer must stand on its own. Each section repeats the pattern. No warm-up paragraphs before the answer.

---

## 3.2 Question-based headings

People ask AI in natural language. H2s and H3s written as the user's natural question match the queries: "How do I set up llms.txt?" beats "llms.txt configuration". Reuse these headings as questions in the `FAQPage` schema (Layer 2.3).

---

## 3.3 TL;DR blocks

At the top of long content, include a summary of **4 to 6 bullets** covering the key points. It is an extremely high-extraction chunk: the AI grabs the TL;DR as a ready-made synthesis. Each bullet self-contained and factual.

---

## 3.4 Statistics and quantitative data

Content with concrete numbers is more extractable and citable. Target: **one quantitative data point every 150-200 words**.

- Numbers, percentages, and quantities **in plain text** — never trapped in images or infographics.
- If a chart is required, repeat the data point in text in the body or the caption.
- Each statistic with an explicit source (see 3.6).
- Prefer specific data: "reduced response time by 42%" beats "reduced it a lot".

GEO studies suggest visibility gains of around 31% with consistent use of statistics. Cite that number only if you can produce a verifiable source; otherwise apply the principle without the number.

---

## 3.5 Expert quotes

Direct quotes from **named** experts add authority and break up monolithic blocks.

```
"[Specific expert insight.]"
— [Full Name], [role/credential], [organization]
```

The expert must be real, named, and have a verifiable credential. The quote must add insight. GEO studies suggest gains around 41% — only apply the number with a source.

---

## 3.6 Source citations

Linking every factual claim to a primary, authoritative source increases the model's confidence.

- Prefer **primary sources**: official bodies, papers, data from `.gov` and `.edu` domains.
- The link should be explicit and clickable, close to the claim.
- In editorial content, keep the source visible in text: "According to [source]...".
- Never invent attributions or numbers. Without a verifiable source, do not use the data point.

GEO studies suggest gains around 27% — only apply the number with a source.

---

## 3.7 Semantic chunking

The AI extracts **blocks**, not entire articles. Organize the content into **self-contained chunks of 100 to 300 tokens** (~75 to 225 words) that make sense when read in isolation.

- Each block covers a complete idea, with enough context to stand alone.
- Use an H2/H3 before each block as a label.
- Avoid pronouns and external references ("as we saw above", "this") — repeat the subject.
- Test: copy a block in isolation; if it needs outside context, rewrite it.

---

## 3.8 Real HTML tables

Comparative data must live in **real HTML tables** (`<table>`), never in images or screenshots. The AI extracts rows and columns from HTML tables; it gets nothing from an image.

This applies to product comparisons, plans, pricing, pros and cons. Give each table a title/caption for context.

---

## 3.9 Numbered lists and bullets

Models prefer scannable formats when generating summaries. Use numbered lists for sequences and processes, bullets for sets of items. Each item concise and self-contained.

---

## 3.10 Defining technical terms

Explain every complex concept on its **first use**. This creates a "citable knowledge unit": the definition becomes a chunk the AI can extract to answer "what is X". Format: term + direct definition in the same sentence or the next one.

---

## 3.11 Active voice

"The CRM organizes contacts" beats "Contacts are organized by the CRM". Active voice is semantically clearer and easier to process and extract.

---

## 3.12 Conversational writing

Match the tone to how people actually speak and ask questions. Short sentences, one idea per sentence. Avoid unnecessary jargon; when you use a technical term, define it (see 3.10).

---

## 3.13 Contextual sufficiency

Every paragraph must be understandable **in isolation**, without leaning heavily on prior references. This is the chunking principle (3.7) applied paragraph by paragraph. Repeat the subject instead of using "it", "this", "that process".

---

## 3.14 Removing "fluff"

Cut generic introductions, warm-up sentences, and redundancies that add no factual information. Lean, dense content is more extractable; "fluff" dilutes chunks and delays the direct answer.

---

## Expected output from this layer

Deliver the rewritten content (or a page-by-page diagnosis) with: answer-first applied, headings converted into questions, TL;DR added, callouts where sources/statistics/experts are missing, comparative data converted into HTML tables, and the content reorganized into self-contained chunks without fluff.
