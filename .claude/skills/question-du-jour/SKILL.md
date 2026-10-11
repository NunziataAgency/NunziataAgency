---
name: question-du-jour
description: Gère la grande bibliothèque de « questions du jour » de la newsletter — en génère des centaines (liées à l'actu ou intemporelles), sans doublon avec les anciens numéros, et en propose une sélection au choix. À utiliser quand on demande des questions du jour, d'enrichir la bibliothèque ou de choisir la question d'un numéro.
argument-hint: "generer [actu|intemporel] [nombre] | choisir | utilisee <id>"
---

# Bibliothèque de questions du jour

Fichiers :
- `newsletter/questions/actu.md` — questions liées à l'actualité (elles périment : chacune a une date de fin).
- `newsletter/questions/intemporel.md` — questions qui marchent n'importe quand.
- `newsletter/questions/utilisees.md` — questions déjà publiées (avec la date du numéro).

Format d'une ligne (tableau Markdown) :
`| id | question | format | catégorie | note | statut |`
- **id** : `A-0001` (actu) ou `I-0001` (intemporel), jamais réutilisé.
- **format** : sondage (avec les options), quiz (avec la réponse + 1 phrase d'anecdote), ouverte.
- **note** : potentiel de réponses/engagement sur 10.
- **statut** : `dispo` · `choisie JJ/MM` · pour l'actu, `expire JJ/MM`.

Lis toujours `newsletter/config.md`, `newsletter/style.md` s'il existe, et `utilisees.md` avant d'agir.
Si `utilisees.md` est vide et que `newsletter/historique/` contient d'anciens numéros, remplis-le d'abord avec toutes les questions du jour déjà publiées (une ligne par question, avec la date du numéro), et note les 10 qui ont visiblement le mieux marché si l'historique le montre (résultats de sondage, réponses citées).

## `generer [actu|intemporel] [nombre]`

Par défaut : les deux, 50 actu + 200 intemporelles. Vise une bibliothèque de **500+ intemporelles** au total.

- **Intemporel** : répartis le travail entre 4 à 6 sous-agents (Agent), un par grande catégorie adaptée à la thématique de la config (ex. métier, habitudes, futur, dilemmes, culture, souvenirs, opinions tranchées, « tu préfères… »). Donne à chacun la config, le style et la liste des questions existantes pour éviter les doublons.
- **Actu** : pars de la veille la plus récente dans `newsletter/veille/` et des dossiers, plus une recherche web des sujets de la semaine. Une question par sujet fort, avec une date d'expiration (sujet chaud : 7 jours ; tendance de fond : 30 jours).

Une bonne question du jour :
- se lit en une seconde et donne envie de répondre tout de suite ;
- divise (pour un sondage, des options équilibrées, aucune « bonne » réponse évidente) ;
- est en lien avec le lectorat, pas une question de culture générale vague ;
- respecte le ton de la newsletter ;
- n'est ni blessante ni piégeuse, et ne demande pas de données personnelles sensibles.

Dédoublonne (même idée formulée autrement = doublon) contre les trois fichiers, numérote à la suite, ajoute, puis donne le nouveau total par fichier.

## `choisir`

1. Marque `expire` les questions actu dont la date est passée.
2. Propose avec AskUserQuestion **4 options** : 2 actu (les mieux notées et non expirées, en lien avec le numéro en cours si possible) et 2 intemporelles (catégories différentes de celles des 3 derniers numéros). L'utilisateur peut en citer une autre via « Autre » (par son id).
3. Passe la question retenue en `choisie JJ/MM`.

## `utilisee <id>`

Déplace la question vers `utilisees.md` avec la date du jour.
