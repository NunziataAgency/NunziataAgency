# Atelier newsletter

Un workflow Claude Code pour préparer chaque numéro :

```
Gmail (toutes tes newsletters)
        │  /newsletter-veille
        ▼
Grosse liste numérotée ── B1…B60 Lien en bref (infos courtes et croustillantes)
                       └─ R1…R30 Rubrique (sujets à traiter en long)
        │  tu choisis
        ▼
/newsletter-dossier ── 5 recherches en parallèle :
   presse · X/Twitter · autres newsletters · sources primaires · avis contraires
        ▼
Note de synthèse pour écrire à la main : l'essentiel, chronologie,
chiffres et citations sourcés, débat, angles (dont ceux déjà pris
ailleurs) et le stock complet d'articles avec liens
```

- **Liens en bref** : tu choisis dans une grosse liste, le système les vérifie et les **rédige**.
- **Rubriques** : tu choisis, le système fait la recherche et te livre une **note de synthèse** ; c'est toi qui écris.

## Les commandes

| Commande | Ce qu'elle fait |
|---|---|
| `/newsletter` | Tout le workflow : veille → tu choisis → recherches → récap du numéro |
| `/newsletter-veille 7` | Seulement la veille Gmail sur 7 jours |
| `/newsletter-dossier <sujet>` | Le tour complet d'un sujet + angles proposés |
| `/newsletter-brefs B1 B4…` | Vérifie et rédige les Liens en bref choisis, prêts à coller |
| `/question-du-jour generer` | Enrichit la bibliothèque : questions liées à l'actu + intemporelles |
| `/question-du-jour choisir` | Te propose 4 questions, tu choisis |

## Installation sur Mac (une seule fois)

1. **Installer Claude Code** : ouvre l'app **Terminal** et colle :
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
   (Ou utilise l'onglet **Code** de l'app Claude pour Mac, téléchargeable sur claude.ai/download.)
2. **Récupérer le système** dans ton dossier Documents :
   ```
   cd ~/Documents
   git clone -b claude/newsletter-workflow-analysis-5wqo54 https://github.com/NunziataAgency/NunziataAgency.git
   ```
   Si le Mac te propose d'installer les « outils de ligne de commande », accepte puis relance la commande.
3. **Connecter Gmail** : sur claude.ai → Paramètres → Connecteurs → Gmail → Connecter.
4. **Lancer** :
   ```
   cd ~/Documents/NunziataAgency
   claude
   ```
   Connecte-toi avec ton compte Claude, puis tape `/mcp` pour vérifier que Gmail apparaît.
   Dans l'app Claude : onglet **Code** → choisir le dossier `Documents/NunziataAgency`.
5. **Brancher ton historique** : dans `newsletter/config.md`, indique le dossier de ton Mac où sont tes anciens numéros (ex. `~/Documents/Ma newsletter`). Pas besoin de les déplacer.
6. **Remplir le reste de `config.md`** : thématique, lectorat, ton, libellé Gmail des newsletters, comptes X à suivre.
   Astuce : un libellé Gmail « Newsletters » (avec un filtre automatique) rend la veille bien plus fiable.

Ensuite, chaque semaine : ouvre le dossier, lance `claude`, tape `/newsletter`.

## Où vont les résultats

- `veille/` : la short-list de chaque semaine
- `dossiers/` : un dossier par sujet creusé
- `brefs/` : les Liens en bref rédigés
- `questions/` : la bibliothèque de questions du jour (actu, intemporel, déjà utilisées)
- `numeros/` : le récap de préparation de chaque numéro

## Limites à connaître

- **X/Twitter** : pas d'accès à l'API X, la recherche passe par le web (`site:x.com`). Les posts très récents ou peu relayés peuvent manquer.
- **Newsletters payantes** : seul ce qui est dans l'e-mail est lu ; les articles derrière paywall ne sont pas accessibles.
- Les faits sont vérifiés et sourcés, mais relis toujours les chiffres clés avant publication.
