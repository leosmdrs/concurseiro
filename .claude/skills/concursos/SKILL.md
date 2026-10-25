---
name: concursos
description: Estudo para concursos (banca CEBRASPE) — Contabilidade Pública, Auditoria Governamental e Controle, Finanças Públicas, Avaliação de Políticas Públicas, Reconhecimento de Fala/Transcrição/IA e Linguística (inclui degravação, comunicações oficiais e técnica legislativa), Regimento Interno da Câmara e Regimento Comum do Congresso, Direito Constitucional (processo legislativo). Use sempre que o usuário disser "concursos", "Câmara" ou "CGU", pedir para estudar um tópico dessas disciplinas, enviar conteúdo-base ou questões anteriores.
---

# Concursos — estudo direcionado (CEBRASPE)

Todo o material vive na raiz do repositório, uma pasta por disciplina. Leia `README.md` primeiro (disciplinas, convenções, cruzamentos e alertas de atualização normativa).

## Fluxo

1. **Identificar o tópico.** Se o usuário não disse qual, mostre a tabela de tópicos da disciplina (`<disciplina>/README.md`) destacando os de prioridade Alta ainda ⬜ e pergunte.
2. **Ler a ficha** `README.md` da pasta do tópico (edital literal, fontes, como a banca cobra, alertas).
3. **Trabalhar o material.** Conteúdo-base enviado pelo usuário vai para `material/` da pasta. Use a norma/manual na versão exigida pelo edital; quando a versão vigente divergir, sinalize a diferença em vez de trocar uma pela outra. Para temas técnicos (ASR, APIs), sinalize o que depende de versão ou data.
4. **Produzir/atualizar `resumo.md`**: direcionado ao que a CEBRASPE cobra — literalidade dos dispositivos-chave, listas e números (prazos, percentuais, rol de competências), comparações entre conceitos parecidos, exemplos aplicados ao cargo e um bloco final "Pegadinhas".
5. **Produzir/atualizar `questoes.md`**:
   - questões anteriores enviadas pelo usuário: enunciado, gabarito e comentário com o dispositivo que fundamenta;
   - itens C/E inéditos no estilo CEBRASPE (mudança de uma palavra, generalização indevida, troca de conceitos; em Linguística, reescritas "mantém-se a correção e o sentido"), com gabarito e justificativa separados do enunciado.
6. **Atualizar status** na ficha do tópico e na tabela da disciplina (⬜ → 🟨 → ✅ → 🔁).
7. **Commitar e fazer push** ao final de cada sessão de estudo.

## Regras

- **Material-base por disciplina:** se existir `<disciplina>/material/README.md`, ele indica quais aulas/PDFs cobrem cada tópico. Ao montar material de estudo, use essas aulas como **base** (consulte o `.txt` extraído) e complemente com pesquisa (WebSearch, obras de referência, provas CEBRASPE) para dar qualidade ao estudo — o usuário autorizou essas pesquisas. Cite de qual aula/página veio cada ponto central e sinalize quando a aula divergir da doutrina ou não cobrir o subtópico.

- **Discursiva × só objetiva:** quando o edital separa parte básica (só objetiva) e específica (objetiva + discursiva), cada ficha traz o campo **Discursiva** (✍️ pode cair / 🚫 não cai). Ao preparar material ou treino de discursiva, use apenas tópicos ✍️.
- **Quantidade de itens proporcional ao conteúdo:** gere itens C/E em número razoável para o trecho estudado — em regra 1 a 2 itens por dispositivo relevante (caput, parágrafo ou inciso com regra própria). Ex.: um artigo com caput e parágrafo único → ~6 itens; um capítulo de 15 artigos → ~30–40. Não encha com itens de outros artigos; cruzamentos entram só quando essenciais e, se for o caso, no resumo.
- **Mapa mental:** quando o usuário pedir mapa mental, siga `_prompts/mapa-mental-bussolamap.md` à risca. Gere os UUIDs v4 e monte o JSON com script (Python `uuid4` + `json.dumps`), valide a consistência `children`/`parentId`/`depth` antes de entregar, salve como `mapa-mental.json` na pasta do tópico e entregue no chat só o JSON (em bloco de código, para copiar).
- **Apostila em PDF:** quando o usuário pedir apostila/PDF de estudo de um tópico, siga `.claude/skills/concursos/apostila-pdf/README.md` (padrão aprovado: `base.css` + `render.js`, conteúdo baseado nas questões reais da banca, anexo na guia Draw via `url` do GitHub).
- **Importar questões de PDF (TEC Concursos) para a Bússola:** extraia com `pdftotext -layout`, deduplique pelo id da questão (`tecconcursos.com.br/questoes/<id>`) e **junte as linhas de cada parágrafo** antes de importar (o app mostra cada quebra do PDF como linha separada; preserve versos de poema). Transcreva textos que vêm como imagem. Comente cada item justificando o gabarito oficial e classifique pelo que o item cobra. `listar_questoes` corta em ~45 questões por tópico, sem paginação; para editar em massa depois, mova as já tratadas temporariamente para o tópico pai e devolva no fim.
- Prioridade = incidência CEBRASPE × pertinência para o cargo. Sempre direcione o estudo para o que mais cai.
- Priorize o que cruza disciplinas (retextualização ↔ degravação; formatação parlamentar ↔ redação oficial e técnica legislativa).
- Nunca invente redação de lei: quando citar artigo literal sem a fonte em mãos, diga que é de memória e marque para conferência.
- Novas disciplinas entram como `NN-disciplina/` (próximo número livre), com tópicos `NN-topico/` e subtópicos `N.N-nome/`, cada um com `README.md`; registre a disciplina na tabela de `README.md` (raiz).

## Supabase (banco de estudos)

- Só acesse quando o usuário pedir. Produção é o projeto do `.mcp.json` (servidor configurado como read-only).
- Prefira consultas de leitura (`list_tables`, `execute_sql` com SELECT). Qualquer escrita em produção exige confirmação explícita do usuário, mostrando antes o SQL que será executado.
