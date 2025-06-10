from django.shortcuts import render
from .forms import FilmForm
from . import models

from .models import Film
# Create your views here.

def ajout(request):
    
    if request.method == "POST": 
        form = FilmForm(request)
        if form.is_valid():
            film= form.save() 
            list_data = list(models.Film.objects.all())
            return render(request,"banque/Film/ajout_film.html",{"form" : form})
        else :       
            return render(request,"banque/Film/ajout_film.html",{"form" : form})
        
def traitement(request, id):
    lform = FilmForm(request.POST)
    if lform.is_valid():
        film = lform.save()
        list_data = list(models.Film.objects.all())
        return render(request, "banque/Film/all_film.html", {"liste" : list_data})
    else:
        return render(request,"banque/Film/ajout_film.html",{"form": lform})

def affiche_all(request):
    list_data = list(models.Film.objects.all())
    return render(request, "banque/Film/all_film.html", {"liste" : list_data})

def modifier(request, id):
    categorie = models.Film.objects.get(id=id)
    lform = FilmForm(categorie.__dict__)
    return render(request, "banque/Film/modifier_film.html", {"lform" : lform, "id" : id})

def sauvegarder_modif(request, id):
    n_form = FilmForm(request.POST)
    if n_form.is_valid():
        sauvegarde = n_form.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        list_data = list(models.Magasin.objects.all())
        return render(request, "banque/Film/all_film.html", {"liste" : list_data})

def supprimer(request, id):
    film = models.Film.objects.get(id=id)
    lform = FilmForm(film.__dict__)
    return render(request, "banque/Film/supprimer_film.html", {"lform" : lform, "id" : id})

def stock(request, id):
    film = models.Film.objects.get(id=id)
    list_data = list(models.Film.objects.all())
    return render(request, "banque/Film/stock_film.html", {"liste" : list_data, "id" : id})
