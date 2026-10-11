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

Lis toujours `newsletter/config.md` et `utilisees.md` avant d'agir.
L'historique des anciens numéros est dans le dossier indiqué dans la config (section « Historique »), sinon dans `newsletter/historique/`.
Si `utilisees.md` est vide et que l'historique contient d'anciens numéros, remplis-le d'abord avec toutes les questions du jour déjà publiées (une ligne par question, avec la date du numéro), et note les 10 qui ont visiblement le mieux marché si l'historique le montre (résultats de sondage, réponses citées).

## `generer [actu|intemporel] [nombre]`

Par défaut : 10 actu + 40 intemporelles par appel (la bibliothèque grossit à chaque numéro, sans gros lot coûteux).

- **Intemporel** : fais-le toi-même, sans sous-agent, en tournant sur les catégories adaptée à la thématique de la config (ex. métier, habitudes, futur, dilemmes, culture, souvenirs, opinions tranchées, « tu préfères… »). Dédoublonne contre les fichiers existants.
- **Actu** : pars uniquement de la veille la plus récente dans `newsletter/veille/` (pas de recherche web). Une question par sujet fort, avec une date d'expiration (sujet chaud : 7 jours ; tendance de fond : 30 jours).

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
