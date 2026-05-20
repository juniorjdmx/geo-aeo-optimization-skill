# Camada 4 — Semântica e Estratégia de Intenção

As Camadas 2 e 3 cuidam de páginas individuais. Esta camada cuida da **estratégia**: que conteúdo criar, para quais perguntas, e como organizá-lo para que a IA reconheça o site como autoridade num tema inteiro, não em páginas soltas.

## Checklist

- [ ] Domínio de topic clusters (páginas pilar + conteúdo de suporte)
- [ ] Otimização para search intent (informativa, consideração, transacional)
- [ ] Mapeamento de "Golden Prompts"
- [ ] Foco em "dark queries"
- [ ] Demonstrar experiência de primeira mão
- [ ] Expert author bylines

---

## 4.1 Topic clusters

Em vez de artigos isolados, organize o conteúdo em **clusters**: uma página pilar abrangente sobre um tema central, conectada por links a várias páginas de suporte que aprofundam subtópicos.

- **Página pilar** — cobre o tema amplo de forma completa ("Guia de CRM para pequenas empresas").
- **Páginas de suporte** — aprofundam subtópicos ("Quanto custa um CRM", "Como migrar dados para um CRM", "CRM vs planilha").
- **Links internos** — a pilar linka para todas as de suporte, e cada uma de suporte linka de volta para a pilar.

Isso sinaliza à IA cobertura temática profunda. A estrutura de URLs (Camada 1.8) e os breadcrumbs (Camada 2.9) devem refletir o cluster.

---

## 4.2 Otimização para search intent

Cada conteúdo deve satisfazer o **"porquê"** por trás da pergunta. Identifique a intenção e entregue o que ela pede:

- **Informativa** — o usuário quer entender algo ("o que é", "como funciona"). Entregue explicação clara e completa.
- **Consideração** — o usuário compara opções ("X ou Y", "melhores", "vale a pena"). Entregue comparativos, tabelas, prós e contras.
- **Transacional** — o usuário quer agir ("comprar", "contratar", "preço de"). Entregue dados comerciais, CTA claro, schema de Product.

Conteúdo que erra a intenção não é citado, por melhor que seja escrito.

---

## 4.3 Mapeamento de Golden Prompts

Os **Golden Prompts** são as ~20 perguntas mais valiosas que o público-alvo faz às IAs e onde a marca quer ser citada.

Como mapear:
- Cubra a jornada: descoberta, comparação, decisão.
- Inclua perguntas onde os concorrentes provavelmente aparecem.
- Priorize por valor comercial, não por volume de busca.
- Mantenha o conjunto fixo — ele é a base de medição do Share of Model (Camada 6.1).

Para cada Golden Prompt, deve existir conteúdo no site que responda diretamente àquela pergunta, em formato answer-first (Camada 3.1).

---

## 4.4 Dark queries

"Dark queries" são perguntas de **volume zero** no Google — ninguém as digita lá — mas que as IAs **geram internamente** ao decompor uma pergunta complexa do usuário (processo de query fan-out).

Exemplo: o usuário pergunta "qual o melhor CRM para uma clínica?". A IA pode gerar internamente sub-perguntas como "CRMs com agendamento integrado", "CRM compatível com LGPD para saúde", "custo de CRM para clínicas pequenas". Essas sub-perguntas são dark queries.

Estratégia: crie conteúdo que responda às sub-perguntas previsíveis dos seus Golden Prompts, mesmo que ferramentas de keyword tradicionais mostrem volume zero. O tráfego não vem da busca direta — vem de a IA recuperar esse conteúdo ao montar a resposta.

---

## 4.5 Experiência de primeira mão

Modelos valorizam o "E" de Experiência no E-E-A-T. Demonstre vivência real do tema:

- Estudos de caso com resultados concretos e números.
- Fotos reais (próprias, não banco de imagens) com alt-text descritivo.
- Lições aprendidas "no campo": o que deu errado, o que você ajustaria.
- Processos e bastidores que só quem fez de verdade conhece.

Conteúdo claramente vivido se distingue de conteúdo genérico e tende a ser mais citado como fonte original.

---

## 4.6 Expert author bylines

Torne **visível** quem escreveu cada conteúdo e por que essa pessoa é qualificada.

- Assinatura do autor visível na página, com cargo e credencial.
- Mini-bio explicando a expertise relevante para aquele tema.
- Link para uma página de autor completa.
- Conecte ao `Person` schema (Camada 2.2).

A IA usa o byline para avaliar a autoridade da fonte. Conteúdo anônimo transmite menos confiança.

---

## Saída esperada desta camada

Entregue: um mapa de topic clusters (pilares e páginas de suporte) com o que já existe e o que falta criar; a lista de Golden Prompts definida com o usuário; as dark queries previsíveis a cobrir; recomendações de onde adicionar estudos de caso e bylines de autor. Esta camada produz um **plano editorial**, não só ajustes de página.
