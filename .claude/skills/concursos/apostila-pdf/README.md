# Apostila em PDF direcionada à banca (padrão aprovado)

Use quando o usuário pedir "apostila", "PDF de estudo" ou "material em PDF" de um tópico, sobretudo a partir de cadernos de questões (TEC Concursos etc.). Primeiro uso: apostilas de Sintaxe (`10-lingua-portuguesa/01-sintaxe/material/`).

## Arquivos deste kit

| Arquivo | Papel |
|---|---|
| `base.css` | Visual completo: capa, caixas coloridas, tabelas, fluxos, análise sintática colorida, questões, checklist. **Não altere por apostila**; escreva só o corpo HTML usando as classes dele. |
| `render.js` | HTML do corpo + `base.css` → PDF A4 (Chromium/Playwright), com rodapé e número de página. |
| `otf2ttf.py` | Converte a Inter (OTF) para TTF. Rode uma vez por ambiente antes de renderizar. |

## Preparar o ambiente (uma vez por sessão)

```bash
pip install --quiet fonttools
mkdir -p ~/.fonts
python3 -I .claude/skills/concursos/apostila-pdf/otf2ttf.py Inter-Regular Inter-Italic Inter-Medium Inter-SemiBold Inter-SemiBoldItalic Inter-Bold Inter-BoldItalic Inter-ExtraBold InterDisplay-Bold InterDisplay-SemiBold InterDisplay-ExtraBold
fc-cache -f ~/.fonts
```

O `base.css` carrega as fontes de `file:///root/.fonts/InterTT-*.ttf`, nas famílias `IT` (texto) e `ITD` (títulos). Sem essa conversão o PDF dobra de tamanho, porque a fonte entra como Type 3.

## Montar o conteúdo

1. **Base = as questões reais.** Levante, por tópico: nº de questões, % Certo/Errado, faixa de anos e órgãos mais frequentes. Classifique cada item por subtema para obter a frequência do "Raio-X". Não invente dados; exemplos fora das questões vão marcados como "didáticos".
2. **Estrutura** (≈12–16 páginas A4):
   1. Capa: `<section class="cover">` com `.kicker`, `h1`, `.sub`, `.stats > .stat` (`<b>116</b> questões analisadas`) e `.foot`.
   2. Sumário (`<ol class="toc">`).
   3. Raio-X da banca: tabela subtema × qtd × C/E, formatos típicos de item e "leitura estratégica" (ex.: "item que afirma sujeito indeterminado → 46 de 52 foram ERRADOS").
   4. Teoria enxuta, sempre com exemplos das questões, usando tabelas comparativas, `.flow` (fluxo de decisão "Como identificar…"), `.grid2/.grid3` com `.card` e análise colorida `.ana`.
   5. Pegadinhas recorrentes: `.box.pegadinha`, cada uma com questão real.
   6. 10–14 questões comentadas, `.q` (C e E equilibrados).
   7. Checklist de 1 página, "Na hora da prova" (`.checklist`).
3. **Classes principais**:
   - caixas: `<div class="box conceito|dica|pegadinha|esquema|atencao"><span class="bt">Título</span>…</div>`;
   - análise: `<p class="ana"><span class="s" data-f="SUJEITO">…</span> <span class="v" data-f="VERBO">…</span> <span class="c" data-f="OD">…</span> <span class="a" data-f="ADJ. ADV.">…</span> <span class="o" data-f="OR. SUB.">…</span></p>`. Use rótulos curtos e espace termos curtos, para os rótulos não se sobreporem;
   - questão: `<div class="q"><div class="meta">CEBRASPE · Órgão · Ano · Q123</div><div class="item">…</div><span class="gab C">CERTO</span><span class="why">…</span></div>`;
   - destaques: `<mark>`, `.t1`–`.t5`, `.pb` (quebra de página; evite forçar, deixa páginas meio vazias);
   - dentro de `.flow .node` o `<b>` vira título em bloco; para negrito no meio do texto use `<strong>`.
4. Com vários tópicos, paralelize: um agente por apostila, todos com o mesmo `base.css`.

## Renderizar e revisar

```bash
RODAPE='Sintaxe · CEBRASPE — material direcionado' node .claude/skills/concursos/apostila-pdf/render.js <pasta-saida> <topico>.html
pdffonts <pasta-saida>/<topico>.pdf | grep -c "Type 3"   # tem de dar 0
pdftocairo -png -r 50 -f 1 -l 4 <pasta-saida>/<topico>.pdf prev   # revise as páginas com Read
```

O resultado esperado é de 200–270 KB para 13–18 páginas. Revise capa, quebras, tabelas cortadas e rótulos `data-f`.

## Entregar na Bússola (guia Draw do tópico)

1. Salve o PDF no repositório, em `<disciplina>/<topico>/material/apostila-<nome>.pdf`, e faça commit e push na branch de trabalho.
2. `anexar_pdf` com `url` = `https://raw.githubusercontent.com/leosmdrs/concurseiro/<branch>/<caminho>.pdf`, `topico_id` do tópico e `nome_arquivo` "Apostila CEBRASPE - <Tópico>.pdf".
   - **O repositório precisa estar público no momento do anexo**: o conector não baixa de repositório privado ("Não consegui baixar o PDF dessa url"). Se estiver privado, peça ao usuário para torná-lo público (Settings → Danger Zone → Change visibility). Depois de anexar, ele pode voltar a privado, porque o Draw guarda a cópia.
   - Não tente `conteudo_base64` com PDFs desse tamanho: ~300 mil caracteres não cabem numa chamada.
3. Confira com `listar_anexos` (páginas e KB).
