from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentaireForm
from . import models

from .models import Commentaire, Film, Personne
# Create your views here.

def ajout(request):
    personne_id = request.GET.get('personne_id')
    film_id = request.GET.get('film_id')

    if not personne_id or not film_id:
        return redirect('index')

    personne = get_object_or_404(Personne, id=personne_id)
    film = get_object_or_404(Film, id=film_id)

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.personne = personne
            commentaire.film = film
            commentaire.save()
            return redirect('details_film', id=film.id)
    else:
        form = CommentaireForm()

    return render(request, 'banque/commentaire/ajout_commentaire.html', {
        'form': form,
        'personne': personne,
        'film': film,
    })


def modifier(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)
    
    if request.method == 'POST':
        mail = request.POST.get('mail')
        mdp = request.POST.get('mot_de_passe')
        
        if commentaire.personne.mail == mail and commentaire.personne.mot_de_passe == mdp:
            form = CommentaireForm(request.POST, instance=commentaire)
            if form.is_valid():
                form.save()
                return redirect('details_film', id=commentaire.film.id)
        else:
            return render(request, 'banque/commentaire/modifier_commentaire.html', {
                'form': CommentaireForm(instance=commentaire),
                'erreur': "Accès refusé, identifiants incorrects.",
                'id': id
            })
    else:
        form = CommentaireForm(instance=commentaire)
        return render(request, 'banque/commentaire/modifier_commentaire.html', {
            'form': form,
            'id': id
        })


def supprimer(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)

    if request.method == 'POST':
        mail = request.POST.get('mail')
        mdp = request.POST.get('mot_de_passe')

        if commentaire.personne.mail == mail and commentaire.personne.mot_de_passe == mdp:
            film_id = commentaire.film.id
            commentaire.delete()
            return redirect('details_film', id=film_id)
        else:
            return render(request, 'banque/commentaire/supprimer_commentaire.html', {
                'erreur': "Identifiants invalides, suppression refusée.",
                'id': id
            })
    return render(request, 'banque/commentaire/supprimer_commentaire.html', {'id': id})
