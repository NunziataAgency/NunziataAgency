# Failles PHP « php2shell » (à confirmer) et la coupure de mercredi — dossier du 21/10/2026
Environ 25 sources consultées (résultats de recherche) · presse 12 · X 0 · newsletters 0 (Gmail non interrogé) · primaires 3 pages lues (php.net, blog Cloudflare index, cloudflarestatus). Limites : article Wired illisible, budget de 4 WebFetch épuisé, aucune page détaillant les failles n'a été trouvée.

## 🆕 Mise à jour : la faille s'appelle PHP2Shell (sources trouvées)
- **Nom** : PHP2Shell, deux failles critiques (**CVE-2026-109618 et CVE-2026-109619**), notées 9,2/10 par les développeurs de PHP et 10/10 par la société de sécurité watchTowr. ⚠️ Certaines pages intervertissent les deux numéros : vérifie dans l'avis officiel de PHP.
- **Ce qu'elles permettent** : prendre le contrôle complet d'un serveur à distance, sans identifiant et sans action de la victime, via un simple fichier envoyé. Elles touchent toutes les installations PHP qui servent des pages web (PHP-FPM, mod_php, FrankenPHP), c'est-à-dire les sites WordPress, Drupal, Magento…
- **Versions touchées** : PHP 5, 7 et 8 en entier. Correctifs : **8.5.12, 8.4.27, 8.3.36 et 8.2.35**, publiés le **mercredi 21/10**. Aucun correctif pour PHP 5 et 7, versions encore utilisées par de vieux sites.
- **Le raté** : les détails ont **fuité en ligne avant la publication coordonnée** des correctifs.
- **Les attaques ont déjà commencé** : watchTowr observe des exploitations dans la nature dès le 21/10 ; Cloudflare a vu du trafic d'attaque contre ses clients avant la sortie des correctifs ; Sansec s'attendait à des attaques massives « dans les 15 minutes » ; l'agence néerlandaise NCSC-NL signale des exploits publics et prévoit des attaques à grande échelle.
- **Solutions de dépannage** : relever la limite de mémoire de PHP (pour la 1re faille) et désactiver la fonction « session upload progress » (pour la 2e), en attendant la mise à jour.
- **La « coupure de mercredi »** : aucune panne d'internet majeure n'a eu lieu mercredi (seulement une latence de Cloudflare en Inde, environ 3 h). Ce qui s'est passé mercredi, c'est la **sortie en urgence des correctifs**. C'est sans doute ce que l'auteur a entendu.
- Sources :
  - Bleeping Computer — https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/
  - Help Net Security, 21/10 — https://www.helpnetsecurity.com/2026/10/21/php2shell-php-vulnerabilities-patched-cve-2026-109618-cve-2026-109619/
  - SecurityWeek — https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/
  - watchTowr — https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/
  - JFrog — https://research.jfrog.com/post/php2shell-all-you-need-to-know-about-cve-2026-109618-and-cve-2026-109619/
  - Imperva — https://www.imperva.com/blog/php2shell-vulnerability-updates/
  - Brandefense — https://brandefense.io/blog/php2shell-php-rce-cve-2026-109618-109619/
  - Wikipédia — https://en.wikipedia.org/wiki/PHP2Shell
  - Techpresso (21/10) — https://archive.techpresso.co/p/critical-php-flaws-hit-millions-of-sites
  - Wired (article d'origine) — https://www.wired.com/story/this-is-not-a-drill-2-php-vulnerabilities-are-setting-the-internet-on-fire/

## L'essentiel en 5 lignes
1. Rien de vérifiable n'a été trouvé sur les deux failles : pas de CVE, pas de versions, pas d'avis php.net d'octobre 2026 dans les recherches. Tout vient du résumé Techpresso/Wired (non lu).
2. Seul indice primaire : l'index du blog Cloudflare liste le 21/10/2026 « Cloudflare deploys protections against php2shell vulnerability » (titre seul, article non lu). « php2shell » est donc très probablement le nom de la faille ; aucun autre média trouvé.
3. Le « avant la publication » du brief est cohérent avec une protection WAF Cloudflare publiée le jour même, mais rien de lu ne le prouve.
4. La « coupure de mercredi » : aucune panne internet majeure trouvée ni pour le 21/10 ni pour le 14/10. Le seul incident Cloudflare du mercredi 21/10 : « Increased Latency in India » (dès 16h42 UTC, ~3h15 selon cloudflarestatus). Aucun lien démontré avec PHP.
5. Contexte utile : 2026 a eu wp2shell (WordPress, 17/07) et une série de failles « x2shell » ; la menace « fichier envoyé → contrôle du serveur » est devenue banale, d'où l'intérêt d'un angle pratique plutôt qu'alarmiste.

## Ton avis à l'épreuve des faits
- Avis de l'auteur : « c'est quoi la coupure de mercredi » (question, pas thèse).
- Soutient un lien possible : un mercredi (21/10) a bien un incident Cloudflare, et Cloudflare publie le même jour sur la faille PHP.
- Contredit : l'incident du 21/10 est un souci de latence en Inde, durée ~3h15, sans mention PHP (titre seul). Les autres incidents Cloudflare d'octobre sont des 19-20/10 (Gemini/SWG, Zero Trust, bots). Pas de panne grand public trouvée.
- Autre candidat : mercredi 14/10 = billet Cloudflare sur la panne Yandex (frappes de drones ukrainiennes sur 3 datacenters Yandex du 8 au 11/10 selon la presse ; hors sujet PHP). L'auteur peut aussi parler d'une panne locale (ex. opérateur Free le 06/10, 09/10) : à lui de préciser.
- Pour muscler : demander à l'auteur où il l'a entendue (service, pays) ; vérifier Downdetector et la page d'état du service concerné.

## Avis divergents
Insuffisant : non trouvé sur la faille PHP elle-même (aucune voix d'expert retrouvée, X non accessible). Voix divergentes de CONTEXTE, à ne pas confondre avec le sujet :
1. Ipregistry (blog) : l'arrêt de Yandex n'a pas stoppé les bots, qui ont changé d'ASN ; « bloquer par réseau ne dure jamais ». Pertinence : relativise l'idée que couper un acteur règle la menace. Crédibilité moyenne (éditeur de données IP). https://ipregistry.co/blog/yandex-outage-bots-changed-asn (📅 oct. 2026, date exacte non lue)
2. Défaut de lecture de l'article Wired : titre dramatique ; la sécurité réelle dépend des réglages. Sans source lue, je ne cite personne : À CHERCHER (experts relativisant la panique, ex. Cloudflare, Patchstack, Wordfence, CERT-FR).
3. Cas wp2shell (juillet) : un tracker mesurait 81,6 % de sites WordPress déjà patchés sur 124 580 testés (via Elastic/Security Arsenal, résumé de recherche), soit une majorité protégée grâce aux mises à jour automatiques. Argument : la panique est tempérée par l'auto-update. Source secondaire, à vérifier. https://securityarsenal.com/blog/cve-2026-60137-and-cve-2026-63030-wp2shell-wordpress-exploitation-detection-and-hardening-guide
Conclusion : pas trois voix divergentes sur la faille PHP trouvées, à compléter.

## Ce qui s'est passé (chronologie datée)
- 17/07/2026 : wp2shell (WordPress, CVE-2026-63030 et CVE-2026-60137), exploitation en moins d'une heure après divulgation, selon Defiant (via Elastic). Précédent, pas notre sujet.
- 08-11/10/2026 : frappes sur datacenters Yandex (presse, attribution non officielle).
- 14/10/2026 (mercredi) : Cloudflare publie son analyse Yandex ; Drupal corrige deux RCE (CVE-2026-108097, CVE-2026-108099) selon Next.
- 24/09/2026 : PHP 8.5.11 corrige 11 CVE (FPM, OpenSSL, phar, SOAP...), aucune qualifiée RCE par la page lue (php.net ChangeLog).
- 21/10/2026 : Cloudflare publie un billet « php2shell » et un billet WAF « transaction detection » (titres seuls) ; incident « Increased Latency in India » 16h42 UTC.
- ANOMALIE : php.net ChangeLog affiche PHP 8.5.12 et 8.4.27 datés du 22/10/2026 (demain). Soit décalage horaire/erreur de la page, soit page lue non fiable. Ne PAS écrire « PHP 8.5.12 corrige les failles » sans vérifier : la page ne cite aucun CVE pour 8.5.12 (deux GHSA sur la corruption d'état).

## Les chiffres clés
- Aucun chiffre sur les failles php2shell trouvé. Pas de nombre de sites exposés.
- Part du web en PHP / WordPress : non vérifié dans cette recherche (ne pas citer de pourcentage de mémoire).
- PHP 8.5.11 : 11 CVE corrigées (php.net ChangeLog-8.php, 📅 24/09/2026).
- Incident Cloudflare Inde : ~3h15 (cloudflarestatus.com/history).
- wp2shell : 81,6 % patchés sur 124 580 sites (secondaire).

## Les acteurs et leurs positions
- Cloudflare : aurait déployé des protections le 21/10 (titre seul).
- Wired / Techpresso : source de l'alerte, non lue.
- Équipe PHP : correctifs 8.5.x ; lien avec php2shell non établi.
- WordPress/Defiant/Elastic : précédent wp2shell.

## Ce que dit X/Twitter
Non couvert (pas d'API X ; aucune réaction retrouvée).

## Ce que disent les autres newsletters
Non couvert (Gmail non interrogé dans cette passe). Techpresso du 21/10 est la source de départ.

## Les points de débat et ce qui reste incertain
- Existence, CVE, versions, mécanisme exact de « 2 failles PHP » : non établis.
- Exploitation réelle avant publication : affirmation du brief, non recoupée.
- Lien avec la coupure : aucun trouvé.

## 3 à 5 angles proposés
1. « Quelle coupure ? » : l'actu est ailleurs. Thèse : ce qui fait peur (pannes) n'est pas ce qui menace (mises à jour oubliées). Limite : demande d'avoir la panne exacte.
2. Guide pratique PME : 5 gestes (mise à jour auto WordPress/PHP, demander à l'hébergeur sa version PHP, WAF/Cloudflare, sauvegardes, désactiver l'envoi de fichiers inutiles). Limite : ne pas promettre qu'ils suffisent tant que les CVE sont inconnus.
3. Le délai : de la divulgation à l'attaque, en heures (wp2shell : moins d'une heure). Limite : exemple d'un autre cas.
4. La dépendance : PHP et WordPress, briques invisibles. Limite : chiffres de part de marché à sourcer.
→ Le plus fort : angle 2 (utile, vérifiable plus tard), en attendant les CVE ; angle 3 pour l'accroche.

## Les munitions
- Chiffres : 11 CVE dans PHP 8.5.11 ; 3h15 d'incident Cloudflare Inde ; 81,6 % / 124 580 (wp2shell) ; exploitation 13 min après sonde (Defiant, wp2shell) ; 3 datacenters Yandex.
- Citations exactes : titre Wired « This Is Not a Drill: 2 PHP Vulnerabilities Are Setting the Internet on Fire » ; titre Cloudflare « Cloudflare deploys protections against php2shell vulnerability ». Aucune autre citation vérifiée.
- Détail : le nom « x2shell » (wp2shell, Click2Shell, XSS2Shell) devient une marque de fabrique des failles 2026.

## Le stock d'articles
Presse / primaires
- ⭐ Index du blog Cloudflare — Cloudflare — 📅 21/10 — https://blog.cloudflare.com/ — titres php2shell, WAF, Yandex — primaire, titres seuls.
- ⭐ Historique d'incidents Cloudflare — 📅 21/10 — https://www.cloudflarestatus.com/history — incident Inde 16h42 UTC — primaire.
- ⭐ Changelog PHP 8 — php.net — 📅 24/09 et « 22/10 » (anomalie) — https://www.php.net/ChangeLog-8.php — primaire.
- Wired, article source — 📅 21/10 — URL de la consigne — illisible (bloqué).
- wp2shell, BleepingComputer — 📅 07/2026 — https://www.bleepingcomputer.com/news/security/critical-wp2shell-wordpress-flaws-exploited-to-install-webshells/amp/ — contexte.
- wp2shell, Elastic Security Labs — 📅 07/2026 — https://www.elastic.co/security-labs/wp2shell-wordpress-rce-detection-elastic-defend — contexte.
- Drupal : deux failles critiques — Next — 📅 14/10 — https://next.ink/brief-article/drupal-colmate-deux-failles-critiques-exploitables-a-distance/ — contexte voisin, hors PHP.
- Yandex, analyse bots — Ipregistry / ppc.land / Computing — 📅 oct. 2026 — https://ipregistry.co/blog/yandex-outage-bots-changed-asn — avis divergent, hors sujet.
- Pannes Cloudflare passées (18/11/2025, 05/12/2025) — TechRadar, Tom's Guide — contexte « mercredi » : AUCUNE n'est un 21/10.
- Pannes Free France (06/10, 09/10, 16/10/2026) — GeoBlackout (rédigé par IA) — fiabilité faible.
Non trouvé : X, newsletters.

À faire côté auteur : coller l'article Wired ou préciser la « coupure » entendue, puis relancer une recherche ciblée sur les CVE.
