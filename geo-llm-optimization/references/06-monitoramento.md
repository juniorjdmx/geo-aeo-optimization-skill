# Camada 6 — Monitoramento, Métricas e Manutenção

SEO clássico mede posição e cliques. GEO exige métricas novas: a marca aparece (ou não) **dentro de uma resposta sintetizada**. Esta camada é o ciclo de feedback que valida todo o resto e mantém o conteúdo vivo.

## Checklist

- [ ] Medir o Share of Model (SoM)
- [ ] Monitorar o sentimento da IA sobre a marca
- [ ] Capturar tráfego de referência de IA no GA4
- [ ] Auditoria mensal de citações
- [ ] Rastrear o citation rate
- [ ] Analisar o ROI do tráfego de referência de IA
- [ ] Atualização recorrente (freshness, a cada 90 dias)
- [ ] Garantir integridade factual do site
- [ ] Otimização multimodal (alt-text e metadados)
- [ ] Preparação para comércio agêntico

A base de medição é o conjunto de **Golden Prompts** definido na Camada 4.3.

---

## 6.1 Share of Model (SoM)

Mede em que **porcentagem das respostas de IA a marca é citada**, comparada aos concorrentes, para os Golden Prompts.

Como medir:
1. Rode cada Golden Prompt em cada IA alvo (ChatGPT, Perplexity, Gemini, AI Overviews, Claude). Rode cada um várias vezes (ex: 3-5) e agregue.
2. Para cada resposta, registre se a marca e os concorrentes foram mencionados.
3. **SoM** = respostas que citam a marca / total de respostas.
4. Compare com o SoM dos concorrentes.

Acompanhe o SoM ao longo do tempo, por motor e por prompt. Prompts onde a marca está ausente viram prioridade de conteúdo (Camada 4).

---

## 6.2 Sentimento da IA

Não basta ser citado — importa **como**. A IA pode posicionar a marca de forma positiva, neutra ou negativa. Sentimentos negativos recorrentes ativam uma **lógica de exclusão**: o modelo passa a evitar recomendar a marca.

- Para cada resposta em que a marca aparece, classifique o sentimento e registre o motivo quando negativo.
- Acompanhe a tendência.
- Diante de sentimento negativo recorrente, investigue a origem (reviews, fóruns, notícias), aja na causa real e na narrativa (Camada 5).

---

## 6.3 Tráfego de referência de IA no GA4

Configure o **Google Analytics 4** para isolar visitas vindas de IAs.

- Crie um segmento/canal para domínios de referência como `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`.
- Acompanhe volume, páginas de entrada e comportamento desse tráfego separadamente.
- Sem isso, o tráfego de IA fica diluído em "referral" ou "direct" e o resultado do GEO fica invisível.

---

## 6.4 Auditoria mensal de citações

Mensalmente, teste manualmente os prompts estratégicos (Golden Prompts) e documente:
- A marca apareceu? Em que posição da resposta?
- Em que contexto foi mencionada?
- Quais fontes a IA citou (o site da marca? terceiros? concorrentes?).

Mantenha um histórico para ver evolução e impacto das otimizações.

---

## 6.5 Citation rate

Mede a **porcentagem de consultas-alvo em que o domínio aparece com um link clicável** na resposta da IA. Diferente do SoM (que conta menção da marca), o citation rate conta a **citação com link** do domínio. Acompanhe por motor e ao longo do tempo.

---

## 6.6 ROI do tráfego de referência de IA

O tráfego vindo de IA tende a ter intenção mais alta — o usuário já recebeu uma recomendação. A taxa de conversão pode ser várias vezes maior que a do orgânico tradicional (algumas análises de mercado apontam algo em torno de 4,4x; cite o número só se houver fonte verificável).

- Compare a taxa de conversão do tráfego de IA com a do orgânico tradicional, usando os segmentos do GA4 (6.3).
- Use esse dado para justificar investimento contínuo em GEO.

---

## 6.7 Freshness — atualização recorrente

Modelos generativos têm **forte viés de recência**. Conteúdo desatualizado perde espaço. Rotina a cada **90 dias**:

- Atualize estatísticas e dados para os valores mais recentes (com fonte — Camada 3).
- Atualize a data visível de "última atualização" e o `dateModified` do schema (Camada 2.6).
- Revise referências e links quebrados.
- Atualize o `llms.txt` e o `sitemap.xml` se a estrutura mudou.
- Reflita mudanças de produto, preço ou posicionamento.

---

## 6.8 Integridade factual do site

A IA "alucina" sobre a marca quando encontra informações **contraditórias ou imprecisas** no próprio site.

- Corrija divergências de preço, serviços, planos e liderança entre páginas.
- Garanta uma única "fonte da verdade" para cada dado.
- Conecta com a consistência de entidade (Camada 5.4): a coerência precisa valer dentro do site e entre canais.

---

## 6.9 Otimização multimodal

Imagens e vídeos também podem servir de fonte para a IA — se tiverem metadados ricos.

- **Alt-text descritivo e factual** em todas as imagens (não "imagem1.jpg").
- Nomes de arquivo semânticos.
- Legendas que repitam em texto qualquer dado mostrado na imagem (ver Camada 3.4).
- Para vídeos, transcrições e `VideoObject` (Camada 5.2).

---

## 6.10 Preparação para comércio agêntico

Agentes de IA começam a realizar compras e reservas de forma autônoma. Para participar disso:

- Estruture **feeds de produto** completos e atualizados (preço, disponibilidade, SKU).
- Aplique `Product` schema com dados comerciais precisos (Camada 2.4).
- Garanta que preço e estoque no site, no schema e no feed sejam idênticos.
- Mantenha o processo de compra/reserva acessível e sem dependência de interação que um agente não conseguiria executar.

---

## Saída esperada desta camada

Entregue: a lista de Golden Prompts; um método/planilha para medir SoM, sentimento e citation rate de forma repetível; uma linha de base atual comparada aos concorrentes; a configuração de segmentos de IA no GA4; um calendário de freshness (rotina de 90 dias); uma auditoria de integridade factual; e a recomendação de re-medir após cada rodada de otimização para fechar o ciclo.
