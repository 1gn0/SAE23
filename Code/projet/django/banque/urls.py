from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import categorie_views
from . import acteur_views
from . import film_views
from . import personne_views
from . import commentaire_views
from . import views 

urlpatterns = [

    # Acteur
    path('Acteur/modifier_acteur/<int:id>/', acteur_views.modifier, name="modifier_acteur"),
    path('Acteur/sauvegarder_acteur/<int:id>/', acteur_views.sauvegarder_modif, name="sauvegarder_acteur"),
    path('Acteur/supprimer_acteur/<int:id>/', acteur_views.supprimer, name="supprimer_acteur"),
    path('Acteur/suppression_acteur/<int:id>/', acteur_views.suppression, name="suppression_acteur"),
    path('Acteur/ajout_acteur/', acteur_views.ajout, name="ajout_acteur"),
    path('Acteur/affiche_acteur/<int:id>/', acteur_views.affiche_all, name="affiche_acteur"),
    path('Acteur/traitement/<int:id>/', acteur_views.traitement, name="traitement_acteur"),
    path('Acteur/all_acteur/', acteur_views.affiche_all, name="all_acteur"),

    # Catégorie
    path('Categorie_Film/modifier_categorie_film/<int:id>/', categorie_views.modifier, name="modifier_categorie_film"),
    path('Categorie_Film/sauvegarder_categorie_film/<int:id>/', categorie_views.sauvegarder_modif, name="sauvegarder_modif_categorie_film"),
    path('Categorie_Film/supprimer_categorie_film/<int:id>/', categorie_views.supprimer, name="supprimer_categorie_film"),
    path('Categorie_Film/suppression_categorie_film/<int:id>/', categorie_views.suppression, name="suppression_categorie_film"),
    path('Categorie_Film/ajout_categorie_film/', categorie_views.ajout, name="ajout_categorie_film"),
    path('Categorie_Film/all_categorie_film/', categorie_views.affiche_all, name="all_categorie_film"),
    path('Categorie_Film/traitement/<int:id>/', categorie_views.traitement, name="traitement_categorie_film"),
    path('Categorie_Film/stock_categorie_film/<int:id>/', categorie_views.stock, name="stock_categorie_film"),

    # Commentaire
    path('Commentaire/modifier_commentaire/<int:id>/', commentaire_views.modifier, name="modifier_commentaire"),
    path('Commentaire/supprimer_commentaire/<int:id>/', commentaire_views.supprimer, name="supprimer_commentaire"),
    path('Commentaire/ajout_commentaire/', commentaire_views.ajout, name="ajout_commentaire"),
    path('Commentaire/login/<int:film_id>/', personne_views.login, name="login_commentaire"),

    # Film
    path('Film/modifier_film/<int:id>/', film_views.modifier, name="modifier_film"),
    path('Film/supprimer_film/<int:id>/', film_views.supprimer, name="supprimer_film"),
    path('Film/ajout_film/<int:id>/', film_views.ajout, name="ajout_film"),
    path('Film/affiche_film/<int:id>/', film_views.affiche_all, name="affiche_film"),
    path('Film/traitement/<int:id>/', film_views.traitement, name="traitem,ent_film"),
    path('Film/stock_film/<int:id>/', film_views.stock, name="stock_film"),
    path('Film/details/<int:id>/', film_views.details_film, name='details_film'),
    path('film/<int:film_id>/ajouter_acteur_au_film/', acteur_views.ajouter_acteur_au_film, name='ajouter_acteur_au_film'),


    # Personne
    path('Personne/modifier_personne/<int:id>/', personne_views.modifier, name="modifier_personne"),
    path('Personne/supprimer_personne/<int:id>/', personne_views.supprimer, name="supprimer_personne"),
    path('Personne/ajout_personne/', personne_views.ajout, name="ajout_personne"),
    path('Personne/affiche_personne/<int:id>/', personne_views.affiche_all, name="affiche_personne"),
    path('Personne/traitement/', personne_views.traitement, name="traitement_personne"),
    

    # Index
    path('index/', views.index, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)