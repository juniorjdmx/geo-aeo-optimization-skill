# Camada 3 — Arquitetura de Conteúdo e Visibilidade (GEO)

Depois que a IA recupera o site (Camada 1) e lê seus dados estruturados (Camada 2), ela precisa **extrair trechos úteis** do conteúdo. Conteúdo mal estruturado é recuperado mas não usado. Esta camada faz o conteúdo ser extraível e citável.

## Checklist

- [ ] Estrutura "Answer-First" (BLUF) nas primeiras 40-60 palavras
- [ ] Títulos H2/H3 baseados em perguntas
- [ ] Blocos TL;DR com 4-6 bullets no início de conteúdos longos
- [ ] Estatísticas em texto puro a cada 150-200 palavras
- [ ] Citações de especialistas nomeados
- [ ] Citação de fontes de alta confiança
- [ ] Chunking semântico em blocos de 100-300 tokens
- [ ] Tabelas HTML reais para dados comparativos
- [ ] Listas numeradas e bullets para conteúdo scannável
- [ ] Definição de termos técnicos no primeiro uso
- [ ] Frases em voz ativa
- [ ] Escrita conversacional
- [ ] Suficiência contextual de cada parágrafo
- [ ] Eliminação de "fluff"

---

## 3.1 Estrutura Answer-First (BLUF)

BLUF = Bottom Line Up Front. A resposta direta à pergunta principal deve aparecer nas **primeiras 40 a 60 palavras**, logo abaixo do H1 ou H2. Modelos extraem o início do bloco como candidato a resposta.

```
## Quanto custa implantar um CRM para pequenas empresas?

[Resposta direta, 40-60 palavras] Implantar um CRM para uma pequena empresa
custa, em média, entre X e Y, considerando licença, configuração e treinamento.
O valor varia conforme o número de usuários e o nível de automação.

[Depois disso: desenvolvimento, contexto, nuances.]
```

A resposta inicial precisa fazer sentido lida sozinha. Cada seção repete o padrão. Sem parágrafos de aquecimento antes da resposta.

---

## 3.2 Títulos baseados em perguntas

As pessoas perguntam para a IA em linguagem natural. H2 e H3 escritos como a pergunta natural do usuário casam com as queries: "Como configurar o llms.txt?" vence "Configuração de llms.txt". Reaproveite esses títulos como perguntas no `FAQPage` schema (Camada 2.3).

---

## 3.3 Blocos TL;DR

No início de conteúdos longos, inclua um resumo com **4 a 6 bullets** cobrindo os pontos-chave. É um chunk de altíssima extração: a IA pega o TL;DR como síntese pronta. Cada bullet auto-contido e factual.

---

## 3.4 Estatísticas e dados quantitativos

Conteúdo com números concretos é mais extraível e citável. Meta: **um dado quantitativo a cada 150-200 palavras**.

- Números, porcentagens e quantidades **em texto puro** — nunca presos em imagens ou infográficos.
- Se um gráfico for necessário, repita o dado em texto no corpo ou na legenda.
- Cada estatística com fonte explícita (ver 3.6).
- Prefira dados específicos: "reduziu o tempo de resposta em 42%" vence "reduziu bastante".

Estudos de GEO indicam ganho de visibilidade na faixa de ~31% com uso consistente de estatísticas. Cite este número apenas se houver fonte verificável; caso contrário, aplique o princípio sem o número.

---

## 3.5 Citações de especialistas

Depoimentos diretos de especialistas **nomeados** conferem autoridade e quebram blocos monolíticos.

```
"[Insight específico do especialista.]"
— [Nome completo], [cargo/credencial], [organização]
```

O especialista precisa ser real, nomeado e com credencial verificável. A citação deve agregar insight. Estudos de GEO indicam ganho na faixa de ~41% — aplicar o número só com fonte.

---

## 3.6 Citação de fontes

Vincular cada afirmação factual a uma fonte primária e autoritária aumenta a confiança do modelo.

- Prefira **fontes primárias**: órgãos oficiais, papers, dados de domínios `.gov` e `.edu`.
- O link deve ser explícito e clicável, próximo da afirmação.
- Em conteúdo editorial, deixe a fonte visível em texto: "Segundo a [fonte]...".
- Nunca invente atribuições nem números. Sem fonte verificável, não use o dado.

Estudos de GEO indicam ganho na faixa de ~27% — aplicar o número só com fonte.

---

## 3.7 Chunking semântico

A IA extrai **blocos**, não o artigo inteiro. Organize o conteúdo em chunks **auto-contidos de 100 a 300 tokens** (~75 a 225 palavras) que façam sentido lidos isoladamente.

- Cada bloco trata de uma ideia completa, com contexto suficiente para ser entendido sozinho.
- Use um H2/H3 antes de cada bloco como rótulo.
- Evite pronomes e referências externas ao bloco ("como vimos acima", "isso") — repita o sujeito.
- Teste: copie um bloco isolado; se precisa de contexto externo, reescreva.

---

## 3.8 Tabelas HTML reais

Dados comparativos devem estar em **tabelas HTML reais** (`<table>`), nunca em imagens ou capturas de tela. A IA extrai linhas e colunas de tabelas HTML; de uma imagem, não extrai nada.

Vale para comparativos de produtos, planos, preços, prós e contras. Cada tabela com um título/legenda que a contextualize.

---

## 3.9 Listas numeradas e bullets

Modelos preferem formatos scannáveis para gerar resumos. Use listas numeradas para sequências e processos, bullets para conjuntos de itens. Cada item conciso e auto-contido.

---

## 3.10 Definição de termos técnicos

Explique cada conceito complexo no seu **primeiro uso**. Isso cria uma "unidade de conhecimento citável": a definição vira um chunk que a IA pode extrair para responder "o que é X". Formato: termo + definição direta na mesma frase ou na seguinte.

---

## 3.11 Voz ativa

"O CRM organiza os contatos" vence "Os contatos são organizados pelo CRM". A voz ativa é mais clara semanticamente e mais fácil de processar e extrair.

---

## 3.12 Escrita conversacional

Adapte o tom para como as pessoas realmente falam e perguntam. Frases curtas, uma ideia por frase. Evite jargão desnecessário; quando usar termo técnico, defina-o (ver 3.10).

---

## 3.13 Suficiência contextual

Cada parágrafo deve ser compreensível **isoladamente**, sem depender excessivamente de referências anteriores. É o mesmo princípio do chunking (3.7) aplicado parágrafo a parágrafo. Repita o sujeito em vez de usar "ele", "isso", "esse processo".

---

## 3.14 Eliminação de "fluff"

Remova introduções genéricas, frases de aquecimento e redundâncias que não agregam informação factual. Conteúdo enxuto e denso é mais extraível; "fluff" dilui os chunks e atrasa a resposta direta.

---

## Saída esperada desta camada

Entregue o conteúdo reescrito (ou diagnóstico página a página) com: answer-first aplicado, títulos convertidos em perguntas, TL;DR adicionado, indicação de onde faltam fontes/estatísticas/especialistas, dados comparativos convertidos em tabelas HTML, e o conteúdo reorganizado em chunks auto-contidos sem fluff.
