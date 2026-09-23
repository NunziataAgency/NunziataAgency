# Carnet de lectures

Site mobile pour retrouver tous les livres lus depuis 1988. Il est pensé pour une personne âgée atteinte de Parkinson : texte en grand, gros boutons espacés, aucun geste de glissement, et un double appui accidentel ne déclenche rien.

- `index.html` : le site (style estampe japonaise).
- `livres.json` : les livres du carnet (`lu` = année de lecture, `paru` = première parution).
- `nouveautes.json` : les dernières sorties des auteurs déjà lus (liste figée, à mettre à jour).

Pour l'essayer en local : `python3 -m http.server` dans ce dossier.
L'ajout et la correction de livres ne marchent que dans la version publiée sur claude.ai.
