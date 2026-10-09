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

3. Coordenadas: Defina x: 0 e y: 0 para todos os nós — o sistema recalcula o layout automaticamente.

4. Cores disponíveis (use para diferenciar categorias/ramos):
   - "#6366f1" (índigo) — padrão
   - "#3b82f6" (azul)
   - "#06b6d4" (ciano)
   - "#10b981" (verde)
   - "#f59e0b" (âmbar)
   - "#ef4444" (vermelho)
   - "#ec4899" (rosa)
   - "#8b5cf6" (violeta)
   - "#f97316" (laranja)
   - "#14b8a6" (teal)
   Use a mesma cor para todos os nós de um mesmo ramo.

5. Campo "hideInReview":
   - false (ou omitir): nó visível por padrão no modo revisão quando o pai estiver revelado
   - true: nó fica oculto (ghost) e precisa ser adivinhado/revelado (use para conceitos e detalhes que quer testar)

6. Campo "question" (opcional):
   - Texto exibido acima do nó oculto no modo revisão (funciona como pista de flashcard)
   - Use para guiar a memória: "O que é...?", "Quais são os...?", "Como funciona...?"
   - Deixe "" ou omita se não for necessário

7. Campo "comment" (opcional):
   - Nota extra: definição completa, exemplo, mnemônico ou contexto adicional
   - Aparece no painel de edição ao selecionar o nó

## ESTRATÉGIA PARA O MAPA

- Nível 0 (raiz): Tema principal do conteúdo
- Nível 1 (filhos da raiz): Grandes categorias ou módulos — ficam visíveis por padrão
- Nível 2: Subcategorias ou tópicos importantes — use hideInReview: true com question relevante
- Nível 3+: Detalhes, exemplos, definições — sempre com question bem formulada

Crie um mapa rico, com pelo menos 3 níveis de profundidade e pelo menos 25-40 nós no total.
Quanto mais detalhado e bem estruturado, mais útil será para o estudo.

## CONTEÚDO A TRANSFORMAR EM MAPA MENTAL

[COLE AQUI O CONTEÚDO QUE VOCÊ QUER APRENDER]

## RESPOSTA ESPERADA

Retorne APENAS o JSON válido, sem explicações, sem markdown, sem texto extra antes ou depois.
O JSON deve estar pronto para importar diretamente no BussolaMap.
