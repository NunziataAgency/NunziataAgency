# Atelier newsletter

Un workflow Claude Code pour préparer chaque numéro :

```
Gmail (toutes tes newsletters)
        │  /newsletter-veille
        ▼
Short-list notée ── Lien en bref (infos courtes et croustillantes)
                └─ Rubrique (sujets à traiter en long)
        │  tu choisis
        ▼
/newsletter-dossier ── 5 recherches en parallèle :
   presse · X/Twitter · autres newsletters · sources primaires · avis contraires
        ▼
Dossier : l'essentiel, chronologie, chiffres sourcés, débat,
3 à 5 angles (dont ceux déjà pris ailleurs), plan proposé
```

## Les commandes

| Commande | Ce qu'elle fait |
|---|---|
| `/newsletter` | Tout le workflow : veille → tu choisis → recherches → récap du numéro |
| `/newsletter-veille 7` | Seulement la veille Gmail sur 7 jours |
| `/newsletter-dossier <sujet>` | Le tour complet d'un sujet + angles proposés |
| `/newsletter-dossier <sujet> --bref` | Vérifie une info courte et rédige le Lien en bref |

## Avant la première utilisation

1. **Connecter Gmail** : claude.ai → Paramètres → Connecteurs → Gmail, puis l'activer dans la conversation.
2. **Remplir `config.md`** : thématique, lectorat, ton, libellé Gmail des newsletters, comptes X à suivre.
   Astuce : un libellé Gmail « Newsletters » (avec un filtre automatique) rend la veille bien plus fiable.

## Où vont les résultats

- `veille/` : la short-list de chaque semaine
- `dossiers/` : un dossier par sujet creusé
- `numeros/` : le récap de préparation de chaque numéro

## Limites à connaître

- **X/Twitter** : pas d'accès à l'API X, la recherche passe par le web (`site:x.com`). Les posts très récents ou peu relayés peuvent manquer.
- **Newsletters payantes** : seul ce qui est dans l'e-mail est lu ; les articles derrière paywall ne sont pas accessibles.
- Les faits sont vérifiés et sourcés, mais relis toujours les chiffres clés avant publication.
