---
name: newsletter
description: Workflow complet de préparation d'un numéro de la newsletter — veille de toutes les newsletters Gmail en grosse liste numérotée, choix par l'utilisateur, rédaction des Liens en bref choisis et note de synthèse de recherche pour chaque Rubrique choisie. À utiliser quand on dit « prépare ma newsletter », « lance la veille de la semaine » ou qu'on tape /newsletter.
argument-hint: "[nombre de jours, ex. 7]"
---

# Préparer un numéro de la newsletter

Enchaîne les étapes ci-dessous. Tiens l'utilisateur au courant en une ligne à chaque étape.

## Étape 1 — Veille

Applique `.claude/skills/newsletter-veille/SKILL.md` avec `$ARGUMENTS` comme période.
Si Gmail n'est pas connecté, arrête-toi là avec l'explication prévue dans ce fichier.

## Étape 2 — Choix (c'est l'utilisateur qui décide)

La veille donne une grosse liste numérotée (R1… pour les Rubriques, B1… pour les Liens en bref).
Affiche-la en entier dans le chat, une ligne par sujet, puis attends que l'utilisateur réponde avec les numéros choisis (autant qu'il veut dans chaque liste).
Ne choisis jamais à sa place.

Un numéro `R…` suivi de « (en bref) » se traite comme un Lien en bref. Les `F…` (Fun & actionnable) aussi.

La sélection peut contenir un bloc « Mes liens : » (ajouté depuis la page mobile), une ligne par lien : `- [Lien en bref|Rubrique] <url> — <note>`. Traite chaque lien perso comme un sujet choisi du type indiqué : lis la page (WebFetch) pour en tirer le sujet, puis envoie-le au même traitement que les autres (rédaction pour un Lien en bref, note de synthèse pour une Rubrique, avec ce lien comme première source).

## Étape 3 — Recherche

En parallèle :
- **Rubriques choisies** → d'abord la **fiche de l'article d'origine** : `.claude/skills/newsletter-fiche/SKILL.md`. Puis attends l'avis de l'utilisateur (message « Recherche R4 — mon avis : … », ou bloc « Mes avis : » dans la sélection). Seulement alors, la recherche complète guidée par cet avis : `.claude/skills/newsletter-dossier/SKILL.md` (note de synthèse, pas de texte rédigé). Si l'avis est déjà donné dans la sélection, enchaîne fiche puis recherche sans attendre ;
- **Liens en bref choisis** → vérification et **rédaction** : `.claude/skills/newsletter-brefs/SKILL.md` ;
- la génération des questions du jour liées à l'actu de la semaine : `.claude/skills/question-du-jour/SKILL.md`, mode `generer actu`.

Puis la question du jour (mode `choisir` du même fichier).

## Étape 4 — Récap

Écris `newsletter/numeros/AAAA-MM-JJ.md` :

```markdown
# Numéro du JJ/MM/AAAA — préparation

## Rubriques
- <sujet> — angle le plus fort : … — note : newsletter/dossiers/<fichier>.md

## Liens en bref (rédigés, prêts à coller)
1. **<Titre>** — <texte> — [lien](url) ✅

## Question du jour
<id> — <question> (<format>)
```

Puis mets à jour la page (onglet « Mon numéro ») : `python3 newsletter/app/build.py` et publie `newsletter/app/veille.html` avec l'outil Artifact sur `https://claude.ai/artifact/CKhVmMUZynduL57bPZrDG2`.

Termine dans le chat par : les rubriques et leur angle le plus fort, les liens en bref rédigés (avec ⚠️/❌ si besoin), et les chemins des fichiers. Ne rédige pas les rubriques : l'utilisateur les écrit lui-même à partir des notes.
