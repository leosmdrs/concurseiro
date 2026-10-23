# 🎯 Concursos — estudo direcionado (banca CEBRASPE)

Todas as disciplinas ficam aqui. Cada **disciplina** é uma pasta, e cada **tópico ou subtópico do edital** é uma subpasta com um `README.md` (ficha do tópico).

## Disciplinas

| # | Disciplina | Edital de origem | Pasta |
|---|---|---|---|
| 1 | Contabilidade Aplicada ao Setor Público | CGU | [01-contabilidade-publica](./01-contabilidade-publica/) |
| 2 | Auditoria Governamental e Controle Interno | CGU | [02-auditoria-governamental-e-controle](./02-auditoria-governamental-e-controle/) |
| 3 | Finanças Públicas | CGU | [03-financas-publicas](./03-financas-publicas/) |
| 4 | Avaliação de Políticas Públicas | CGU | [04-avaliacao-de-politicas-publicas](./04-avaliacao-de-politicas-publicas/) |
| 5 | Reconhecimento de Fala, Transcrição e Inteligência Artificial | Câmara dos Deputados (Registro e Redação) | [05-reconhecimento-de-fala-transcricao-e-ia](./05-reconhecimento-de-fala-transcricao-e-ia/) · [📋 plano](./05-reconhecimento-de-fala-transcricao-e-ia/PLANO.md) |
| 6 | Linguística | Câmara dos Deputados (Registro e Redação) | [06-linguistica](./06-linguistica/) |
| 7 | Regimento Interno da Câmara (RICD) e Regimento Comum do Congresso (RCCN) — ✍️ parte específica / 🚫 parte básica | Câmara dos Deputados (Registro e Redação) | [07-regimento-interno-cd-e-regimento-comum](./07-regimento-interno-cd-e-regimento-comum/) |
| 8 | Direito Constitucional | Câmara dos Deputados (Registro e Redação) | [08-direito-constitucional](./08-direito-constitucional/) |
| 9 | Direito Administrativo | — | [09-direito-administrativo](./09-direito-administrativo/) |

📝 **Prova discursiva da Câmara (Registro e Redação):** [critérios de avaliação e fórmulas](./prova-discursiva-camara-registro-e-redacao.md)

> A coluna "Edital de origem" indica de qual edital veio a lista de tópicos (texto literal na ficha de cada tópico). O material serve para qualquer concurso que cobre o assunto.

> **Sem duplicidade:** cada assunto aparece uma só vez, na disciplina mais pertinente.
> - **LRF** → `03-financas-publicas/15-lrf-topicos-selecionados/` (subtópicos 15.01–15.10).
> - **Sistema de Controle Interno** → `02-auditoria-governamental-e-controle/01-sci-poder-executivo-federal/`.
> - **Estágios, classificações e restos a pagar** → Finanças (10 e 11); Contabilidade (04) cobre só os lançamentos contábeis.
> - "Estrutura e competência da CGU / Sistemas estruturantes" está em Auditoria (`08` e `09`).

## Convenção de cada pasta de tópico

```
NN-nome-do-topico/
├── README.md     # ficha: edital literal, fontes, prioridade, como a CEBRASPE cobra, alertas, status
├── resumo.md     # resumo direcionado (criado quando o tópico for estudado)
├── questoes.md   # questões anteriores comentadas + itens C/E inéditos
└── material/     # conteúdo-base enviado (lei, PDF, aula, slides, documentação)
```

**Status:** ⬜ não iniciado · 🟨 em estudo · ✅ estudado · 🔁 em revisão

## Prioridade

Combina **incidência em provas CEBRASPE** com **pertinência para o cargo**. Os tópicos de **Alta** devem ser estudados primeiro e revisados mais vezes.

- **Disciplinas 1–4:** controle interno, auditoria, correição, transparência.
- **Disciplinas 5–6:** registro, degravação e redação de sessões parlamentares. Prioridade máxima para o que se cruza entre as duas:
  - **retextualização fala → escrita** (Linguística 6.2 e 7.2) ↔ **degravação e revisão** (Fala/IA 2.x);
  - **formatação parlamentar** (Fala/IA 2.4) ↔ **comunicações oficiais** (Linguística 11) e **técnica legislativa** (Linguística 13);
  - **vocabulário parlamentar** (Fala/IA 1.6 e 2.8) ↔ **oratória parlamentar** (Linguística 5.3).

## Como a CEBRASPE cobra (diretrizes gerais)

- Itens **Certo/Errado**, com penalização: um errado anula um certo, então só marque com segurança.
- **Literalidade** de lei, decreto, IN e manual: a troca de uma palavra ("deverá" × "poderá", "controle" × "propriedade", "dois" × "três exercícios") torna o item errado.
- Generalizações ("sempre", "exclusivamente", "em nenhuma hipótese") costumam ser erradas, mas não é regra absoluta.
- Situações hipotéticas com aplicação de norma (ex.: ente que extrapola limite de pessoal na LRF).
- Mistura de fontes e termos parecidos: IN SFC 3/2017 × IPPF; três linhas de defesa × modelo de três linhas 2020; Lei 4.320 × MCASP; diarização × identificação de locutor; WER × DER; hiperônimo × hipônimo; pressuposto × subentendido.
- Em interpretação de texto: reescritas em que **"mantém-se a correção gramatical e o sentido"**.

## ⚠️ Pontos de atualização

Estudar pela versão pedida no edital, mas saber o que mudou:

- MCASP 9ª ed. → já existem edições posteriores.
- NBC T 16.11 → substituída pela NBC TSP 34 (Custos no Setor Público).
- IPPF/IIA → substituído pelas Normas Globais de Auditoria Interna (2024).
- Lei 13.844/2019 → revogada pela Lei 14.600/2023; Decreto 9.681/2019 → substituído por estrutura regimental posterior.
- IN SFC 3/2017 → data oficial normalmente citada como 9 de **junho** de 2017 (o edital da CGU diz julho).
- **Ferramentas e APIs de ASR** (Whisper, Google, Azure, AWS) mudam rápido: conferir a documentação vigente perto da prova.
- **Comunicações oficiais:** se o edital ou a Câmara indicarem manual próprio de redação ou de taquigrafia, ele prevalece sobre o Manual da Presidência.

## Fluxo de estudo

Ao pedir para estudar qualquer disciplina ou tópico daqui, o Claude carrega a skill [`.claude/skills/concursos`](../.claude/skills/concursos/SKILL.md) e segue o fluxo: escolher o tópico → ler a ficha → trabalhar o material enviado → gerar `resumo.md` e `questoes.md` → atualizar status.
