from django.db import models
import bleach

class Categorie_Film(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length = 100)
    def __str__(self):
        chaine = f"Son nom est : {self.nom} ayant comme sdescriptif : {self.descriptif}."
        return chaine


class Film(models.Model):
    titre = models.CharField(max_length=100)
    annee_sortie = models.DateField(max_length = 100)
    affiche = models.ImageField(blank=True, null = True)
    realisateur = models.CharField(blank=True, null = True)
    categorie = models.CharField(max_length=100)
    def __str__(self):
        chaine = f"Son titre est : {self.titre},sorti en : {self.sortie} et ayant comme affiche : {self.affiche}, le réalisateur est : {self.realisateur} et ayant comme catégorie : {self.categorie}."
        return chaine
    
class Acteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length = 100)
    age = models.IntegerField(max_length = 100)
    photos = models.ImageField(blank=True, null = True)
    def __str__(self):
        chaine = f"Son nom est : {self.nom} et son prenom : {self.prenom}, ayant : {self.age} ans et comme photos : {self.photos}."
        return chaine
    
class Personne(models.Model):
    pseudo = models.CharField(max_length=100)
    nom_prenom = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    type = models.CharField(max_length = 100)
    def __str__(self):
        chaine = f"Son pseudo est : {self.nom} ayant comme sdescriptif : {self.descriptif}."
        return chaine

class Commentaire(models.Model):
    film = models.CharField(max_length=100)
    personnes = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    commentaire = models.CharField(max_length=100)
    date = models.CharField(max_length = 100)
    def __str__(self):
        chaine = f"Le film est : {self.film} et ayant comme personnes : {self.personnes}, ayant comme note : {self.note}, a comme commentaire : {self.commentaire} et ayant comme date : {self.date}"
        return chaine
