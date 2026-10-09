# Prompt — Mapa mental (BussolaMap)

> **Uso:** sempre que o usuário pedir um **mapa mental** sobre algum assunto, siga este prompt na íntegra. O conteúdo do mapa vem do material de estudo do tópico (resumo, texto-base, aulas) ou do que o usuário enviar.

---

Você é um especialista em criação de mapas mentais para estudo com memorização espaçada.

Gere um JSON válido no formato BussolaMap para o conteúdo que vou fornecer abaixo.

## FORMATO EXATO DO JSON

{
  "rootId": "<uuid-da-raiz>",
  "nodes": {
    "<uuid>": {
      "id": "<uuid>",
      "label": "Texto do nó",
      "x": 0,
      "y": 0,
      "color": "#6366f1",
      "comment": "Nota explicativa opcional",
      "depth": 0,
      "parentId": null,
      "children": ["<uuid-filho1>", "<uuid-filho2>"],
      "hideInReview": false,
      "question": ""
    }
  },
  "thresholds": {
    "revealThreshold": 10,
    "hideBadgeOnZero": true
  },
  "edges": []
}

## REGRAS OBRIGATÓRIAS

1. IDs: Use UUIDs v4 reais (formato: xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx). Cada nó deve ter um ID único.

2. Estrutura de árvore:
   - O nó raiz tem depth: 0 e parentId: null
   - Filhos diretos da raiz têm depth: 1 e parentId: "<id-da-raiz>"
   - Os campos "children" (no pai) e "parentId" (no filho) DEVEM ser consistentes entre si
   - Todo ID listado em "children" DEVE existir em "nodes"
   - Legibilidade: no máximo 7 filhos por nó e no máximo 4 níveis abaixo da raiz

3. Coordenadas: Defina x: 0 e y: 0 para todos os nós — o sistema recalcula o layout automaticamente.

4. Cores disponíveis (use para diferenciar categorias/ramos):
   - "#6366f1" (índigo) — padrão, use na raiz
   - "#3b82f6" (azul)
   - "#06b6d4" (ciano)
   - "#10b981" (verde)
   - "#f59e0b" (âmbar)
   - "#ef4444" (vermelho)
   - "#ec4899" (rosa)
   - "#8b5cf6" (violeta)
   - "#f97316" (laranja)
   - "#14b8a6" (teal)
   Cada ramo de nível 1 recebe uma cor diferente; todos os descendentes do ramo usam a mesma cor.

5. Campo "label":
   - Até 60 caracteres, em forma de tópico (sem frases longas)
   - Texto literal, exemplos, explicação e mnemônicos vão no "comment", nunca no "label"
   - Cada prazo, quórum, percentual, número ou item de lista fechada é um nó próprio, nunca diluído dentro de um rótulo maior

6. Campo "hideInReview":
   - false (ou omitir): nó visível por padrão no modo revisão quando o pai estiver revelado
   - true: nó fica oculto (ghost) e precisa ser adivinhado/revelado (use para conceitos e detalhes que quer testar)

7. Campo "question":
   - OBRIGATÓRIO em todo nó com hideInReview: true; nos demais, deixe ""
   - Texto exibido acima do nó oculto no modo revisão (funciona como pista de flashcard)
   - Formule como pergunta: "O que é...?", "Quais são os...?", "Qual o prazo para...?"
   - A pergunta NÃO pode conter as palavras do "label" que a respondem (não vazar a resposta)

8. Campo "comment" (opcional):
   - Nota extra: definição completa, texto literal da fonte (com artigo/página), exemplo, mnemônico ou contexto adicional
   - Aparece no painel de edição ao selecionar o nó

9. Ordem e coerência:
   - A ordem do array "children" é a ordem de leitura: siga a ordem da fonte (artigos, etapas de um processo, sequência cronológica)
   - Os filhos de um mesmo nó devem ser da mesma natureza (todos "requisitos", todos "etapas", todos "hipóteses"); não misture tipos diferentes no mesmo nível

## ESTRATÉGIA PARA O MAPA

- Nível 0 (raiz): Tema principal do conteúdo
- Nível 1 (filhos da raiz): Grandes categorias ou módulos — ficam visíveis por padrão
- Nível 2: Subcategorias ou tópicos importantes — use hideInReview: true com question relevante
- Nível 3+: Detalhes, exemplos, definições — sempre com question bem formulada
- Quando couber, inclua dois ramos padrão no nível 1:
  - "Pegadinhas": afirmações erradas comuns em prova, com a correção no "comment"
  - "Comparações": institutos parecidos lado a lado (ex.: comissão externa × CPI; adiamento × encerramento)

Tamanho proporcional ao conteúdo: um nó por ideia relevante. Não crie nós para atingir uma quantidade; se o conteúdo for pequeno (um artigo, um conceito), o mapa é pequeno. Como referência, um capítulo ou tópico completo costuma render 25 a 40 nós, com pelo menos 3 níveis.

## CONTEÚDO A TRANSFORMAR EM MAPA MENTAL

[COLE AQUI O CONTEÚDO QUE VOCÊ QUER APRENDER]

## RESPOSTA ESPERADA

Retorne APENAS o JSON válido, dentro de um único bloco de código, sem explicações nem texto extra antes ou depois.
O JSON deve estar pronto para importar diretamente no BussolaMap.
