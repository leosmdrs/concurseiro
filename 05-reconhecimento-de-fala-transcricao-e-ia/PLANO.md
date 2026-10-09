# Plano de estudo — Reconhecimento de Fala, Transcrição e IA (Câmara · Registro e Redação · CEBRASPE)

## 1. Diagnóstico

- **Matéria nova:** há pouquíssimas questões CEBRASPE sobre ASR, diarização ou degravação. Não dá para estudar "pelo histórico".
- **Como a CEBRASPE cobra tema novo de tecnologia:** costuma pegar frases de **documentação oficial, artigos de referência e manuais** e mudar um detalhe. Também testa **definições**, **comparações entre conceitos vizinhos** e **generalizações** ("sempre", "elimina", "dispensa").
- **Parte da matéria tem muitas questões análogas:** **LGPD, segurança da informação e IA/PLN** (aprendizado de máquina, embeddings, LLM, RAG) aparecem em centenas de provas CEBRASPE. É aí que está o maior retorno por hora.
- **O núcleo do cargo** (degravação, revisão, formatação parlamentar) se resolve com **conceito + prática + padrão da Câmara**. Bom senso treinado vale mais do que decoreba.

**Estratégia em uma frase:** dominar com segurança o núcleo conceitual (nível A), treinar com questões análogas onde elas existem, criar um banco próprio de itens C/E onde não existem e calibrar o bom senso com duas práticas curtas com áudio real da Câmara.

## 2. Prioridades (níveis)

| Nível | Meta | Subtópicos | Tempo |
|---|---|---|---|
| **A — garantir** | Acertar praticamente tudo | 1.1 ASR · 1.2 end-to-end · 1.4 diarização · 1.6 PT-BR · 1.8 ferramentas · 2.1 transcrição × degravação × revisão · 2.2 human in the loop · 2.3 revisão e fidelidade · 2.4 formatação parlamentar · 4.1 LGPD · 4.3 segurança | ~55% |
| **B — essencial** | Dominar conceito e comparações | 1.3 LLMs de áudio · 1.7 tempo real · 2.5 normalização · 2.7 controle de qualidade · 2.8 adaptação de vocabulário · 3.2 busca semântica · 3.3 atas e resumos · 4.2 direitos autorais e ética | ~35% |
| **C — noção** | Reconhecer termos e evitar armadilhas | 1.5 pontuação e capitalização · 2.6 ferramentas CAT · 3.1 aplicações em parlamentos · 3.4 modelos em português | ~10% |

## 3. Cronograma (6 semanas + manutenção)

> **Premissa:** cerca de 6 h por semana, em 4 sessões de 1h30. Se a data da prova ou sua disponibilidade forem outras, me diga que eu reajusto.
> **Trilha paralela:** em toda semana, 1 sessão é de **questões CEBRASPE análogas** (LGPD, segurança, IA). É o que mantém o ritmo de C/E.

| Semana | Sessões 1–3 (conteúdo) | Sessão 4 (trilha paralela) | Entregáveis no repositório |
|---|---|---|---|
| **1** | 1.1 ASR (pipeline, modelo acústico e de linguagem, WER) · 1.2 end-to-end (CTC, RNN-T, atenção, Whisper) · montar o **glossário** | LGPD: princípios, definições, dado sensível | `glossario.md`, `resumo.md` de 1.1 e 1.2 |
| **2** | 1.4 diarização (DER, embeddings de locutor, sobreposição) · 1.7 tempo real · 1.3 LLMs de áudio · 1.5 pontuação | LGPD: bases legais, poder público, transferência internacional | resumos 1.3, 1.4, 1.5, 1.7 |
| **3** | 1.6 desafios em PT-BR · 1.8 **tabela comparativa** Whisper × Google × Azure × AWS · **Laboratório 1** (WER em áudio real) | Segurança da informação: CID, criptografia, controle de acesso | resumos 1.6 e 1.8, relatório do laboratório |
| **4** | 2.1 a 2.4: transcrição × degravação × revisão, HITL, critérios de fidelidade, padrão das notas taquigráficas · **Laboratório 2** (retextualização) | IA/PLN: aprendizado de máquina, alucinação, viés | resumos 2.1–2.4 |
| **5** | 2.5–2.8 (normalização, CAT, qualidade, adaptação) · 3.1–3.4 (RAG, busca semântica, sumarização) | Direitos autorais e ética em IA | resumos 2.5–2.8 e 3.x, resumo 4.2 |
| **6** | **Revisão ativa:** banco de itens C/E (meta de 150+), refazer os erros, revisar o glossário | Simulado misto: 40 itens | `questoes.md` de todos os subtópicos |
| **Depois** | 1 sessão por semana: 20–30 itens C/E + revisão espaçada no Omni (D+1, D+7, D+30) | — | — |

## 4. O que dominar em cada tópico (checklist objetivo)

> Marque ✅ quando conseguir **explicar sem consultar**. Cada item é uma afirmação que pode virar item C/E.
> ⚠️ Conteúdo técnico de memória. Confira detalhes de produto (nomes, limites, recursos) na documentação oficial perto da prova.

### Nível A

**1.1 ASR**
- [ ] Pipeline: captura → pré-processamento (detecção de voz/VAD, normalização) → extração de características (**espectrograma log-mel / MFCC**) → decodificação → pós-processamento.
- [ ] Arquitetura clássica: **modelo acústico** (HMM-GMM, depois híbrido DNN-HMM) + **léxico de pronúncia** + **modelo de linguagem** (n-gramas) + **decodificador** (Viterbi / *beam search*).
- [ ] **WER = (S + D + I) / N**: substituições, deleções e inserções sobre o nº de palavras da referência. **Pode passar de 100%** (por inserções). **CER** é o equivalente por caractere.
- [ ] Fontes de erro: ruído, fala sobreposta, sotaque, fala espontânea (hesitações), **palavras fora do vocabulário (OOV)**, qualidade de microfone e de compressão.

**1.2 Modelos end-to-end**
- [ ] Um **único modelo**, treinado de ponta a ponta, mapeia áudio direto em texto. Dispensa léxico de pronúncia e alinhamento explícito.
- [ ] **CTC** (token *blank*, saídas condicionalmente independentes) × **RNN-Transducer** (bom para **streaming**) × **encoder-decoder com atenção** (Transformer; o Whisper é desse tipo) × **Conformer** (convolução + Transformer).
- [ ] **Pré-treinamento autossupervisionado** (wav2vec 2.0, HuBERT): aprende com áudio sem rótulo e depois ajusta com poucos dados rotulados. É útil para idiomas com menos dados.
- [ ] Prós: pipeline simples, ótimo desempenho com muitos dados. Contras: precisa de muito dado e tem dificuldade com termos raros e de domínio, o que motiva a adaptação (2.8).

**1.4 Diarização**
- [ ] Responde "**quem falou quando**": segmentação → **embeddings de locutor** (i-vector, x-vector) → **clusterização** → rotulação anônima (Falante 1, 2…).
- [ ] **Diarização ≠ identificação de locutor** (dar nome à voz, exige cadastro prévio de voz) **≠ verificação** (confirmar se é quem diz ser) **≠ separação de fontes** (separar sinais misturados).
- [ ] **DER** = (falso alarme + fala perdida + confusão de locutor) / tempo total de fala.
- [ ] Desafios: **fala sobreposta** (apartes!), turnos curtos, número de falantes desconhecido. No plenário, **um canal por microfone** facilita muito.
- [ ] Ligação com LGPD: a voz usada para **identificar** pessoas é **dado biométrico** e, portanto, **sensível** (4.1).

**1.6 ASR em português brasileiro**
- [ ] Variação regional (cruza com Linguística 7.1), fala espontânea, redução e apagamento de sons (ex.: "falá"), ritmo.
- [ ] **Homófonos** decisivos no registro parlamentar: sessão/seção/cessão, conserto/concerto, cassar/caçar, censo/senso, acento/assento.
- [ ] Vocabulário parlamentar: nomes de parlamentares, siglas (PEC, PLP, MPV, PDL), jargão regimental ("questão de ordem", "pela ordem", "destaque", "requerimento de urgência"), números de proposições e citações de normas.
- [ ] Menos dados anotados que o inglês, por isso pesam a adaptação de domínio (2.8) e a revisão humana (2.2).

**1.8 Ferramentas e APIs** — monte a tabela comparativa com estas colunas: aberto/fechado, local/nuvem, *batch*/streaming, diarização, adaptação de vocabulário, idiomas.
- [ ] **Whisper (OpenAI):** modelo **aberto** (pesos publicados), encoder-decoder Transformer, treinado com **~680 mil horas** de áudio da web com **supervisão fraca**. É multilíngue, faz transcrição, **tradução para o inglês**, identificação de idioma e marcação de tempo. Processa em **janelas de 30 s** e pode rodar **localmente**. **Não faz diarização nativa** (combina-se com pyannote/WhisperX). Ponto fraco conhecido: **alucinações** (repetições, texto em trechos de silêncio).
- [ ] **Google Speech-to-Text:** reconhecimento síncrono, assíncrono (áudio longo) e **streaming**; diarização; **adaptação de modelo** (*phrase sets*, classes, *boost*); pontuação automática.
- [ ] **Azure AI Speech:** tempo real e transcrição em lote; **Custom Speech** (adaptação com seus dados); diarização; lista de frases; opção de **contêineres** (execução fora da nuvem).
- [ ] **AWS Transcribe:** lote e streaming; **vocabulário customizado** e **modelos de linguagem customizados**; diarização; identificação de canal; **ocultação automática de dados pessoais (PII)**.
- [ ] Diferença-chave para a prova: **aberto e local (Whisper) × serviço em nuvem**. Pesam privacidade e soberania de dados (4.1 e 4.3), custo, customização e escala.

**2.1 Transcrição automática × degravação × revisão humana**
- [ ] **Transcrição automática:** saída bruta do ASR.
- [ ] **Degravação:** passar o áudio para texto **fiel**, segundo padrões editoriais.
- [ ] **Revisão humana:** verificar a fidelidade, a norma e o padrão.
- [ ] Graus de edição: **literal (verbatim)**, que mantém hesitações e repetições × **verbatim limpo** × **texto editado/redigido**, adequado à norma culta **sem alterar o conteúdo nem a intenção do orador**.
- [ ] Ligação com Linguística 6.2 e 7.2: **retextualização fala → escrita** (Marcuschi): retirar marcas interacionais e hesitações, inserir pontuação e parágrafos, substituir, reordenar. Tudo isso **mantendo o sentido**.

**2.2 Human in the loop (HITL)**
- [ ] Fluxo: captação → ASR → (diarização, pontuação, normalização) → **revisão humana** → controle de qualidade → publicação → **as correções voltam para melhorar o modelo**.
- [ ] A **pontuação de confiança** do ASR indica onde o revisor deve olhar com mais atenção.
- [ ] **Viés de automação:** a tendência do revisor de aceitar erros **plausíveis** da máquina. Por isso, nomes, números e negações merecem atenção redobrada.
- [ ] A **responsabilidade final é humana**: a IA aumenta a produtividade, não substitui a revisão.

**2.3 Revisão: qualidade e fidelidade**
- [ ] Critérios: **fidelidade** ao discurso (conteúdo e intenção), correção gramatical, padronização, legibilidade, consistência terminológica.
- [ ] Erros típicos do ASR que o revisor precisa caçar: homófonos, **nomes próprios**, **números e valores**, **"não" omitido** (inverte o sentido!), alucinação em silêncio ou ruído, **troca de orador**, pontuação que muda o sentido.

**2.4 Formatação parlamentar**
- [ ] **Ação prática:** baixe 2 ou 3 **notas taquigráficas** de sessões no portal da Câmara e observe o padrão:
  - identificação do orador (tratamento, nome, partido e UF);
  - Presidência;
  - apartes;
  - marcações de manifestações, interrupções e trechos inaudíveis;
  - suspensões e reabertura.
- [ ] Procure normas ou manuais do **Detaq (Departamento de Taquigrafia, Revisão e Redação)** da Câmara. Se existirem publicamente, viram a **fonte primária** deste tópico.

**4.1 LGPD** (trilha paralela — muitas questões CEBRASPE)
- [ ] Art. 5º: dado pessoal, **dado sensível** (inclui **biométrico**), anonimização, controlador, operador, encarregado, tratamento.
- [ ] Art. 6º: **os 10 princípios** — finalidade, adequação, necessidade, livre acesso, qualidade dos dados, transparência, segurança, prevenção, não discriminação, responsabilização e prestação de contas.
- [ ] Bases legais (art. 7º) e para dados sensíveis (art. 11). **Tratamento pelo poder público** (arts. 23 a 32). **Transferência internacional** (art. 33, ligada ao uso de APIs em nuvem no exterior). Segurança (art. 46). Revisão de decisões automatizadas (art. 20).
- [ ] Interpretação a ter em mente: o áudio de **sessão pública** é dado pessoal tornado público, mas os **princípios continuam valendo**. A voz vira **biométrica e sensível** quando tratada **para identificar** a pessoa (impressão de voz).

**4.3 Segurança em pipelines de áudio e transcrição**
- [ ] **Confidencialidade, integridade e disponibilidade** (+ autenticidade). Criptografia **em trânsito** (TLS) e **em repouso**. **Menor privilégio** e controle de acesso por papel. **Trilhas de auditoria** (logs). Retenção e descarte.
- [ ] **Nuvem × local:** risco de vazamento de áudio de **reuniões reservadas**; contratos e localização dos dados.
- [ ] Ameaças específicas: **deepfake de voz**, ataques adversariais em áudio e **prompt injection** (o texto transcrito pode conter instruções que um LLM depois executa).

### Nível B

- [ ] **1.3 LLMs multimodais de áudio:** recebem áudio direto, sem ASR intermediário (ex.: GPT-4o, Gemini). **Vantagens:** menor latência; preservam entonação e emoção. **Riscos:** alucinação, menos controle de marcação de tempo e de literalidade, auditabilidade. Compare com a **cascata ASR → LLM**.
- [ ] **1.7 Tempo real:** *streaming* × lote. Resultados **parciais** × **finais**. *Endpointing* (detectar o fim da fala). O trade-off central é **latência × acurácia**. Uso típico: legendagem ao vivo (acessibilidade).
- [ ] **2.5 Normalização:** **ITN** (normalização inversa: "dois mil e vinte e quatro" → 2024), siglas, datas, valores, citação de normas (cruza com Linguística 11 e 13, LC 95).
- [ ] **2.7 Controle de qualidade:** revisão em dupla, **auditoria por amostragem**, métricas (WER após edição, taxa de **erros críticos**: nome, número, negação) e **SLA** (prazo e qualidade acordados).
- [ ] **2.8 Adaptação:** lista de frases e *boost*, vocabulário customizado, **modelo de linguagem customizado** (treinado com discursos anteriores), *fine-tuning* do modelo acústico. **Objetivo:** reduzir erros de OOV e de termos do domínio.
- [ ] **3.2 Busca semântica:** **embeddings** e **similaridade de cosseno** × busca lexical (palavra-chave/BM25). Busca **híbrida**. **RAG** (recupera trechos e o LLM responde citando-os): **reduz, mas não elimina** a alucinação.
- [ ] **3.3 Atas e resumos:** sumarização **extrativa** (copia trechos) × **abstrativa** (reescreve). **Ata** (registro resumido das deliberações) × **notas taquigráficas** (íntegra). A revisão humana é obrigatória.
- [ ] **4.2 Direitos autorais e ética:** pela Lei 9.610/1998, a proteção recai sobre "criações do espírito" e o autor é **pessoa física** (debate sobre conteúdo gerado por IA). Atos oficiais **não** são protegidos. Ética: transparência, supervisão humana, vieses, responsabilização. Verifique a situação do **PL 2.338/2023** (marco legal da IA). ⚠️ Artigos de memória: conferir.

### Nível C

- [ ] **1.5:** restauração de pontuação e de maiúsculas como pós-processamento (ou nativa no end-to-end). Afeta a legibilidade e o sentido.
- [ ] **2.6:** editores com áudio sincronizado ao texto (marcação de tempo), controle de velocidade, atalhos e pedal, glossário, destaque de trechos de baixa confiança.
- [ ] **3.1:** transcrição, sumarização, indexação, classificação de proposições. Na Câmara, conheça a iniciativa **Ulysses** (IA da Câmara).
- [ ] **3.4:** modelos multilíngues × especializados em português (ex.: BERTimbau, Sabiá). O trade-off é **desempenho × soberania de dados**.

## 5. Onde estudar (fontes enxutas)

| Para | Fonte | Uso |
|---|---|---|
| Base conceitual de ASR | Jurafsky & Martin, *Speech and Language Processing* (3ª ed., rascunho gratuito em web.stanford.edu/~jurafsky/slp3), capítulo de ASR | Ler as seções de arquitetura e de WER (não o capítulo todo) |
| Whisper | Radford et al. (2022), *Robust Speech Recognition via Large-Scale Weak Supervision* (arXiv 2212.04356): resumo, introdução e seção de abordagem | Muitas frases-chave que viram item C/E |
| Diarização | Documentação do pyannote.audio (github.com/pyannote/pyannote-audio) | Conceitos e DER |
| APIs | Páginas de visão geral: Google Cloud Speech-to-Text, Azure AI Speech, Amazon Transcribe | **Só as páginas de visão geral e de recursos**, para preencher a tabela comparativa |
| Degravação e retextualização | Marcuschi, *Da fala para a escrita: atividades de retextualização* (Cortez) | Também serve para Linguística 6.2 e 7.2 |
| Padrão da Câmara | Notas taquigráficas e Diário da Câmara (portal) + normas do Detaq, se publicadas | Fonte primária de 2.4 |
| LGPD e direitos autorais | Lei 13.709/2018 e Lei 9.610/1998 (texto compilado) + guias da ANPD | Lei seca |

> Pode me mandar PDFs e páginas salvas: eu extraio, resumo e gero itens C/E, como fizemos na CGU. A rede desta sessão bloqueia downloads diretos.

## 6. Como conseguir questões quando quase não existem

1. **Análogas da CEBRASPE** (QConcursos/TEC, filtrando Banca CEBRASPE):
   - **LGPD**, **Segurança da Informação** (princípios, criptografia, controle de acesso);
   - **Inteligência Artificial / Aprendizado de Máquina / Processamento de Linguagem Natural** (LLM, embeddings, alucinação, RAG);
   - **Direito Autoral**.
2. **Busca por termo, em qualquer banca:** "reconhecimento de fala", "transcrição", "diarização", "Whisper", "speech-to-text", para mapear o que as bancas já perguntaram.
3. **Provas de taquigrafia e revisão legislativa** (Câmara, Senado, Assembleias): para degravação, revisão e retextualização.
4. **Banco próprio:** a cada resumo, eu gero 10–15 itens C/E inéditos no estilo CEBRASPE. Meta: **150+ itens** até a semana 6.

## 7. Laboratórios (calibram o bom senso)

- **Laboratório 1 — WER na prática (semana 3, 1h30):**
  1. Pegue 3 minutos de uma sessão da Câmara (vídeo oficial).
  2. Gere a transcrição automática (Whisper ou a legenda automática do YouTube).
  3. Compare com as **notas taquigráficas oficiais** do mesmo trecho.
  4. Conte substituições, deleções e inserções e calcule o WER.
  5. Classifique os erros: homófono, nome, número, negação, pontuação, orador.
- **Laboratório 2 — retextualização (semana 4, 1h):**
  1. Pegue 1 minuto da transcrição bruta.
  2. Transforme-o no padrão das notas taquigráficas.
  3. Liste as **operações de retextualização** que usou.
  4. Anote o que você mudou e o que **não poderia** mudar, para preservar a fidelidade.

## 8. Bom senso em C/E (quando não souber o conteúdo)

> **São tendências, não regras.** Use só para decidir se vale arriscar.

- **Afirmações absolutas** costumam ser **erradas**: "elimina erros", "dispensa revisão humana", "garante 100%", "sempre identifica o falante".
- Afirmações que reconhecem **trade-offs** costumam ser **certas**: "reduz a latência à custa de acurácia", "melhora, mas não elimina".
- **Supervisão humana, transparência, minimização de dados e segurança** são sempre a resposta "institucionalmente correta" num contexto parlamentar ou público.
- Desconfie de **troca de conceitos vizinhos**: diarização × identificação; WER × DER; extrativa × abstrativa; lexical × semântica; *batch* × *streaming*.
- **Penalização:** um erro anula um acerto. Só vale responder se você acha que tem **mais de 50% de chance** de acertar. Com 60% ou mais, responda; abaixo disso, deixe em branco.

## 9. Integração com o Omni

- O **glossário** (cerca de 60 termos) vira **flashcards** no formato `front/back` do Omni.
- Registre cada subtópico estudado no Omni para as **revisões espaçadas** (D+1, D+7, D+30).
- Atualize o status nas fichas e na tabela da matéria (⬜ → 🟨 → ✅ → 🔁).
