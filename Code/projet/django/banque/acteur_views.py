from django.shortcuts import render
from .forms import ActeurForm
from . import models

from .models import Acteur
# Create your views here.

def ajout(request):
    
    if request.method == "POST": 
        form = ActeurForm(request.POST)
        if form.is_valid():
            Acteur= form.save() 
            list_data = list(models.Acteur.objects.all())
            return render(request, "banque/acteur/affiche_acteur.html", {"liste" : list_data})
        else:
            return render(request,"banque/acteur/ajout_acteur.html",{"form": form, "id" : id})
    else :
        form = ActeurForm() 
        return render(request,"banque/acteur/ajout_acteur.html",{"form" : form, "id" : id})
        

def traitement(request, id):
    Acteur = models.Acteur.objects.get(id=id)
    form = ActeurForm(request.POST)
    if form.is_valid():
        Acteur = form.save()
        list_data = list(models.Acteur.objects.all())
        return render(request, "banque/acteur/all_acteur.html", {"liste" : list_data})
    else:
        return render(request,"banque/acteur/ajout_acteur.html",{"form": form, "id" : id}) 

def affiche_all(request):
    list_data = list(models.Acteur.objects.all())
    return render(request, "banque/acteur/all_acteur.html", {"liste" : list_data})

def modifier(request, id):
    Acteur = models.Acteur.objects.get(id=id)
    lform = ActeurForm(Acteur.__dict__)
    return render(request, "banque/acteur/modifier_acteur.html", {"lform" : lform, "id" : id})

def sauvegarder_modif(request, id):
    n_form = ActeurForm(request.POST)
    if n_form.is_valid():
        sauvegarde = n_form.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        list_data = list(models.Acteur.objects.all())
        return render(request, "banque/acteur/all_acteur.html", {"liste" : list_data})

def supprimer(request, id):
    Acteur = models.Acteur.objects.get(id=id)
    lform = ActeurForm(Acteur.__dict__)
    return render(request, "banque/acteur/supprimer_acteur.html", {"lform" : lform, "id" : id})

def suppression(request, id):
    Acteur = models.Acteur.objects.get(id=id)
    Acteur.delete()
    list_data = list(models.Acteur.objects.all())
    return render(request, "banque/acteur/all_acteur.html", {"liste" : list_data})

