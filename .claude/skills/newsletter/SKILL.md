---
name: newsletter
description: Workflow complet de préparation d'un numéro de la newsletter — veille de toutes les newsletters Gmail, choix des sujets, recherche approfondie (web, X/Twitter, autres newsletters) et dossier avec angles. À utiliser quand on dit « prépare ma newsletter », « lance la veille de la semaine » ou qu'on tape /newsletter.
argument-hint: "[nombre de jours, ex. 7]"
---

# Préparer un numéro de la newsletter

Enchaîne les étapes ci-dessous. Tiens l'utilisateur au courant en une ligne à chaque étape.

## Étape 1 — Veille

Applique `.claude/skills/newsletter-veille/SKILL.md` avec `$ARGUMENTS` comme période.
Si Gmail n'est pas connecté, arrête-toi là avec l'explication prévue dans ce fichier.

## Étape 2 — Choix (c'est l'utilisateur qui décide)

Avec AskUserQuestion, en une seule fois :

1. **Rubrique** (choix unique) : les 3 sujets les mieux notés + leur note et une phrase. La 1re option porte « (Recommandé) ».
2. **Liens en bref** (choix multiple) : les 4 meilleurs sujets courts. Préciser que les autres restent dans le fichier de veille et qu'on peut en citer d'autres via « Autre ».

## Étape 3 — Recherche

En parallèle :
- le dossier complet sur le sujet de Rubrique choisi : `.claude/skills/newsletter-dossier/SKILL.md` ;
- les fiches des Liens en bref retenus : `.claude/skills/newsletter-brefs/SKILL.md` ;
- la génération des questions du jour liées à l'actu de la semaine : `.claude/skills/question-du-jour/SKILL.md`, mode `generer actu`.

Puis la question du jour (mode `choisir` du même fichier).

## Étape 4 — Récap

Écris `newsletter/numeros/AAAA-MM-JJ.md` :

```markdown
# Numéro du JJ/MM/AAAA — préparation

## Rubrique : <sujet>
Angle le plus fort : … — note : newsletter/dossiers/<fichier>.md

## Liens en bref
1. **<Sujet>** ✅ — le fait en une ligne — fiche : newsletter/brefs/<fichier>.md

## Question du jour
<id> — <question> (<format>)
```

Termine dans le chat par : la rubrique et son angle recommandé, les liens en bref validés (avec ⚠️/❌ si besoin), et les chemins des fichiers. Ne rédige rien : l'utilisateur écrit lui-même à partir des notes.
