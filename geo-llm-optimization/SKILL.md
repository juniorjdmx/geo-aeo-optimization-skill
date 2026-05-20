---
name: geo-llm-optimization
description: Otimiza sites e conteúdo para o melhor posicionamento orgânico possível dentro de LLMs e motores de busca generativos (ChatGPT, Perplexity, Google AI Overviews, Gemini, Claude). Cobre GEO (Generative Engine Optimization) e AEO (Answer Engine Optimization) com um checklist de 58 pontos. Use SEMPRE que o usuário pedir para melhorar visibilidade em IA, ranquear em ChatGPT/Perplexity, aparecer em AI Overviews, criar arquivos llms.txt, otimizar conteúdo para ser citado por modelos, fazer auditoria GEO/AEO, escrever artigos "answer-first", aplicar schema markup para IA, montar topic clusters, ou qualquer variação de "como aparecer nas respostas de IA". Também ative quando o usuário falar de Share of Model, Golden Prompts, dark queries, chunking semântico, citation rate, tráfego de referência de IA, ou monitoramento de menções de marca em LLMs, mesmo sem citar "GEO" explicitamente.
---

# GEO / AEO: Otimização para LLMs

Posicionar um site ou marca para ser **recuperado, citado e recomendado** por motores generativos (ChatGPT, Perplexity, Google AI Overviews, Gemini, Claude). Isso é diferente de SEO clássico: o objetivo não é ranquear uma URL azul, é virar parte da resposta sintetizada pela IA.

## Modelo mental

Uma LLM responde em três etapas. Otimizar significa atacar cada uma:

1. **Recuperação (retrieval)** — o motor busca documentos relevantes em tempo real. Se o site é lento, bloqueia crawlers, não tem HTTPS ou depende de JS pesado, ele nunca entra no conjunto de recuperação. Coberto pela **Camada 1**.
2. **Extração e síntese** — o modelo lê o que recuperou, interpreta os dados estruturados e extrai trechos para montar a resposta. Conteúdo mal estruturado é descartado. Coberto pelas **Camadas 2, 3 e 4**.
3. **Citação e recomendação** — o modelo decide quais fontes citar e com que sentimento posicionar a marca. Coberto pelas **Camadas 5 e 6**.

Não pule etapas: um conteúdo perfeito (Camada 3) num site que a IA não consegue recuperar (Camada 1) tem visibilidade zero.

## Como usar esta skill

Identifique o que o usuário precisa e leia o arquivo de referência correspondente. **Não tente fazer tudo de memória** — cada referência tem checklists, exemplos de código e templates prontos.

| Pedido do usuário | Leia |
|---|---|
| llms.txt, SSR, latência, robots.txt, WAF, Bing, HTTPS, URLs, canonical, sitemap, Core Web Vitals | `references/01-infraestrutura.md` |
| Schema FAQPage, Person, Organization, Product, HowTo, Article, LocalBusiness, Review, Breadcrumb, @graph, sameAs, Wikidata | `references/02-schema-markup.md` |
| Answer-first, títulos como pergunta, TL;DR, chunking, citações, estatísticas, especialistas, tabelas, voz ativa, anti-fluff | `references/03-conteudo-geo.md` |
| Topic clusters, search intent, Golden Prompts, dark queries, experiência de primeira mão, author bylines | `references/04-semantica-intencao.md` |
| YouTube, Reddit/Quora, PR digital, consistência de entidade, diretórios, Knowledge Graph | `references/05-ecossistema-autoridade.md` |
| Share of Model, sentimento, GA4, citation rate, ROI de referência, freshness, integridade factual, multimodal, comércio agêntico | `references/06-monitoramento.md` |
| Auditoria automática de um site | `scripts/audit_geo.py` |

Se o pedido for amplo ("otimize meu site para IA"), faça uma **auditoria completa**: rode o script de auditoria, depois percorra as 6 referências na ordem 1 → 6 — cada uma abre com o checklist da sua camada — e trabalhe item por item.

## Fluxo de trabalho recomendado

1. **Diagnóstico.** Se há um site, rode `python scripts/audit_geo.py <url>` para um relatório automático (latência, SSR, HTTPS, robots.txt, llms.txt, sitemap, canonical, schema, tabelas, alt-text). Use o resultado para priorizar.
2. **Camada 1 primeiro.** Sem infraestrutura recuperável, nada mais importa.
3. **Camadas 2, 3 e 4 juntas.** Schema, conteúdo answer-first e arquitetura semântica se reforçam — trabalhe-os na mesma passada.
4. **Camadas 5 e 6 são contínuas.** Ecossistema e monitoramento não são tarefas únicas; entregue ao usuário um plano recorrente.
5. **Entregue um checklist priorizado.** Sempre feche com um plano de ação ordenado por impacto/esforço, não só uma lista de tudo que existe.

## Princípios que valem para qualquer entrega

- **Texto puro vence.** Dados, estatísticas, tabelas e respostas precisam estar em texto extraível, nunca presos em imagens, PDFs não-OCR ou componentes que só renderizam via JS no cliente.
- **Toda afirmação factual precisa de fonte.** Modelos confiam mais em conteúdo verificável. Vincule dados a fontes primárias e autoritárias (domínios .gov, .edu, papers, órgãos oficiais). Nunca invente números.
- **Blocos auto-contidos.** A IA extrai pedaços, não o artigo inteiro. Cada bloco de 100-300 tokens deve fazer sentido lido isoladamente.
- **Frescor importa.** Modelos generativos têm forte viés de recência. Conteúdo com data visível e atualizado a cada ~90 dias é favorecido.
- **A pergunta é o título.** H2/H3 escritos como perguntas naturais batem com o jeito que as pessoas perguntam para a IA.
- **Consistência de entidade.** Nome, descrição, dados e perfis da marca devem ser idênticos em todos os canais para a IA reconciliar a entidade.

## Formato de entrega esperado

Quando o usuário pedir uma auditoria ou plano, entregue:

1. **Resumo executivo** — 3-5 linhas sobre o estado atual e a maior alavanca.
2. **Achados por camada** — o que está OK, o que falta, organizado nas 6 camadas.
3. **Plano de ação priorizado** — tabela com tarefa, camada, impacto estimado (alto/médio/baixo) e esforço.
4. **Artefatos prontos** — quando aplicável, gere os arquivos reais (llms.txt, blocos de JSON-LD, conteúdo reescrito) em vez de só descrever.

Para arquivos como `llms.txt` e blocos de schema, use os templates em `assets/`.

## Erros comuns a evitar

- Tratar GEO como SEO clássico. Densidade de palavra-chave e link building tradicional não são o foco; estrutura extraível e autoridade de entidade são.
- Otimizar conteúdo num site que a IA não consegue renderizar, recuperar ou que não tem HTTPS válido.
- Esconder dados em imagens "para ficar bonito" — a IA não lê. Tabelas comparativas precisam ser HTML real.
- Citar estatísticas sem fonte. Isso reduz a confiança do modelo no documento inteiro.
- Bloquear `OAI-SearchBot`, `PerplexityBot` ou `ClaudeBot` no robots.txt — ou no WAF/Cloudflare Bot Fight Mode — por engano.
- Ignorar o Bing: o ChatGPT usa o índice do Bing para busca em tempo real.
- Deixar informações contraditórias sobre preço, serviço ou liderança no site — isso gera alucinações da IA sobre a marca.
- Entregar uma lista genérica de boas práticas sem priorizar pelo contexto real do site.
