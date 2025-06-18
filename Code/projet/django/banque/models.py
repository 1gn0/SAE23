from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class Categorie_Film(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Acteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    photos = models.ImageField(blank=True, null=True, upload_to='photos/')

    def __str__(self):
        return f"{self.prenom} {self.nom}, {self.age} ans"


class Film(models.Model):
    titre = models.CharField(max_length=100)
    annee_sortie = models.DateField()
    affiche = models.ImageField(blank=True, null=True, upload_to='affiches/')
    realisateur = models.CharField(blank=True, null=True, max_length=100)
    synopsis = models.TextField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie_Film, on_delete=models.CASCADE)
    acteurs = models.ManyToManyField(Acteur, related_name="films")

    def __str__(self):
        return f"{self.titre} ({self.annee_sortie.year})"


class Personne(models.Model):
    pseudo = models.CharField(max_length=100)
    nom_prenom = models.CharField(max_length=100)
    mail = models.EmailField()
    mot_de_passe = models.CharField(max_length=128)  
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pseudo} ({self.nom_prenom})"


class Commentaire(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="commentaires")
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="commentaires", null=True, blank=True)
    note = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.personne.pseudo} sur {self.film.titre} ({self.note}/5) : {self.commentaire[:30]}..."
