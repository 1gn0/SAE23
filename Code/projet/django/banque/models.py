from django.db import models

class Categorie_Film(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Film(models.Model):
    titre = models.CharField(max_length=100)
    annee_sortie = models.DateField()
    affiche = models.ImageField(blank=True, null=True, upload_to='affiches/')
    realisateur = models.CharField(blank=True, null=True, max_length=100)
    categorie = models.ForeignKey("Categorie_Film", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} ({self.annee_sortie}) par {self.realisateur} - Catégorie : {self.categorie.nom}"


class Acteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    photos = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"Son nom est : {self.nom}, prénom : {self.prenom}, âge : {self.age} ans, photo : {self.photos}."


class Personne(models.Model):
    pseudo = models.CharField(max_length=100)
    nom_prenom = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"Pseudo : {self.pseudo}, nom complet : {self.nom_prenom}"


class Commentaire(models.Model):
    film = models.CharField(max_length=100)
    personnes = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    commentaire = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    def __str__(self):
        return f"Film : {self.film}, personnes : {self.personnes}, note : {self.note}, commentaire : {self.commentaire}, date : {self.date}"
