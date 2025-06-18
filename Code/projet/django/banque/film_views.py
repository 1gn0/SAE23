from django.shortcuts import render, get_object_or_404, redirect
from .forms import FilmForm, CommentaireForm
from . import models

def ajout(request, id):
    """Ajout d'un film à une catégorie donnée (id = id de la catégorie)"""
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            objet = form.save(commit=False)
            objet.categorie = models.Categorie_Film.objects.get(id=id)
            objet.save()
            return redirect(f"/banque/Film/stock_film/{id}/")
        else:
            return render(request, "banque/film/ajout_film.html", {"form": form, "id": id})
    else:
        form = FilmForm()
        return render(request, "banque/film/ajout_film.html", {"form": form, "id": id})

def traitement(request, id):
    form = FilmForm(request.POST, request.FILES)
    if form.is_valid():
        film = form.save(commit=False)
        film.categorie = models.Categorie_Film.objects.get(id=id)
        film.save()
        return redirect(f"/banque/Film/stock_film/{id}/")
    else:
        return render(request, "banque/film/ajout_film.html", {"form": form, "id": id})

def affiche_all(request):
    list_data = list(models.Film.objects.all())
    return render(request, "banque/film/all_film.html", {"liste": list_data})

def modifier(request, id):
    film = get_object_or_404(models.Film, id=id)
    form = FilmForm(instance=film)
    return render(request, "banque/film/modifier_film.html", {"form": form, "id": id})

def sauvegarder_modif(request, id):
    film = get_object_or_404(models.Film, id=id)
    form = FilmForm(request.POST, request.FILES, instance=film)
    if form.is_valid():
        form.save()
        return redirect(f"/banque/Categorie_Film/stock_categorie_film/{film.categorie.id}/")
    return render(request, "banque/film/modifier_film.html", {"form": form, "id": id})

def supprimer(request, id):
    film = get_object_or_404(models.Film, id=id)
    if request.method == "POST":
        cat_id = film.categorie.id
        film.delete()
        return redirect(f"/banque/Categorie_Film/stock_categorie_film/{cat_id}/")
    return render(request, "banque/film/supprimer_film.html", {"film": film})

def stock(request, id):
    categorie = get_object_or_404(models.Categorie_Film, id=id)
    list_data = models.Film.objects.filter(categorie=categorie)
    return render(request, "banque/film/stock_film.html", {"liste": list_data, "categorie": categorie})

from . import models

def details_film(request, id):
    film = get_object_or_404(models.Film, id=id)
    acteurs = film.acteurs.all()  
    commentaires = models.Commentaire.objects.filter(film=film).order_by('-date')  
    notes_filtrees = [c.note for c in commentaires if c.note <= 5]
    if notes_filtrees:
        moyenne = sum(notes_filtrees) / len(notes_filtrees)
    else:
        moyenne = 0
    return render(request, 'banque/film/details_film.html', {
        'film': film,
        'acteurs': acteurs,
        'commentaires': commentaires,
        'moyenne': moyenne
    })
