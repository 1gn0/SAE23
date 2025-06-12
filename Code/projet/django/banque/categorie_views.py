from django.shortcuts import render
from .forms import Categorie_FilmForm
from . import models

from .models import Categorie_Film
# Create your views here.

def ajout(request):
    if request.method == "POST": 
        form = Categorie_FilmForm(request.POST)
        if form.is_valid():
            objet = form.save(commit=False)  
            objet.save()  
            list_data = list(models.Categorie_Film.objects.all())
            return render(request, "banque/categorie/ajout_categorie_film.html", {
                "liste": list_data,
                "form": form,
                "id": objet.id  
            })
        else:
            return render(request, "banque/categorie/ajout_categorie_film.html", {"form": form})
    else:
        form = Categorie_FilmForm()
        new_obj = models.Categorie_Film.objects.create(nom="")
        return render(request, "banque/categorie/ajout_categorie_film.html", {"form": form, "id": new_obj.id})
    
def traitement(request, id):
    lform = Categorie_FilmForm(request.POST)
    if lform.is_valid():
        Categorie = lform.save()
        list_data = list(models.Categorie_Film.objects.all())
        return render(request, "banque/categorie/all_categorie_film.html", {"liste" : list_data})
    else:
        return render(request,"banque/categorie/ajout_categorie_film.html",{"form": lform})

def affiche_all(request):
    list_data = list(models.Categorie_Film.objects.all())
    return render(request, "banque/categorie/all_categorie_film.html", {"liste" : list_data})

def modifier(request, id):
    categorie = models.Categorie_Film.objects.get(id=id)
    lform = Categorie_FilmForm(categorie.__dict__)
    return render(request, "banque/categorie/modifier_categorie_film.html", {"lform" : lform, "id" : id})

def sauvegarder_modif(request, id):
    n_form = Categorie_FilmForm(request.POST)
    if n_form.is_valid():
        sauvegarde = n_form.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        list_data = list(models.Categorie_Film.objects.all())
        return render(request, "banque/categorie/all_categorie_film.html", {"liste" : list_data})

def supprimer(request, id):
    categorie = models.Categorie_Film.objects.get(id=id)
    lform = Categorie_FilmForm(categorie.__dict__)
    return render(request, "banque/categorie/supprimer_categorie_film.html", {"lform" : lform, "id" : id})

def suppression(request, id):
    categorie = models.Categorie_Film.objects.get(id=id)
    categorie.delete()
    list_data = list(models.Categorie_Film.objects.all())
    return render(request, "banque/categorie/all_categorie_film.html", {"liste" : list_data})


def stock(request, id):
    categorie = models.Categorie_Film.objects.get(id=id)
    list_data = list(models.Categorie_Film.objects.all())
    return render(request, "banque/film/all_film.html", {"liste" : list_data, "id" : id})
