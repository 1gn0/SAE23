### Organisation des pages html du projet

###### index.html

- Page d'accueil du projet
- Contient un menu de navigation
- Contient un lien d'accès vers la page de liste des films
- sert de template au reste des pages

Le dossier templates contient 5 dossiers en fonction des CRUD nécessaires au fonctionnement de l'application. 

Pour chaque dossier, on peut retrouver les fichiers html suivants : 

###### affiche.html

Permet d'afficher les informations d'une entité, cette page n'est pas nécessaire pour tout les CRUD

###### ajout.html

Contient le formulaire d'ajout d'une entité, est nécessaire pour tout les CRUD

###### modifier.html

Permet de modifier les informations d'une entité, est nécessaire pour tout les CRUD
Est basé sur le formulaire d'ajout

###### supprimer.html

Permet de supprimer une entité, est nécessaire pour tout les CRUD

###### afficher_all.html

Permet d'afficher l'ensemble des entités d'une table, peut avoir besoin d'un id pour afficher par ex : 
- tout les films d'un acteur
- tout les films d'un genre
- tout les commentaires d'un film