from django.shortcuts import render
from .forms import PersonneForm
from . import models

from .models import Personne
# Create your views here.

def ajout(request):
    if request.method == "POST": 
        form = PersonneForm(request)
        if form.is_valid():
            Personne= form.save() 
            list_data = list(models.Personne.objects.all())
            return render(request, "banque/Personne/affiche_personne.html", {"liste" : list_data})
        else:
            return render(request,"banque/Personne/ajout_personne.html",{"form": form})
    else :
        form = PersonneForm() 
        return render(request,"banque/Personne/personne.html",{"form" : form})
    
def traitement(request, id):
    lform = PersonneForm(request.POST)
    if lform.is_valid():
        personne = lform.save()
        list_data = list(models.Personne.objects.all())
        return render(request, "banque/Personne/all_personne.html", {"liste" : list_data})
    else:
        return render(request,"banque/Personne/ajout_personne.html",{"form": lform})

def affiche_all(request):
    list_data = list(models.Personne.objects.all())
    return render(request, "banque/Personne/all_personne.html", {"liste" : list_data})

def modifier(request, id):
    categorie = models.Personne.objects.get(id=id)
    lform = PersonneForm(categorie.__dict__)
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
