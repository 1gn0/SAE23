from django.shortcuts import render
from .forms import Categorie_FilmForm
from . import models

from .models import Categorie_Film
# Create your views here.

def ajout(request):
    
    if request.method == "POST": 
        form = Categorie_FilmForm(request)
        if form.is_valid():
            Categorie_Film= form.save() 
            list_data = list(models.Categorie_Film.objects.all())
            return render(request,"banque/Categorie/ajout_categorie.html",{"form" : form})
        else :       
            return render(request,"banque/Categorie/ajout_categorie.html",{"form" : form})
        
def traitement(request, id):
    lform = Categorie_FilmForm(request.POST)
    if lform.is_valid():
        categorie = lform.save()
        list_data = list(models.Categorie_Film.objects.all())
        return render(request, "banque/Categorie/all_categorie.html", {"liste" : list_data})
    else:
        return render(request,"banque/Categorie/ajout_categorie.html",{"form": lform})

def affiche_all(request):
    list_data = list(models.Categorie_Film.objects.all())
    return render(request, "banque/Categorie/all_categorie.html", {"liste" : list_data})

def modifier(request, id):
    categorie = models.Categorie_Film.objects.get(id=id)
    lform = Categorie_FilmForm(categorie.__dict__)
    return render(request, "banque/Categorie/modifier_categorie.html", {"lform" : lform, "id" : id})

def sauvegarder_modif(request, id):
    n_form = Categorie_FilmForm(request.POST)
    if n_form.is_valid():
        sauvegarde = n_form.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        list_data = list(models.Magasin.objects.all())
        return render(request, "banque/Categorie/all_categorie.html", {"liste" : list_data})

def supprimer(request, id):
    categorie = models.Categorie_Film.objects.get(id=id)
    lform = Categorie_FilmForm(categorie.__dict__)
    return render(request, "banque/Categorie/supprimer_categorie.html", {"lform" : lform, "id" : id})

def stock(request, id):
    categorie = models.Categorie_Film.objects.get(id=id)
    list_data = list(models.Categorie_Film.objects.all())
    return render(request, "banque/Categorie/stock_categorie.html", {"liste" : list_data, "id" : id})
