# Layer 2 — Structured Data (Advanced Schema Markup)

Schema markup is what the model reads as **declared fact** about the page. Done well, it helps the AI identify question/answer pairs as "ground truth", feed shopping agents, understand processes, and consolidate the brand as an entity in the knowledge graph.

Always use **JSON-LD**. Ready templates live in `assets/schema-templates.json`. Ideally, join all entities on the page into a single graph via `@graph` (see 2.11).

## Checklist

- [ ] `Organization` with `sameAs`
- [ ] `Person` (author) with credentials and expertise
- [ ] `FAQPage`
- [ ] `Product` (price, SKU, availability, ratings)
- [ ] `HowTo` for step-by-step processes
- [ ] `Article` with `datePublished` and `dateModified`
- [ ] `LocalBusiness` with consistent NAP
- [ ] `Review` for testimonials
- [ ] `BreadcrumbList`
- [ ] Everything connected via `@graph`

---

## 2.1 Organization

Defines the brand as an **entity**. The `sameAs` property links the entity to official profiles and entries in structured bases like Wikidata, helping the AI solidify the brand in the knowledge graph.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://site.com",
  "logo": "https://site.com/logo.png",
  "description": "What the company does, in one factual sentence.",
  "sameAs": [
    "https://www.wikidata.org/wiki/Q00000000",
    "https://en.wikipedia.org/wiki/Company_Name",
    "https://www.linkedin.com/company/company",
    "https://www.crunchbase.com/organization/company"
  ]
}
```

The most valuable `sameAs` link is **Wikidata**. Include every verifiable official profile. Keep `name`, `description`, and `logo` identical across every channel (see Layer 5.4 — entity consistency).

---

## 2.2 Person (author)

Detailing who wrote the content reinforces the **E-E-A-T** signal (Experience, Expertise, Authoritativeness, Trustworthiness).

```json
{
  "@type": "Person",
  "name": "Author Full Name",
  "jobTitle": "Role or specialty",
  "description": "Summary of relevant expertise and experience.",
  "knowsAbout": ["Topic 1", "Topic 2"],
  "sameAs": ["https://www.linkedin.com/in/profile"]
}
```

`knowsAbout` reflects real areas of expertise. Connect `Person` to the `Article` via the `author` property. Credentials must be true and verifiable.

---

## 2.3 FAQPage

Marking up question/answer pairs makes the AI treat them as **ground truth** — trusted, directly citable content. It is one of the highest-ROI formats for AEO.

```json
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Common question in natural language?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Direct answer in plain text, identical to the visible content."
      }
    }
  ]
}
```

The answer in the schema must **match the visible content** on the page. Reuse the questions you used as H2/H3 (Layer 3).

---

## 2.4 Product

Feeds shopping agents and transactional answers. Include complete commercial data.

```json
{
  "@type": "Product",
  "name": "Product Name",
  "sku": "SKU-123",
  "description": "Product description.",
  "offers": {
    "@type": "Offer",
    "price": "189.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  }
}
```

Price, SKU, availability, and ratings must reflect what is on the page and the real inventory.

---

## 2.5 HowTo

Marks up step-by-step processes explicitly, ideal for procedural queries ("how to...").

```json
{
  "@type": "HowTo",
  "name": "How to set up X",
  "step": [
    { "@type": "HowToStep", "name": "Step 1", "text": "Instruction for step 1." },
    { "@type": "HowToStep", "name": "Step 2", "text": "Instruction for step 2." }
  ]
}
```

Each step with clear, self-contained text. Pairs with answer-first content and chunking (Layer 3).

---

## 2.6 Article

Use on every editorial post and page. `datePublished` and `dateModified` are essential — they feed the freshness signal (Layer 6).

```json
{
  "@type": "Article",
  "headline": "Article title, ideally phrased as a question",
  "datePublished": "2026-01-01",
  "dateModified": "2026-05-20",
  "author": { "@type": "Person", "name": "Author Name" },
  "publisher": {
    "@type": "Organization",
    "name": "Company Name",
    "logo": { "@type": "ImageObject", "url": "https://site.com/logo.png" }
  }
}
```

Update `dateModified` for real when you revise the content.

---

## 2.7 LocalBusiness

For businesses with a physical presence. The golden rule is absolute **NAP** (Name, Address, Phone) consistency everywhere.

```json
{
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Example St",
    "addressLocality": "City",
    "addressRegion": "ST",
    "postalCode": "00000"
  },
  "telephone": "+1-000-000-0000"
}
```

The schema's NAP must be identical to the Google Business Profile, directories, and the visible content. Divergence confuses the AI.

---

## 2.8 Review

Marks up customer testimonials, increasing the trust signal.

```json
{
  "@type": "Review",
  "itemReviewed": { "@type": "Organization", "name": "Company Name" },
  "author": { "@type": "Person", "name": "Customer Name" },
  "reviewRating": { "@type": "Rating", "ratingValue": "5" },
  "reviewBody": "Real customer testimonial."
}
```

Use only real testimonials. Fake reviews, once detected, destroy trust.

---

## 2.9 BreadcrumbList

Signals the page's hierarchy and context, making it easier for the AI to "navigate" the site's structure.

```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://site.com" },
    { "@type": "ListItem", "position": 2, "name": "Services", "item": "https://site.com/services" }
  ]
}
```

It must mirror the real URL path and the topic-cluster structure (Layer 4).

---

## 2.10 Other useful types

Depending on the content: `QAPage` (a page with one question and community answers), `VideoObject` (videos, see Layer 5.1), `Event`, `Recipe`, `JobPosting`. Use the type that best describes the actual content of the page.

---

## 2.11 Connecting via @graph

Instead of scattered JSON-LD blocks, join all page entities into a **single graph** with `@graph`. This gives the model maximum clarity about how entities relate (the article, its author, the publishing organization, the breadcrumbs).

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "@id": "https://site.com/#org", "name": "..." },
    { "@type": "Person", "@id": "https://site.com/#author", "name": "..." },
    {
      "@type": "Article",
      "author": { "@id": "https://site.com/#author" },
      "publisher": { "@id": "https://site.com/#org" }
    }
  ]
}
```

Use `@id` to reference entities between blocks, avoiding repetition and ambiguity.

---

## Validation

Validate the JSON-LD at `validator.schema.org` and Google's Rich Results Test. Make sure the markup is in the server-rendered HTML (see Layer 1.2).

## Expected output from this layer

Deliver ready-to-use JSON-LD blocks filled with real data, ideally joined via `@graph`, with instructions for where to insert them and the reminder to validate before publishing. Provide a Wikidata recommendation: is there an item? Is it worth creating one?
