# Faille PHP2Shell : la guerre des IA pour un trophée — dossier du 01/11/2026
23 sources · émission Silicon Carne + presse 13 + primaires (W3Techs, CISA, Sénat, curl) 6 + avis 8 · X : couverture nulle

## 📰 L'épisode de Silicon Carne — la fiche
Source : épisode de Silicon Carne (Carlos Diaz, en direct de San Francisco) avec Greg Gambatto (Contrôle G, ex-Unleadust) et « Nicoo », ingénieur sécurité senior chez Trail of Bits — transcription collée par l'auteur. 📅 fin octobre 2026.
⚠️ Transcription automatique (noms déformés : « Calif » = probablement Calif, « Wi » = Wiz, « Entropique » = Anthropic, « page de planète » = Patch the Planet). Les chiffres sont des affirmations orales des invités, non vérifiées.
⚠️ Déjà traité le 23/10 : l'explication technique des deux failles PHP2Shell (« Internet en panne et réflexion business »). Le nouvel angle est la bataille pour la paternité de la découverte et ce qu'elle dit de l'IA en cybersécurité.

### La thèse en une phrase
Les IA trouvent désormais les failles presque toutes seules, mais l'histoire PHP2Shell montre une guerre de communication entre labos (OpenAI contre Google/Wiz) pour s'en attribuer le mérite, alors que le vrai goulot n'est plus de trouver les bugs mais de les corriger.

### Ce que dit l'émission
- **La faille** : selon Carlos Diaz, toutes les versions de PHP depuis la 5.4 permettraient à un pirate, sans mot de passe, de prendre le contrôle d'un serveur ou de lire sa mémoire (deux failles notées 9,2/10). PHP fait tourner « à peu près » 70 % du web (WordPress…). Mettre à jour son app ne suffit pas, c'est le moteur en dessous qui est touché. Le bug serait connu depuis une dizaine d'années et mis « sous le tapis ».
- **Qui l'a trouvée ?** Officiellement, un chercheur de **Calif** (start-up de sécurité), avec un modèle d'OpenAI (« GPT-5 » ?), dans le cadre de **Patch the Planet**. Ensuite, **Wiz** (filiale de Google) a trouvé des variantes et a tout misé sur la com : son cofondateur au Wall Street Journal, attribution à **Gemini 4**, une vidéo Google prête à l'avance. Wiz aurait même acheté un nom de domaine dédié (rumeur citée à l'antenne). Pour Nicoo : « beaucoup de marketing drama ». Pour Greg : « c'est la foire à la saucisse en termes de communication ».
- **La vraie histoire est moins vendeuse** : un expert qui connaissait déjà PHP a guidé le modèle. Un chercheur de Calif avait déjà trouvé des pistes en 2004, et les bugs trouvés sont des variantes de bugs de 2004 et 2020. Les modèles excellent en « variant analysis » : partir d'une famille de bugs pour en trouver des variantes. Greg : dire « un expert a guidé l'IA » est « vachement moins telling » que « l'IA a tout trouvé seule ».
- **Patch the Planet** : une initiative bénévole de Calif, HackerOne et Trail of Bits avec OpenAI, qui fournit modèles et tokens pour chercher des failles dans les grands projets open source. Les projets candidatent et OpenAI choisit. C'est la fondation PHP qui a demandé à y entrer.
- **Les chiffres qui piquent** :
  - le budget de la fondation PHP serait de **683 550 $** par an, de quoi payer environ 10 développeurs ;
  - c'est le prix d'**un seul** expert cyber de la Silicon Valley : chez Anthropic, entre 300 et 454 k$ de fixe plus des actions, soit environ 650-700 k$ par an de coût ;
  - le budget de tokens d'un chercheur en failles très actif : **50 000 à 200 000 $ par mois**, voire plus ;
  - la cybersécurité ne représenterait que **4 à 6 % du budget informatique** des entreprises, dont environ 80 % de « théâtre de compliance » (des tests d'intrusion à 6 000 € par trimestre, des cases cochées).
- **Le basculement pour les mainteneurs** : avant, ils recevaient du « AI slop » (des faux rapports bien écrits mais faux). Aujourd'hui, il n'y a presque plus de faux positifs et ils sont submergés par de **vrais** rapports (exemple : le projet curl). Le goulot, c'est de corriger vite et proprement sans créer de nouveaux bugs. C'est désormais le cœur du métier de Trail of Bits.
- **Les frigos Intermarché/Super U** : selon Vincent Strubel (patron de l'ANSSI, devant le Sénat), l'attaque n'était « pas du tout sophistiquée ». Après un article de chercheurs sur les failles de Danfoss, un attaquant (sans doute aidé par un modèle open source) a trouvé un mot de passe admin du type « 1234 ».
- **Défense contre attaque** : les « gentils » ont plus de puissance de calcul, mais beaucoup de failles sont simples. OpenAI teste « Daybreak » : des modèles sans garde-fous réservés aux défenseurs. Les modèles chinois sans garde-fous, ou faciles à contourner, compliquent tout. Un néocloud aurait été attaqué avec GLM 5.3 (selon Greg, non vérifié).
- **Open source, l'arme à double tranchant** : Greg, pro open source, compare au débat sur les armes aux États-Unis et dit qu'il pourrait « changer d'avis ». Nicoo défend l'open source : on ne peut pas laisser « toute l'intelligence du monde » à trois entités (Anthropic, OpenAI, Google), et les garde-fous se font contourner de toute façon.
- **Le pronostic** : Greg : « court terme, je pense que ça va être une énorme boucherie », pendant 6 à 12 mois, puis un code bien plus sûr dans 12 à 24 mois. Nicoo : la « sécurité par l'obscurité » est morte, car l'attaquant est désormais une machine qui ne se lasse jamais. Les hôpitaux et les municipalités cherchent tous des profils cyber.
- **En aparté** : Carlos Diaz déplore un article du Monde sur des jeunes qui se tournent vers les métiers manuels par peur de l'IA : « hier ils faisaient des facs de psycho, maintenant ils font des CAP pâtisserie ». Nicoo : en France, travailler avec les labos d'IA, c'est comme « bosser chez Total il y a quelques années ».

### Ce qui est solide / ce qui est fragile
- **Solide** : les failles PHP2Shell, leur note de 9,2, l'urgence des correctifs, l'attaque des frigos Danfoss (déjà vérifiées pour les numéros des 20 et 23/10).
- **Fragile** (oral, à vérifier) :
  - la chronologie Calif → Wiz → OpenAI, Gemini 4 contre GPT-5 ;
  - la vidéo Google et le nom de domaine acheté par Wiz ;
  - le budget de la fondation PHP (683 550 $) ;
  - les salaires d'Anthropic ;
  - les 4 à 6 % de budget cyber ;
  - l'attaque avec GLM 5.3 ;
  - le mot de passe « 1234 » ;
  - « Patch the Planet » et « Daybreak ».

### Ce que l'émission ne dit pas
- Combien de sites ont réellement été compromis ? (Le 23/10, tu as écrit « plus de 57 000 sites KO ».)
- Qui paie les correctifs des projets open source sur le long terme ?
- Un avis extérieur aux labos : Trail of Bits travaille avec eux, et l'invité reconnaît ne pas être « le mieux placé pour avoir un regard objectif ».

### Pistes d'angle
1. ⭐ **« Qui a trouvé la faille ? La guerre des labos pour un trophée »** : comme pour les découvertes en mathématiques, OpenAI et Google se disputent la paternité. Le marketing dépasse la vérité : c'est un expert humain qui a guidé l'IA.
2. **« Le web tient sur 683 000 $ »** : la fondation PHP a le budget d'un seul ingénieur de la Silicon Valley, alors qu'elle fait tourner 70 % du web.
3. **« Trouver les failles n'est plus le problème, les réparer l'est »** : les mainteneurs sont submergés de vrais rapports. Le nouveau goulot, ce sont les humains.
4. **« La cyber, c'était du théâtre »** : 4 à 6 % du budget informatique, des cases cochées, un mot de passe « 1234 » sur des frigos.

## L'essentiel en 5 lignes
- **Chronologie vérifiée** :
  - **Calif** commence l'audit le 30/07 dans le cadre de Patch the Planet et signale le 1er bug à PHP le **11/08** ;
  - **Wiz** (filiale de Google, rachetée 32 Md$) trouve la même faille de son côté le 19/08 et la signale le **24/08** ;
  - **OpenAI** (Codex Security) signale d'autres vecteurs le **18/09** ;
  - la vidéo de démonstration de Calif fuite par erreur le 20/10, et les correctifs sortent le **21/10**, un jour plus tôt que prévu.
- **La guerre Google contre OpenAI est en partie un mythe** : Wiz a utilisé Gemini 4 Argon, mais aussi GPT-5.6 Sol d'OpenAI et son propre outil, Wiz Atlas. L'avis officiel de PHP crédite les trois équipes sur les deux failles, dans un ordre différent pour chacune.
- **C'est l'humain qui a mené l'audit** : Calif écrit « No special harness, or access to models that weren't generally available to everyone were used » et parle de « my LLM companion ». OpenAI, de son côté, affirme : « frontier AI found these vulnerabilities before attackers did ».
- **Le vrai goulot n'est plus de trouver les failles mais de les corriger** : curl est passé du « AI slop tsunami » au « security report tsunami » (Daniel Stenberg, avril 2026). PHP a dû trier plus de 100 rapports invalides générés par IA.
- **Les dégâts restent flous** : la CISA confirme que les deux failles sont exploitées, mais il n'existe aucun décompte de victimes. Le groupe Dream revendique 25 serveurs piratés. ⚠️ **Le chiffre de « 57 000 sites KO » de ton numéro du 23/10 est introuvable** : à ne pas répéter.

## ✅ / ⚠️ / ❌ — ce que disait l'émission
- ✅ La faille touche PHP depuis la 5.4, ne demande pas de mot de passe et est notée 9,2/10.
- ✅ Les correctifs sont sortis le 21/10.
- ✅ L'ordre de découverte : Calif, puis Wiz, puis OpenAI.
- ✅ Wiz appartient à Google.
- ✅ Les failles sont des variantes de pistes déjà repérées en 2004 (Stefan Esser) et 2020.
- ✅ curl est bien passé du « slop » à l'avalanche de vrais rapports, et a arrêté son programme de primes aux failles le 31/01/2026.
- ⚠️ « 70 % du web » : PHP fait tourner **70,2 % des sites dont on connaît le langage serveur** (W3Techs), pas 70 % de tout le web.
- ⚠️ « Calif a utilisé GPT-5 » : OpenAI dit GPT-5.6 Sol ; Calif ne nomme pas le modèle.
- ⚠️ « Wiz attribue tout à Gemini 4 » : Wiz cite aussi GPT-5.6 Sol et Wiz Atlas.
- ⚠️ « Patch the Planet, initiative bénévole de Calif, HackerOne et Trail of Bits » : c'est surtout une initiative d'OpenAI avec Trail of Bits, lancée le 22/06/2026. Elle porte sur 19 projets open source et a produit des centaines de bugs et des dizaines de correctifs dès la première semaine.
- ⚠️ « Daybreak, des modèles sans garde-fous pour les défenseurs » : c'est le programme défensif d'OpenAI, doté d'1 Md$ d'accès subventionné. « Sans garde-fous » n'est pas confirmé.
- ⚠️ « 4 à 6 % du budget informatique » : c'est plutôt environ 3,9 % en 2026 (Gartner : 248,9 Md$ pour la sécurité, sur 6 370 Md$ de dépenses informatiques).
- ⚠️ « Environ 10 développeurs à la fondation PHP » : en réalité 1 salarié à temps plein et 14 prestataires, surtout à temps partiel.
- ⚠️ Les frigos : l'ANSSI (Vincent Strubel) parle de « défauts de sécurisation élémentaire » et de « mots de passe faibles ». La formule « très faible sophistication mais très fort impact politique » est de Nicolas Roche (SGDSN). L'attaque date de la nuit du 12 au 13/10 et touche aussi Leclerc, Carrefour et Monoprix.
- ❌ Le budget de la fondation PHP de **683 550 $** n'apparaît nulle part. Les chiffres trouvés : 784 376 $ de dépenses en 2025 et 730 534 $ de dons (source relais, à vérifier sur Open Collective). L'idée d'un budget minuscule tient, mais il faut changer le chiffre : environ **780 000 $ par an**.
- ? Introuvables : l'interview du cofondateur de Wiz au WSJ, la vidéo Google préparée à l'avance, le nom de domaine acheté par Wiz, les salaires d'Anthropic (300-454 k$), les budgets de tokens (50-200 k$ par mois), l'attaque avec GLM 5.3, et le mot de passe « 1234 ».

## Avis divergents
1. **Ryan Austin (Calif)**, qui a découvert la faille : c'est l'humain qui a mené l'audit avec un modèle grand public, « No special harness ».
2. **Capital & Compute**, blog d'analyse : dire « OpenAI a trouvé le bug » écrase trois événements distincts en un seul. Dans tous les cas, « a human researcher drove the audit ». L'IA rend la recherche de failles moins chère, pas leur correction. https://capitalandcompute.net/blog/who-found-php2shell
3. **Greg Brockman (OpenAI)** reconnaît sur X que « the tail end of the disclosure didn't go as planned ».
4. **Hostinger (26/10)**, côté rassurant : aucune intrusion réussie n'était publiquement confirmée à cette date. https://www.hostinger.com/blog/what-is-php2shell/
5. **Daniel Stenberg (curl)** : le problème n'est plus le « slop », c'est l'avalanche de rapports crédibles qui lui prend des heures chaque jour. https://simonwillison.net/2026/Apr/3/daniel-stenberg/
6. **Le débat sur l'open source** :
   - **Tom Uren (Lawfare)** : interdire les modèles ouverts chinois serait une erreur, ils servent aussi la défense. En face, Scott Bessent (Trésor américain) : « sanctions and Entity List designations will be on the table » (24/07/2026). https://www.lawfaremedia.org/article/knives-are-out-for-open-weight-AI-models
   - **Une coalition de plus de 270 signataires** (dont Nvidia, Microsoft et Meta) défend les modèles ouverts.
7. **Les agences** :
   - le NCSC britannique (01/05/2026) prévoit une « vulnerability patch wave », une vague de correctifs ;
   - les Five Eyes (22/06/2026) disent que l'IA peut transformer la cyberattaque comme la cyberdéfense « en mois, pas en années » ;
   - l'ANSSI voit l'IA comme un « multiplicateur d'efficacité » des attaques.

## Détails croustillants
- **Calif a publié sa vidéo de démonstration par erreur la veille des correctifs.** PHP a donc avancé leur sortie d'un jour.
- **Un piège à pirates d'AWS a vu une tentative d'exploitation dès le 17/10**, quatre jours avant l'annonce publique.
- **Wiz a utilisé les modèles d'OpenAI**, alors que l'histoire était racontée comme un duel Google contre OpenAI.
- **Le premier signe de la faille date de 2024**, lors d'un audit de PHP par la société Quarkslab, mais personne ne l'avait exploitée.
- **Anthropic a testé son modèle Mythos sur curl** : il n'a trouvé qu'une seule faille, de faible gravité (source secondaire).
- **XBOW, une IA, est devenue n°1 du classement des chasseurs de failles HackerOne en 2025**, avec environ 1 060 failles soumises.

## Angles proposés
1. ⭐ **« Qui a trouvé la faille ? Le mythe de l'IA qui hacke toute seule »** : la chronologie, le chercheur humain, Wiz qui utilise OpenAI, et le marketing des labos.
2. **« Le web tient sur 780 000 $ par an »** : la fondation PHP, avec un salarié à temps plein, porte 70 % des sites, face à l'IA qui trouve des failles à la chaîne.
3. **« Trouver les failles n'est plus le problème »** : curl et PHP, submergés de vrais rapports.

→ **Le plus fort : le 1, puis le 2 en chute.** Et rectifie discrètement les « 57 000 sites » du 23/10 en parlant d'« exploitation confirmée par les autorités américaines, sans bilan chiffré ».

## Le stock d'articles
- ⭐ Who Found PHP2Shell? — Capital & Compute — 📅 fin 10/2026 — https://capitalandcompute.net/blog/who-found-php2shell
- ⭐ OpenAI says GPT-5.6 Sol found a PHP flaw before attackers did — PPC Land — 📅 21/10 — https://ppc.land/openai-says-gpt-5-6-sol-found-a-php-flaw-before-attackers-did/
- PHP ships emergency patches for critical PHP2Shell flaws — BleepingComputer — 📅 21/10 — https://bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws
- 'PHP2Shell' Bugs Signal Red Alert — Dark Reading — https://www.darkreading.com/application-security/php2shell-bugs-red-alert-security-industry
- ⭐ CISA confirms attackers are exploiting both PHP2Shell flaws — The Next Web — https://thenextweb.com/news/php2shell-flaws-exploited-cisa-kev
- Gemini and GPT helped find PHP flaws — FourWeekMBA — https://fourweekmba.com/ai-gemini-and-gpt-helped-find-php-flaws-in-up-to-70-of-sites/
- AI found the flaw, hackers found the leak — WUNC — 📅 24/10 — https://www.wunc.org/2026-10-24/ai-found-the-flaw-hackers-found-the-leak-the-race-to-save-php2shell
- php2shell: why you don't need to panic — Hostinger — 📅 26/10 — https://www.hostinger.com/blog/what-is-php2shell/
- OpenAI lance Patch the Planet — CSO Online — 📅 06/2026 — https://www.csoonline.com/article/4188321/openai-rolls-out-ai-led-push-to-fix-open-source-software-flaws.html
- PHP, part de marché — W3Techs — https://w3techs.com/technologies/details/pl-php
- ⭐ Cyberattaque des frigos — Public Sénat — 📅 21/10 — https://www.publicsenat.fr/actualites/politique/des-defauts-de-securisation-elementaire-et-des-mots-de-passe-faibles-ont-permis-la-cyberattaque-contre-les-frigos-de-supermarches
- curl met fin à son programme de primes — The Register — 📅 21/01/2026 — https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/
- curl : les rapports IA ne sont plus du slop — Simon Willison — 📅 03/04/2026 — https://simonwillison.net/2026/Apr/3/daniel-stenberg/
- Daniel's week (Daniel Stenberg) — 📅 04/2026 — https://lists.haxx.se/pipermail/daniel/2026-April/000152.html
- Knives are out for open-weight AI models — Lawfare — 📅 24/07/2026 — https://www.lawfaremedia.org/article/knives-are-out-for-open-weight-ai-models
- Les Five Eyes alertent sur les risques cyber de l'IA — Reuters, via Daily Maverick — 📅 23/06/2026 — https://www.dailymaverick.co.za/article/2026-06-23-five-eyes-intelligence-alliance-warns-that-new-ai-models-pose-urgent-cyber-risk/
- Comment XBOW est devenue n°1 sur HackerOne — XBOW — https://xbow.com/blog/top-1-how-xbow-did-it/
- Rapport d'activité 2025 de la fondation PHP (relais, à vérifier) — https://myvaultcms.pages.dev/posts/2026-06-07-php-foundation-2025-impact-report
