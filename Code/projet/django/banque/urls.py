from django.urls import path
from . import views

urlpatterns = [

    path('Acteur/modifier_acteur/<int:id>/', views.modifier_acteur),
    path('Acteur/supprimer_acteur/<int:id>/', views.supprimer_acteur),
    path('Acteur/ajout_acteur/', views.ajout_acteur),
    path('Acteur/affiche_acteur/<int:id>/', views.affiche_acteur),
    path('Acteur/traitement/', views.traitement_acteur),


    path('Categorie_Film/modifier_categorie_film/<int:id>/', views.modifier_categorie_film),
    path('Categorie_Film/supprimer_categorie_film/<int:id>/', views.supprimer_categorie_film),
    path('Categorie_Film/ajout_categorie_film/', views.ajout_categorie_film),
    path('Categorie_Film/affiche_categorie_film/<int:id>/', views.affiche_categorie_film),
    path('Categorie_Film/traitement/', views.traitement_categorie_film),

    path('Commentaire/modifier_commentaire/<int:id>/', views.modifier_commentaire),
    path('Commentaire/supprimer_commentaire/<int:id>/', views.supprimer_commentaire),
    path('Commentaire/ajout_commentaire/', views.ajout_commentaire),
    path('Commentaire/affiche_commentaire/<int:id>/', views.affiche_commentaire),
    path('Commentaire/traitement/', views.traitement_commentaire),


    path('Film/modifier_film/<int:id>/', views.modifier_film),
    path('Film/supprimer_film/<int:id>/', views.supprimer_film),
    path('Film/ajout_film/', views.ajout_film),
    path('Film/affiche_film/<int:id>/', views.affiche_film),
    path('Film/traitement/', views.traitement_film),


    path('Personne/modifier_personne/<int:id>/', views.modifier_personne),
    path('Personne/supprimer_personne/<int:id>/', views.supprimer_personne),
    path('Personne/ajout_personne/', views.ajout_personne),
    path('Personne/affiche_personne/<int:id>/', views.affiche_personne),
    path('Personne/traitement/', views.traitement_personne),


    path('main/', views.main),


]