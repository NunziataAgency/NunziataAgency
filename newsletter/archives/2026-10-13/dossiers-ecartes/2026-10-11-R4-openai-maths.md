# OpenAI publie 722 manuscrits de maths écrits par une IA — note du 11/10/2026

Méthode : 8 recherches web + 3 lectures de pages (Numerama inaccessible : bloqué par l'outil, non lu). Presque tout vient de sources secondaires ; je n'ai PAS pu ouvrir la page OpenAI ni le GitHub moi-même (URLs relevées via Decrypt). Les posts X ne sont connus que via des articles qui les citent : aucune URL de post X vérifiée. Toute citation ci-dessous est « telle que rapportée » par le média indiqué.

## L'essentiel en 5 lignes
- Le 06/10/2026 (mardi), OpenAI met sur GitHub 722 manuscrits (372 « familles » de résultats) produits par un modèle interne non nommé et non publié, sur ~4 000 problèmes ouverts soumis.
- Vedette : un résultat « quasi-Riemann » (zone sans zéro de la fonction zêta pour Re(s) > 7/8), ce n'est PAS l'hypothèse de Riemann ; Alex Kontorovich (Rutgers) : « instant Fields Medal » si un humain l'avait fait.
- Vérification partielle : seuls 162 manuscrits sur 722 (~22 %) ont leur résultat principal vérifié en Lean ; OpenAI reconnaît que « certains résultats non formalisés pourraient poser problème ». Le 07/10, 3 manuscrits retirés (erreur de signe).
- Contexte tendu : 25 médaillés Fields (dont Tao) ont signé le 11/09 une déclaration contre les preuves IA publiées trop vite et en masse ; un groupe « Association for Human Mathematics » appelle à cesser de travailler avec OpenAI.
- Inquiétude des chercheurs : jeunes chercheurs dont les programmes sont balayés (Buckmaster), culture collaborative fragilisée (Kra), pas de prompts ni de modèle publiés donc pas de reproductibilité (Sutherland).

## Avis divergents
Méthode : 4 recherches + 2 lectures (Decrypt, Officechai). Verdict honnête : 3 voix sceptiques solides trouvées, MAIS aucune voix qui dise « les critiques exagèrent » (cherché explicitement, rien). Citations tirées des pages lues ; posts X non ouverts directement.

Voix sceptiques (≠ « percée historique ») :
1. Andrew Sutherland — mathématicien, MIT (cité aussi par Scientific American) — Argument : sans modèle ni prompts publiés, la revendication « un seul prompt, un seul agent » n'est pas vérifiable. Citation : « treat any claims about one-shotting problems with a single agent as unverified » puis « We should ask for receipts. » — https://decrypt.co/380366/openai-secret-ai-model-cracked-hundreds-math-problems-one-prompt — 📅 07/10/2026
2. Association for Human Mathematics (AHM), groupe de mathématiciens, texte signé « Communications Working Group » (signataires non nommés ; repris en billet invité sur le blog de Tao le 07/10) — Argument : la publication massive viole les normes de la science et sert à montrer sa force ; appel à cesser de travailler avec OpenAI. Citations (fragments, tels que rapportés) : « total disregard » pour les normes qui rendent la science fiable ; « a demonstration of power. » — https://officechai.com/ai/mathematicians-did-not-ask-this-openai-has-total-disregard-for-norms-of-scientific-research/ — 📅 08/10/2026
3. Keith Adler — participe à la formalisation en Lean 4 d'une des preuves (crédibilité : travaille sur le matériel, pas un commentateur extérieur) — Argument : le dépôt est fermé à la contribution (Issues désactivées, aucune pull request acceptée), donc pas de vraie vérification collective. Citation : « That's disappointing. » (X, 07/10) — https://x.com/keithadler/status/2107940309758054728 (lien relevé par Decrypt, non ouvert) — 📅 07/10/2026
4. Institute for Advanced Study (Princeton), statement cité via The Guardian — Argument : la compréhension humaine reste l'enjeu, la participation de son groupe consultatif n'est pas une caution. Citation : « human understanding of mathematics remains of paramount importance » — https://www.theguardian.com/technology/2026/oct/07/openai-mathematical-findings-concerns (via Decrypt, non ouvert) — 📅 07/10/2026

Voix « les critiques exagèrent » : AUCUNE trouvée. Les plus favorables sont enthousiastes sur le fond mais ne rejettent pas les critiques : Alex Kontorovich (Rutgers, « instant Fields Medal » si un humain, voir plus bas) et Abhishek Saha (« It is a very big day for mathematics. », X, 07/10, https://x.com/ObhishekSaha/status/2107801342722928899 via Decrypt). Daniel Litt (Toronto) est paraphrasé (aucune raison de garder prompts/réponses secrets) : critique de la méthode, pas défense. Ne pas présenter ces voix comme des défenseurs des critiques.

Non trouvés / à ne pas inventer : Tao, Buzzard, LeCun, Gowers n'ont aucun commentaire vérifié sur CETTE publication (Tao n'apparaît que comme signataire de la déclaration du 11/09 et hôte du billet AHM). Gary Marcus a critiqué l'annonce « Astra » (août) : autre événement, citations non lues, hors sujet ici sans vérification.

## Chronologie datée
- 11/09/2026 : déclaration de 25 médaillés Fields (Tao, Deligne, Scholze, Hairer, Viazovska, Villani, Bhargava…) : les buts des labos d'IA et de la communauté sont « severely misaligned » (officechai ; signataires cités par pasqualepillitteri). Un teaser Briefia parle de « 28 lauréats » : écart de chiffre non résolu.
- Septembre 2026 (date exacte non vérifiée) : OpenAI revendique Navier-Stokes (10 000 agents coordonnés pendant 88 h, coût estimé jusqu'à 40 M$ selon titre Briefia) ; Levent Alpöge (Anthropic) aurait contesté le crédit (pasqualepillitteri).
- 21/09/2026 : OpenAI annonce un groupe consultatif indépendant (Advisory Group on Mathematics and AI, IAS, 9 membres bénévoles dont Gowers, Hairer, Witten) — sans pouvoir de décision (thenextweb/aiweekly).
- 29/09/2026 : le groupe recommande publier vite, divulguer modèle, prompts, raisonnement, calcul, éviter l'usage marketing (Decrypt ; letsdatascience, source unique pour certains détails).
- 06/10/2026 : publication des 722 manuscrits sur GitHub + annonce sur X (axeetech) ; l'un des manuscrits clés est daté du 05/10.
- 07/10/2026 : Decrypt et Briefia publient ; OpenAI retire 3 manuscrits (erreur de signe sur « Algebraicity of Weil classes on split abelian eightfolds » + 2 dépendants), révise 14 autres ; catalogue ramené à 719 (aiweekly / Retraction Watch).
- 08/10/2026 : dépêche Option Finance/Zonebourse « un modèle mystérieux d'OpenAI réalise des avancées en mathématiques ».
- 09/10/2026 : Winbuzzer.
- 10/10/2026 : Briefia sur les réactions des chercheurs (Kontorovich, Buckmaster, Kra).

## Chiffres clés (chacun avec source)
- 722 manuscrits / 372 familles — Decrypt 07/10, Briefia 07/10.
- ~4 000 problèmes soumis au modèle, seuls les résultats jugés « assez significatifs » publiés — Decrypt 07/10.
- ~3 h de « ChatGPT Pro thinking » par résultat en moyenne — Briefia 07/10, Decrypt 07/10.
- 162/722 (~22 %) avec résultat principal en Lean — Decrypt 07/10 ; une autre source donne ~42 % des « top-line results » après révision (aiweekly) : unités différentes, à ne pas mélanger.
- 10 résumés de raisonnement publiés — Briefia, Decrypt.
- Zone sans zéro : Re(s) > 7/8 (zêta et fonctions L de Dirichlet) ; un 2e manuscrit (05/10) viserait ~11/12 — officechai (sources divergentes, mindstudio dit 0,875).
- Bibliothèque Lean : 121 734 fichiers, 25,9 M de lignes — Towards AI (secondaire, à recouper).
- 3 manuscrits retirés J+1, 14 révisés, 13 références mises à jour, 719 restants — aiweekly/Retraction Watch 07/10.
- Aucun des 5 problèmes du millénaire ouverts résolu dans ce lot — Nature, rapporté par pasqualepillitteri.
- Navier-Stokes : 10 000 agents, 88 h — Decrypt.
- 25 médaillés Fields, déclaration du 11/09 — officechai.

## Acteurs et positions
- OpenAI : transparence partielle ; manuscrits + Lean + 10 résumés, mais ni nom du modèle, ni prompts, ni calcul par problème. Dépôt avec Issues désactivées, pas de pull requests (Keith Adler, cité par Decrypt). Promet de financer des ateliers pour aider les chercheurs (Briefia 10/10). Porte-parole : presque tout vient d'un seul prompt à un seul agent (Decrypt).
- Alex Kontorovich (Rutgers) : enthousiaste sur Riemann ; selon Briefia 10/10, la formation mathématique « pourrait prendre de l'importance ».
- Tristan Buckmaster (NYU, d'après Briefia) : la publication a mis fin à des programmes de jeunes chercheurs ; craint que des projets non publiés alimentent un LLM.
- Bryna Kra (Northwestern) : risque pour la culture collaborative ; personne ne pourrait présenter ces résultats en conférence.
- Andrew Sutherland (MIT) : tout « one-shot » est non vérifié tant que le modèle n'est pas publié.
- Daniel Litt (Toronto) : aucune raison de garder prompts/réponses secrets.
- Abhishek Saha : « very big day for mathematics ». Dmitry Rybin : « totally unbelievable alien math ».
- Levent Alpöge (Anthropic) : « moment le plus significatif de l'histoire des mathématiques » (pasqualepillitteri) — notable car concurrent.
- Terence Tao / médaillés Fields : critique de la vitesse et de la perte de compréhension (citation « too crazy » d'une source de mauvaise qualité, à ne pas utiliser).
- Francesco Maggi (UT Austin) : qui peut digérer des centaines d'articles ? Association for Human Mathematics : appel à arrêter de travailler avec OpenAI.
- Groupe IAS : « human understanding of mathematics remains of paramount importance » ; participation ≠ caution des résultats.
- Anthropic (comparaison Decrypt) : preuve Lean de Fermat publiée (13 M de lignes), mais formalisation de Wiles 1995, pas du nouveau.

## Ce que dit X (citations avec lien)
Aucun post X ouvert directement ; liens = articles qui les citent.
- Alex Kontorovich : « If a human did this, it would be an instant Fields Medal, no questions asked. » — via https://officechai.com/ai/mathematicians-react-with-shock-and-wonder-after-openai-releases-over-300-math-proofs-at-once/ (et humanprogress.org)
- Dmitry Rybin : « totally unbelievable alien math » — via https://decrypt.co/380366/openai-secret-ai-model-cracked-hundreds-math-problems-one-prompt
- Sam Altman (« looking up at stars with extra awe tonight ») — via https://officechai.com/ai/looking-up-at-stars-with-extra-awe-tonight-sam-altman-after-openai-publishes-300-math-proofs-including-quasi-riemann-hypothesis/ (titre ; libellé exact non vérifié)
- Annonce OpenAI sur X le 06/10 — via axeetech.com (secondaire).

## Débat et incertitudes
- « Digne d'une médaille Fields » : conditionnel (« si un humain »), et pour un résultat qui n'est pas Riemann. Le titre Numerama (non lu) cadre sur Riemann.
- Lean : prouve la cohérence logique, pas que l'énoncé formalisé correspond au problème, ni sa nouveauté (Decrypt). 78 % du lot sans vérification formelle.
- Erreurs déjà : 3 retraits en 24 h.
- Pas de reproductibilité : modèle, prompts non publiés ; non-respect partiel des recommandations du groupe consultatif (2 respectées, 2 en partie, 2 non, selon letsdatascience).
- Comptes confus : « 300 résultats » / « 722 » / « 700+ » = unités différentes (familles vs manuscrits) ; « plus de 100 problèmes » pour la revendication de septembre.
- Qui valide ? Les relecteurs humains sont le goulot ; effet sur carrières des jeunes et crédit des idées.
- Écart : 25 vs 28 médaillés Fields ; contenu exact de la déclaration lu seulement en secondaire.
- Conflit d'intérêts/communication : OpenAI juge et partie ; rivalité Anthropic/OpenAI sur le crédit.

## 3 angles possibles
1. « Après le code, la recherche : la vérification devient le vrai métier » — thèse : quand produire coûte 3 h de calcul, la valeur se déplace vers ceux qui certifient (relecteurs, Lean, audit). Original : on parle de remplacement, pas du goulot de vérification, transposable aux freelances (audit, conseil). Faits : 162/722 en Lean, 3 retraits en 24 h, Maggi « qui peut digérer ? », 25 Fields.
2. « Le secret de fabrication : OpenAI publie les résultats, pas la recette » — thèse : la transparence sélective est une stratégie produit/marketing. Original : lit la sortie comme du marketing de capacité, pas de la science. Faits : pas de modèle ni prompts, Issues désactivées, 2/6 recommandations IAS respectées, 4 000 problèmes → 722 triés.
3. « Les juniors d'abord » — thèse : la première victime est le jeune chercheur, comme le junior dev. Original : lien direct avec les métiers intellectuels (entrée de carrière). Faits : Buckmaster (programmes arrêtés), Kra, « calcul de 3 h par résultat ».

Angle le plus fort : n°1. Quand le coût de production s'effondre (3 h/résultat, 4 000 essais), la rareté passe à la vérification et au jugement ; les métiers qui tombent ensuite sont ceux dont le livrable est invérifiable à bas coût. Il s'appuie sur des faits chiffrés (22 % en Lean, 3 retraits) et parle directement aux freelances.

## Munitions
Chiffres frappants :
1. 722 manuscrits en une nuit, ~4 000 problèmes tentés.
2. ~3 h de ChatGPT Pro par résultat.
3. 162/722 seulement vérifiés en Lean (~22 %).
4. 3 retraits à J+1 pour une erreur de signe (+1 au lieu de −1).
5. 25 médaillés Fields signent contre le rythme, 25 jours avant.
Citations (telles que rapportées) :
- « If a human did this, it would be an instant Fields Medal, no questions asked. » — Kontorovich (X, via officechai)
- « We should ask for receipts. » — Andrew Sutherland (via Decrypt 07/10)
- « some of the unformalized results could have issues » — OpenAI (via Decrypt)
- « human understanding of mathematics remains of paramount importance » — IAS (via Decrypt)
- « totally unbelievable alien math » — Dmitry Rybin (X, via Decrypt)
Détails surprenants :
- Le « mathématicien d'Anthropic » (concurrent) salue le « moment le plus significatif de l'histoire des maths ».
- Le dépôt GitHub d'OpenAI a les Issues désactivées et refuse les pull requests.
- Une erreur +1/−1 a fait tomber un résultat sur la conjecture de Hodge rationnelle.
- Personne ne pourrait présenter ces résultats en conférence (Kra).

## Stock d'articles
(Dates : celles lues dans la page ou dans l'URL ; « n.v. » = non vérifiée.)
- ⭐ Decrypt — « OpenAI Says a Secret AI Model Cracked Hundreds of Open Math Problems in One Prompt—Mathematicians Want Receipts » — Decrypt — 📅 07/10 — https://decrypt.co/380366/openai-secret-ai-model-cracked-hundreds-math-problems-one-prompt — chiffres, citations Sutherland/Saha/Rybin, liens OpenAI (github.com/openai/math ; openai.com/index/sharing-ai-progress-in-mathematics/ non ouverts par moi).
- ⭐ Briefia (réactions) — « OpenAI diffuse 700 résultats mathématiques et alerte les chercheurs » — Briefia — 📅 10/10 — https://briefia.fr/article/openai-diffuse-700-resultats-mathematiques-et-alerte-les-chercheurs — Buckmaster, Kra, Kontorovich, ateliers OpenAI.
- ⭐ Retraction Watch / aiweekly — « OpenAI withdraws three preprints a day after releasing 722 manuscripts » — 📅 07/10 — https://retractionwatch.com/?p=136176 — retraits, erreur de signe (titre vu en recherche, non ouvert).
- Briefia — « OpenAI publie 722 manuscrits mathématiques et détaille sa méthode » — 📅 07/10 — https://briefia.fr/article/openai-publie-722-manuscrits-mathematiques-et-detaille-sa-methode — 3 h de calcul, 372 ensembles, critères d'évaluation.
- Numerama — « Si un humain avait fait ça, ce serait la médaille Fields » — 📅 n.v. — https://www.numerama.com/tech/2348207-si-un-humain-avait-fait-ca-ce-serait-la-medaille-fields-lia-dopenai-fait-une-percee-sur-lhypothese-de-riemann.html — NON LU (accès bloqué).
- Officechai — preuves quasi-Riemann/UGC/Hodge — 📅 n.v. (06-07/10) — https://officechai.com/ai/openai-releases-ai-generated-proofs-of-quasi-riemann-hypothesis-unique-games-conjecture-hodge-conjecture-for-cm-abelian-varieties/ — contenu technique, Altman, Lean.
- Officechai — réactions « shock and wonder » — 📅 n.v. — https://officechai.com/ai/mathematicians-react-with-shock-and-wonder-after-openai-releases-over-300-math-proofs-at-once/ — citations X.
- Officechai — déclaration des 25 Fields — 📅 11/09 (signature) — https://officechai.com/ai/25-fields-medal-winners-including-terence-tao-sign-declaration-saying-rapid-ai-proofs-are-harming-math-in-severe-misalignment/
- Winbuzzer — 📅 09/10 — https://winbuzzer.com/2026/10/09/openai-shares-hundreds-of-math-results-from-an-unreleased-ai-xcxwbn/
- Option Finance — 📅 08/10 — https://www.optionfinance.fr/info-financiere-en-continu/d/2026-10-08-un-modele-mysterieux-dopenai-realise-des-avancees-en-mathematiques.html — presse FR dépêche.
- Letsdatascience — « OpenAI posted 722 AI-written math papers, kept the prompts » — 📅 n.v. — https://letsdatascience.com/blog/openai-posted-722-ai-written-math-papers-kept-the-prompts — grille IAS (2/6).
- Pasquale Pillitteri (FR) — 📅 n.v. — https://pasqualepillitteri.it/fr/news/21360/openai-problemes-millenaire-riemann-hodge — Nature, Alpöge (source de faible fiabilité).
- Towards AI — 📅 n.v. — https://pub.towardsai.net/openais-ai-wrote-722-maths-papers-checking-them-was-the-easy-part-886e1a827c28 — angle vérification (payant).
- The Next Web — groupe consultatif — 📅 ~21/09 n.v. — https://thenextweb.com/news/openai-maths-advisory-group-100-open-problems
- YourStory — 📅 n.v. — https://yourstory.com/ai-story/openai-ai-open-maths-problems-solved
