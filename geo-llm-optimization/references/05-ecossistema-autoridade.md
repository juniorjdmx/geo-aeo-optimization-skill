# Camada 5 — Autoridade, Entidade e Ecossistema Externo

Motores generativos sintetizam respostas a partir de **múltiplas fontes**, não só do site da marca. Estar presente e bem-posicionado fora do próprio domínio é o que torna a marca uma referência citável. Esta camada é contínua.

## Checklist

- [ ] Presença em comunidades (Reddit, Quora)
- [ ] Otimização para YouTube (transcrições e timestamps)
- [ ] Digital PR para earned media
- [ ] Consistência de entidade entre canais
- [ ] Listagens em diretórios setoriais
- [ ] Claim do Google Knowledge Graph

---

## 5.1 Presença em comunidades (Reddit/Quora)

IAs como Perplexity e o Google AI Overview priorizam **discussões validadas por humanos**. Reddit e Quora aparecem com frequência como fontes citadas.

- **Presença genuína e útil.** Responda perguntas reais na sua área. Spam e autopromoção são contraproducentes — a IA capta o sinal negativo.
- Responda às perguntas que são **Golden Prompts** (Camada 4.3) quando elas existem nessas plataformas.
- Consistência de identidade com os outros canais (reforça a entidade — ver 5.4).
- Respostas densas, com dados e passos concretos, têm mais chance de extração.
- Respeite as regras de cada comunidade — banimento elimina a fonte.

---

## 5.2 Otimização para YouTube

Vídeos são fontes primárias de autoridade para várias IAs, mas o modelo lê o **texto**, não assiste.

- **Transcrição completa**, revisada (não só a legenda automática). Publique também na descrição ou numa página do site.
- **Timestamps / capítulos** na descrição — transformam o vídeo em chunks navegáveis.
- Título e descrição em linguagem de pergunta (Camada 3.2).
- Descrição rica, com os pontos-chave e dados citados escritos por extenso.
- `VideoObject` no schema da página que hospeda o vídeo (Camada 2.10).

```
00:00 Pergunta de abertura
01:30 Segundo tópico em forma de pergunta
04:15 Terceiro tópico
```

---

## 5.3 Digital PR para earned media

No GEO, menções em sites de terceiros (earned media) pesam **mais** que conteúdo da própria marca (owned media). A IA confia mais em quem fala da marca do que na marca falando de si.

- Foque em ser **mencionado** em veículos, blogs setoriais, podcasts e newsletters com reputação — mesmo sem backlink tradicional, a menção é um vetor de confiança.
- Sites de alta confiança valem mais que muitos sites fracos.
- Contexto positivo e factual (conecta com análise de sentimento — Camada 6.2).
- Táticas: artigos de autoria, dados proprietários que veículos queiram citar, participação em pautas, presença em "listas de melhores", podcasts e entrevistas.

---

## 5.4 Consistência de entidade

A IA reconcilia a marca como **uma entidade** cruzando informações de várias fontes. Divergências confundem o grafo de conhecimento e enfraquecem a entidade.

Garanta que estejam **idênticos** em todos os lugares: nome da empresa, descrição, endereço, telefone, fundação, liderança. Cheque especialmente:
- LinkedIn
- Crunchbase
- Wikidata (e Wikipedia, se houver)
- Google Business Profile
- O `Organization` schema do site (Camada 2.1)

Uma mesma informação contraditória entre dois canais é suficiente para a IA hesitar.

---

## 5.5 Listagens em diretórios setoriais

Perfis ativos e atualizados em diretórios e plataformas de review do setor reforçam a entidade e fornecem fontes que a IA consulta.

- Para SaaS/software: **G2**, **Capterra**.
- Reviews gerais: **Trustpilot**.
- Diretórios específicos do nicho do cliente.
- Mantenha os perfis completos, com NAP consistente (Camada 5.4) e informações atualizadas.

---

## 5.6 Claim do Google Knowledge Graph

O painel de conhecimento do Google (Knowledge Panel) é uma fonte estruturada que alimenta AI Overviews e outras IAs.

- Verifique se a marca/pessoa tem um painel de conhecimento.
- Faça o **claim** do painel (Google permite reivindicar a entidade).
- Mantenha a precisão das informações exibidas.
- Conecte com `sameAs` e Wikidata (Camada 2.1) — esses sinais ajudam o Google a construir e confiar no painel.

---

## Saída esperada desta camada

Como é uma camada contínua, entregue um **plano de presença de ecossistema**: vídeos a otimizar/criar; comunidades e Golden Prompts a monitorar; plano de PR digital; uma auditoria de consistência de entidade entre os canais (apontando divergências); diretórios a cadastrar/atualizar; status do Knowledge Panel. Inclua a cadência recomendada para cada frente.
