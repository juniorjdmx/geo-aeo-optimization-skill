# Camada 2 — Dados Estruturados (Schema Markup Avançado)

Schema markup é o que o modelo lê como **fato declarado** sobre a página. Bem feito, ajuda a IA a identificar pares pergunta/resposta como "ground truth", alimentar agentes de compra, entender processos e consolidar a marca como entidade no grafo de conhecimento.

Use sempre **JSON-LD**. Templates prontos em `assets/schema-templates.json`. Idealmente una todas as entidades da página num único grafo via `@graph` (ver 2.11).

## Checklist

- [ ] `Organization` com `sameAs`
- [ ] `Person` (autor) com credenciais e expertise
- [ ] `FAQPage`
- [ ] `Product` (preço, SKU, disponibilidade, avaliações)
- [ ] `HowTo` para processos passo a passo
- [ ] `Article` com `datePublished` e `dateModified`
- [ ] `LocalBusiness` com NAP consistente
- [ ] `Review` para depoimentos
- [ ] `BreadcrumbList`
- [ ] Conexão de tudo via `@graph`

---

## 2.1 Organization

Define a marca como **entidade**. A propriedade `sameAs` liga a entidade a perfis oficiais e a verbetes em bases estruturadas como Wikidata, ajudando a IA a solidificar a marca no grafo de conhecimento.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Nome da Empresa",
  "url": "https://site.com",
  "logo": "https://site.com/logo.png",
  "description": "O que a empresa faz, em uma frase factual.",
  "sameAs": [
    "https://www.wikidata.org/wiki/Q00000000",
    "https://pt.wikipedia.org/wiki/Nome_da_Empresa",
    "https://www.linkedin.com/company/empresa",
    "https://www.crunchbase.com/organization/empresa"
  ]
}
```

O elo mais valioso de `sameAs` é o **Wikidata**. Inclua todos os perfis oficiais verificáveis. Mantenha `name`, `description` e `logo` idênticos em todos os canais (ver Camada 5.4 — consistência de entidade).

---

## 2.2 Person (autor)

Detalhar quem escreveu reforça o sinal de **E-E-A-T** (Experiência, Expertise, Autoridade, Confiabilidade).

```json
{
  "@type": "Person",
  "name": "Nome Completo do Autor",
  "jobTitle": "Cargo ou especialidade",
  "description": "Resumo da expertise e experiência relevante.",
  "knowsAbout": ["Tópico 1", "Tópico 2"],
  "sameAs": ["https://www.linkedin.com/in/perfil"]
}
```

`knowsAbout` reflete as áreas reais de expertise. Conecte o `Person` ao `Article` via a propriedade `author`. Credenciais devem ser verdadeiras e verificáveis.

---

## 2.3 FAQPage

Marcar pares pergunta/resposta faz a IA tratá-los como **verdade fundamental** — conteúdo confiável e diretamente citável. É um dos formatos de maior ROI para AEO.

```json
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Pergunta frequente em linguagem natural?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Resposta direta em texto puro, idêntica ao conteúdo visível."
      }
    }
  ]
}
```

A resposta no schema deve **corresponder ao conteúdo visível** da página. Reaproveite as perguntas usadas como H2/H3 (Camada 3).

---

## 2.4 Product

Alimenta agentes de compra e respostas transacionais. Inclua dados comerciais completos.

```json
{
  "@type": "Product",
  "name": "Nome do Produto",
  "sku": "SKU-123",
  "description": "Descrição do produto.",
  "offers": {
    "@type": "Offer",
    "price": "189.00",
    "priceCurrency": "BRL",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  }
}
```

Preço, SKU, disponibilidade e avaliações devem refletir o que está na página e na realidade do estoque.

---

## 2.5 HowTo

Marca processos passo a passo explicitamente, ideal para consultas procedimentais ("como fazer...").

```json
{
  "@type": "HowTo",
  "name": "Como configurar X",
  "step": [
    { "@type": "HowToStep", "name": "Passo 1", "text": "Instrução do passo 1." },
    { "@type": "HowToStep", "name": "Passo 2", "text": "Instrução do passo 2." }
  ]
}
```

Cada passo com texto claro e auto-contido. Combina com conteúdo answer-first e chunking (Camada 3).

---

## 2.6 Article

Use em todos os posts e páginas editoriais. `datePublished` e `dateModified` são essenciais — alimentam o sinal de freshness (Camada 6).

```json
{
  "@type": "Article",
  "headline": "Título do artigo, idealmente como pergunta",
  "datePublished": "2026-01-01",
  "dateModified": "2026-05-20",
  "author": { "@type": "Person", "name": "Nome do Autor" },
  "publisher": {
    "@type": "Organization",
    "name": "Nome da Empresa",
    "logo": { "@type": "ImageObject", "url": "https://site.com/logo.png" }
  }
}
```

Atualize o `dateModified` de verdade quando revisar o conteúdo.

---

## 2.7 LocalBusiness

Para negócios com presença física. A regra de ouro é a consistência absoluta de **NAP** (Nome, Endereço, Telefone) em todos os lugares.

```json
{
  "@type": "LocalBusiness",
  "name": "Nome do Negócio",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua Exemplo, 100",
    "addressLocality": "Cidade",
    "addressRegion": "UF",
    "postalCode": "00000-000"
  },
  "telephone": "+55-00-0000-0000"
}
```

O NAP do schema deve ser idêntico ao do Google Business Profile, diretórios e do conteúdo visível. Divergência confunde a IA.

---

## 2.8 Review

Marca depoimentos de clientes, aumentando o sinal de confiança.

```json
{
  "@type": "Review",
  "itemReviewed": { "@type": "Organization", "name": "Nome da Empresa" },
  "author": { "@type": "Person", "name": "Nome do Cliente" },
  "reviewRating": { "@type": "Rating", "ratingValue": "5" },
  "reviewBody": "Depoimento real do cliente."
}
```

Use só depoimentos reais. Reviews falsos detectados destroem a confiança.

---

## 2.9 BreadcrumbList

Sinaliza a hierarquia e o contexto da página, facilitando a "navegação" da IA pela estrutura do site.

```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Início", "item": "https://site.com" },
    { "@type": "ListItem", "position": 2, "name": "Serviços", "item": "https://site.com/servicos" }
  ]
}
```

Deve refletir o caminho real da URL e a estrutura de topic clusters (Camada 4).

---

## 2.10 Outros tipos úteis

Conforme o conteúdo: `QAPage` (página de uma pergunta com respostas da comunidade), `VideoObject` (vídeos, ver Camada 5.1), `Event`, `Recipe`, `JobPosting`. Use o tipo que descreve melhor o conteúdo real da página.

---

## 2.11 Conexão via @graph

Em vez de blocos JSON-LD soltos, una todas as entidades da página num **grafo único** com `@graph`. Isso dá ao modelo clareza máxima sobre como as entidades se relacionam (o artigo, seu autor, a organização publicadora, os breadcrumbs).

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "@id": "https://site.com/#org", "name": "..." },
    { "@type": "Person", "@id": "https://site.com/#autor", "name": "..." },
    {
      "@type": "Article",
      "author": { "@id": "https://site.com/#autor" },
      "publisher": { "@id": "https://site.com/#org" }
    }
  ]
}
```

Use `@id` para referenciar entidades entre si, evitando repetição e ambiguidade.

---

## Validação

Valide o JSON-LD em `validator.schema.org` e no Google Rich Results Test. Garanta que o markup está no HTML servido pelo servidor (ver Camada 1.2).

## Saída esperada desta camada

Entregue os blocos JSON-LD prontos e preenchidos com dados reais, idealmente unidos via `@graph`, com instrução de onde inserir e o lembrete de validar antes de publicar. Recomende sobre Wikidata: existe item? Vale criar?
