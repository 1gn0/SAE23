from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class Categorie_FilmForm(ModelForm):
    class Meta:
        model = models.Categorie_Film
        fields = ('nom', 'descriptif')
        labels = {
            'nom' : _('nom') ,
            'descriptif' : _('descriptif'),
        }

class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('titre', 'annee_sortie', 'affiche', 'realisateur', 'categorie')
        labels = {
            'titre': _('titre'),
            'annee_sortie': _('annee_sortie'),
            'affiche': _('affiche'),
            'realisateur': _('realisateur'),
            'categorie': _('categorie'),
        }


class ActeurForm(ModelForm):
    class Meta:
        model = models.Acteur
        fields = ('nom', 'prenom', 'age','photos')
        labels = {
            'nom' : _('nom') ,
            'prenom' : _('prenom'),
            'age' : _('age'),
            'photos' : _('photos'),
        }

class PersonneForm(ModelForm):
    class Meta:
        model = models.Personne
        fields = ('pseudo', 'nom_prenom', 'mail','mot_de_passe','type')
        labels = {
            'pseudo' : _('pseudo') ,
            'nom_prenom' : _('nom_prenom'),
            'mail' : _('mail'),
            'mot_de_passe' : _('mot_de_passe'),
            'type' : _('type'),
        }

class CommentaireForm(ModelForm):
    class Meta:
        model = models.Commentaire
        fields = ('note', 'commentaire')  
        labels = {
            'note': _('note'),
            'commentaire': _('commentaire')
        }
