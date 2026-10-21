# Comprend-on vraiment les IA ? Goodfire relance le débat — dossier du 19/10/2026
22 sources consultées · primaires (Anthropic, OpenAI, DeepMind, Goodfire, Amodei) 10 · presse 6 · débat/avis 6 · X : couverture quasi nulle

## L'essentiel en 5 lignes
- **Le problème** : personne n'a programmé les IA. On les « cultive » sur des montagnes de données, et même leurs créateurs ne savent pas comment elles fonctionnent à l'intérieur. Amodei : « we do not understand how our own AI creations work ».
- **La piste** : l'« interprétabilité » cherche à ouvrir la boîte noire. Depuis 2023, des progrès réels :
  - des millions de « concepts » repérés dans Claude (34 M en 2024) ;
  - « Golden Gate Claude », un modèle qu'on a rendu obsédé par le pont de San Francisco ;
  - en 2025, on a pu suivre pas à pas le raisonnement de Claude : il prépare la rime d'un vers avant de l'écrire.
- **L'obstacle** : un même neurone réagit à plusieurs choses sans rapport (le « neurone chat et voiture »). La théorie dominante, la « superposition », disait qu'un neurone pouvait mélanger plusieurs concepts.
- **La nouveauté (Goodfire, ~15/10/2026)** : Nick Cammarata, qui avait popularisé cette théorie, dit s'être trompé. Pour lui, les neurones sont déjà « propres » : environ 90 % ont un rôle identifiable dans le modèle Qwen3-32B. Ce serait une bonne nouvelle pour comprendre les IA, mais c'est une « working hypothesis » qui n'a pas été relue par d'autres chercheurs.
- **Le débat** :
  - ceux qui jugent la compréhension urgente pour la sécurité (Amodei, objectif 2027) ;
  - les sceptiques : Neel Nanda (DeepMind), pour qui ce n'est « pas la solution miracle », et Hendrycks, qui juge le système trop complexe ;
  - LeCun, pour qui c'est un problème d'ingénierie à résoudre par itérations successives.

## Ton angle (« le jardin secret de nos IA ») à l'épreuve des faits
- **Ce qui le soutient** :
  - on lit déjà des « pensées » de Claude, comme la planification de la rime ou des concepts partagés entre les langues ;
  - Goodfire affirme que c'est plus simple qu'on ne le croyait ;
  - il y a de l'argent : Goodfire a levé 150 M$ et vaut 1,25 Md$ ;
  - la technologie est classée par la MIT Tech Review parmi les 10 technologies de 2026.
- **Ce qui le freine** :
  - **comprendre 90 % des neurones, ce n'est pas comprendre le modèle** : comprendre les briques ne dit pas comment elles interagissent ;
  - Anthropic reconnaît ne capter qu'« une fraction » des calculs, et passe des heures sur un seul prompt de quelques mots ;
  - Goodfire vend de l'interprétabilité, donc a intérêt à l'optimisme.
- **Le détail qui tue** : quand on demande à Claude comment il calcule, il décrit la méthode scolaire de la retenue, alors qu'il fait tout autrement en interne. Les IA ne savent pas expliquer leur propre fonctionnement. C'est pour ça qu'il faut regarder à l'intérieur.

## Avis divergents
1. **Neel Nanda** (responsable de l'interprétabilité chez Google DeepMind) : « It is not the one thing that will save us, and it still won't be enough for high reliability. » Pour lui, c'est une couche de défense parmi d'autres. Fin 2025, il a recentré son équipe sur une approche « pragmatique », plutôt que de vouloir tout décomposer. https://www.greaterwrong.com/posts/PwnadG4BFjaER3MGf/interpretability-will-not-reliably-find-deceptive-ai (04/05/2025) · https://www.far.ai/events/sessions/neel-nanda-our-pivot-to-pragmatic-interpretability (12/2025)
2. **Dan Hendrycks** (Center for AI Safety) : les IA sont des systèmes complexes. Vouloir les comprendre neurone par neurone revient à prévoir la météo molécule par molécule. « The Misguided Quest for Mechanistic AI Interpretability », AI Frontiers, 05/2025 (paraphrase, à relire avant de citer). https://ai-frontiers.org/articles/the-misguided-quest-for-mechanistic-ai-interpretability
3. **Yann LeCun** : la sécurité de l'IA se règle par l'ingénierie et des améliorations successives, pas par une compréhension complète au départ. Image : se soucier aujourd'hui de la sécurité d'une IA surhumaine, c'est comme s'inquiéter de la sécurité des turboréacteurs en 1920 (citation de seconde main).
4. **OpenAI (2023)** : en faisant expliquer les neurones de GPT-2 par GPT-4, seuls environ 1 000 neurones sur 307 200 ont reçu une bonne explication. « the vast majority of our explanations score poorly ». https://openai.com/index/language-models-can-explain-neurons-in-language-models/
5. **Chanin et al., « A is for Absorption »** : les outils actuels ratent les concepts imbriqués les uns dans les autres. https://arxiv.org/html/2409.14507v3
6. **Le camp de l'urgence, Dario Amodei** : « this lack of understanding is essentially unprecedented in the history of technology ». Il veut un « IRM de l'IA » capable de détecter la plupart des problèmes d'ici 2027. Attention, il est partie prenante. https://www.darioamodei.com/post/the-urgency-of-interpretability

⚠️ Je n'ai trouvé aucune critique publique nommée de l'essai de Goodfire pour l'instant. La couverture de X est faible.

## Ce qui s'est passé
- **09/2022** : « Toy Models of Superposition » (Anthropic) : la théorie selon laquelle un neurone mélange plusieurs concepts.
- **05/2023** : OpenAI fait expliquer les neurones de GPT-2 par GPT-4, avec des résultats faibles.
- **10/2023** : « Towards Monosemanticity » (Anthropic) : on isole des « features » plus lisibles que les neurones (131 072 sur un petit modèle).
- **05/2024** : « Scaling Monosemanticity » : 34 M de features dans Claude 3 Sonnet, et « Golden Gate Claude ».
- **07/2024** : DeepMind publie Gemma Scope, des outils ouverts pour fouiller l'intérieur de son modèle Gemma 2.
- **03/2025** : « Tracing the thoughts » (Anthropic) : suivi pas à pas du raisonnement (rime planifiée, concepts communs aux langues, calcul mental).
- **04/2025** : Amodei publie « The Urgency of Interpretability », avec l'objectif 2027. Anthropic montre aussi que les modèles de raisonnement ne disent pas toujours ce qu'ils pensent.
- **05/2025** : Nanda (« not the one thing that will save us ») et Hendrycks (« misguided quest »).
- **11/2025** : OpenAI entraîne des modèles « creux », avec 16 fois moins de connexions à analyser, mais ils perdent en capacité.
- **12/01/2026** : la MIT Tech Review classe l'interprétabilité parmi les 10 technologies de rupture de 2026.
- **05/02/2026** : Goodfire lève 150 M$ (valorisation 1,25 Md$, menée par B Capital), avec Mayo Clinic et Arc Institute comme partenaires.
- **~15/10/2026** : Goodfire publie « Neural networks are already clean ».

## Les chiffres clés
- 34 M de concepts identifiés dans Claude 3 Sonnet (2024). Amodei parle de plus de 30 M dans un modèle moyen, et d'« un milliard ou plus » de concepts même dans un petit modèle (estimation).
- OpenAI 2023 : plus de 1 000 neurones bien expliqués sur 307 200.
- Goodfire 2026 : environ 90 % des neurones ont un rôle principal, environ 7 % deux rôles, 2 à 4 % restent incompris (Qwen3-32B, résultats préliminaires). Sur le modèle d'images InceptionV1, la part lisible de la dernière couche passe d'environ 5 % à environ 99 % après modification de l'architecture.
- Goodfire : 150 M$ levés à 1,25 Md$ de valorisation.
- Anthropic : « quelques heures » de travail humain pour analyser un prompt de quelques dizaines de mots.

## Les acteurs et leurs positions
- **Anthropic** (Olah, Amodei) : leader du domaine, juge le sujet urgent.
- **Goodfire** (Cammarata, ex-OpenAI) : optimiste, et en fait son business.
- **Google DeepMind** (Nanda) : pragmatique, ce n'est qu'un outil parmi d'autres.
- **OpenAI** : pistes architecturales (modèles « creux »).
- **Les sceptiques** : Hendrycks (trop complexe), LeCun (approche d'ingénieur).
- **Les régulateurs** : l'article 13 de l'AI Act exige que les systèmes à haut risque soient assez transparents pour qu'on comprenne leurs résultats, pas leurs neurones (à faire confirmer par un juriste). https://ai-act-service-desk.ec.europa.eu/fr/ai-act/article-13

## Les points de débat et ce qui reste incertain
- L'essai de Goodfire n'a pas été relu par d'autres chercheurs, et son article technique est attendu.
- Comprendre chaque neurone ne veut pas dire comprendre ce que fait le modèle dans son ensemble.
- Personne ne sait encore si ces méthodes suivront la taille des modèles de pointe.
- À ne pas citer sans vérification : le chiffre « moins de 5 % des calculs compris », le marché de « l'IA explicable », et les « Natural Language Autoencoders » d'Anthropic (source unique).

## 3 à 5 angles proposés
1. ⭐ **« On a construit des cerveaux qu'on ne comprend pas »**
   - La thèse : les IA sont cultivées, pas programmées. Les chercheurs font de la « biologie » des IA.
   - Les faits : la rime planifiée, le calcul expliqué à tort par Claude, Golden Gate Claude.
   - La limite : on n'en comprend encore qu'une fraction.
2. **« Le jardin secret de nos IA s'ouvre-t-il enfin ? »**
   - La thèse : Goodfire dit que c'est plus simple qu'on ne le croyait, un mea culpa d'un des pères de la théorie.
   - La limite : ce n'est qu'une hypothèse de travail, et Goodfire y a un intérêt commercial.
3. **« L'IA ne sait pas comment elle pense »**
   - La thèse : les modèles décrivent mal leur propre raisonnement (calcul, chaîne de pensée), donc on ne peut pas leur faire confiance sur parole.
4. **« L'IRM de l'IA, nouveau marché »**
   - La thèse : Goodfire vaut 1,25 Md$ et l'interprétabilité intéresse la santé, la finance et le crédit (entreprises, régulateurs).

→ **L'angle le plus fort : le 1, avec le 2 en actualité.** On ouvre sur la boîte noire et les exemples concrets d'Anthropic, puis on présente l'essai de Goodfire comme une bonne nouvelle, avec ses deux nuances : c'est une hypothèse, et Goodfire est juge et partie.

## Les munitions
- **Analogies** :
  - **le jardin** : les IA sont « cultivées plus que construites » (Amodei) ;
  - **le cerveau** : on voit les neurones, pas la pensée ;
  - **l'IRM** : un « scanner » de l'IA pour repérer mensonges et failles ;
  - **la valise** : la superposition, c'est une valise trop petite où l'on plie plusieurs affaires ensemble. Goodfire dit que la valise est en fait bien rangée.
- **Citations** :
  - « we do not understand how our own AI creations work » (Amodei) ;
  - « generative AI systems are grown more than they are built » (Amodei) ;
  - « It is not the one thing that will save us » (Nanda) ;
  - « I now think I was making superposition the null hypothesis when it should have been the last hypothesis » (Cammarata) ;
  - « the vast majority of our explanations score poorly » (OpenAI).
- **Détails surprenants** :
  - le neurone « chat et voiture » détecterait en fait une forme en V (phares, moustaches, museaux) ;
  - forcé sur le pont, Claude répond « I am the Golden Gate Bridge » ;
  - Claude choisit sa rime avant d'écrire le vers.

## Le stock d'articles
**Primaires**
- ⭐ Neural networks are already clean — Goodfire (Nick Cammarata, Curt Tigges, Tarun Gogineni) — 📅 ~15/10/2026 — https://already-clean.goodfire.com/
- ⭐ Tracing the thoughts of a large language model — Anthropic — 📅 27/03/2025 — https://www.anthropic.com/research/tracing-thoughts-language-model
- ⭐ The Urgency of Interpretability — Dario Amodei — 📅 04/2025 — https://www.darioamodei.com/post/the-urgency-of-interpretability
- Towards Monosemanticity — Anthropic — 📅 04/10/2023 — https://transformer-circuits.pub/2023/monosemantic-features/
- Scaling Monosemanticity (Golden Gate Claude) — Anthropic — 📅 21/05/2024 — https://transformer-circuits.pub/2024/scaling-monosemanticity/
- Toy Models of Superposition — Anthropic — 📅 14/09/2022 — https://transformer-circuits.pub/2022/toy_model/index.html
- Reasoning models don't always say what they think — Anthropic — 📅 03/04/2025 — https://www.anthropic.com/research/reasoning-models-dont-say-think
- Language models can explain neurons in language models — OpenAI — 📅 09/05/2023 — https://openai.com/index/language-models-can-explain-neurons-in-language-models/
- Weight-sparse transformers have interpretable circuits — OpenAI (arXiv) — 📅 17/11/2025 — https://arxiv.org/abs/2511.13653
- Gemma Scope — Google DeepMind — 📅 31/07/2024 — https://deepmind.google/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models/
- Goodfire, série B — 📅 05/02/2026 — https://www.goodfire.ai/blog/our-series-b

**Presse**
- ⭐ Nick Cammarata… says the theory was wrong — OfficeChai — 📅 16/10/2026 — https://officechai.com/ai/ai-researcher-nick-cammarata-who-helped-discover-superposition-now-says-the-theory-was-wrong-and-thats-great-news-for-understanding-ai/
- Mechanistic interpretability, 10 Breakthrough Technologies 2026 — MIT Technology Review — 📅 12/01/2026 — https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/
- Anthropic CEO wants to open the black box by 2027 — TechCrunch — 📅 24/04/2025 — https://techcrunch.com/2025/04/24/anthropic-ceo-wants-to-open-the-black-box-of-ai-models-by-2027
- Goodfire lève 150 M$ — SiliconANGLE — 📅 05/02/2026 — https://siliconangle.com/2026/02/05/goodfire-raises-150m-funding-enhance-ai-interpretability-platform/
- Les créateurs d'IA ne comprennent pas comment elles fonctionnent — Futura — 📅 06/03/2024 — https://www.futura-sciences.com/tech/actualites/intelligence-artificielle-createurs-intelligences-artificielles-ne-comprennent-pas-elles-fonctionnent-111941
- Cammarata, résumé de l'essai — Crypto Briefing — https://cryptobriefing.com/nick-cammarata-neural-networks-interpretable/ — fiabilité faible.

**Avis contraires**
- ⭐ Interpretability Will Not Reliably Find Deceptive AI — Neel Nanda — 📅 04/05/2025 — https://www.greaterwrong.com/posts/PwnadG4BFjaER3MGf/interpretability-will-not-reliably-find-deceptive-ai
- Our Pivot To Pragmatic Interpretability — Neel Nanda (FAR.AI) — 📅 12/2025 — https://www.far.ai/events/sessions/neel-nanda-our-pivot-to-pragmatic-interpretability
- The Misguided Quest for Mechanistic AI Interpretability — Hendrycks et Hiscott — 📅 05/2025 — https://ai-frontiers.org/articles/the-misguided-quest-for-mechanistic-ai-interpretability
- A is for Absorption — Chanin et al. — https://arxiv.org/html/2409.14507v3
- Goodfire « Already Clean », preuves et limites — braindetox.kr (blog) — https://braindetox.kr/en/posts/neural_networks_already_interpretable_neurons_2026.html
