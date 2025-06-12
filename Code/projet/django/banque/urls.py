from django.urls import path
from . import categorie_views
from . import acteur_views
from . import film_views
from . import personne_views
from . import commentaire_views
from . import views 

urlpatterns = [

    path('Acteur/modifier_acteur/<int:id>/', acteur_views.modifier),
    path('Acteur/supprimer_acteur/<int:id>/', acteur_views.supprimer),
    path('Acteur/ajout_acteur/', acteur_views.ajout),
    path('Acteur/affiche_acteur/<int:id>/', acteur_views.affiche_all),
    path('Acteur/traitement/', acteur_views.traitement),

    path('Categorie_Film/modifier_categorie_film/<int:id>/', categorie_views.modifier),
    path('Categorie_Film/sauvegarder_categorie_film/<int:id>/', categorie_views.sauvegarder_modif),
    path('Categorie_Film/supprimer_categorie_film/<int:id>/', categorie_views.supprimer),
    path('Categorie_Film/suppression_categorie_film/<int:id>/', categorie_views.suppression),
    path('Categorie_Film/ajout_categorie_film/', categorie_views.ajout),
    path('Categorie_Film/all_categorie_film/', categorie_views.affiche_all),
    path('Categorie_Film/traitement/<int:id>/', categorie_views.traitement),
    path('Categorie_Film/stock_categorie_film/<int:id>/', categorie_views.stock),

    path('Commentaire/modifier_commentaire/<int:id>/', commentaire_views.modifier),
    path('Commentaire/supprimer_commentaire/<int:id>/', commentaire_views.supprimer),
    path('Commentaire/ajout_commentaire/', commentaire_views.ajout),
    path('Commentaire/affiche_commentaire/<int:id>/', commentaire_views.affiche_all),
    path('Commentaire/traitement/', commentaire_views.traitement),


    path('Film/modifier_film/<int:id>/', film_views.modifier),
    path('Film/supprimer_film/<int:id>/', film_views.supprimer),
    path('Film/ajout_film/', film_views.ajout),
    path('Film/affiche_film/<int:id>/', film_views.affiche_all),
    path('Film/traitement/', film_views.traitement),


    path('Personne/modifier_personne/<int:id>/', personne_views.modifier),
    path('Personne/supprimer_personne/<int:id>/', personne_views.supprimer),
    path('Personne/ajout_personne/', personne_views.ajout),
    path('Personne/affiche_personne/<int:id>/', personne_views.affiche_all),
    path('Personne/traitement/', personne_views.traitement),


    path('index/', views.index, name="index"),


]