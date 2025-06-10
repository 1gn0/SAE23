from django.shortcuts import render
from .forms import CommentaireForm
from . import models

from .models import Commentaire
# Create your views here.

def ajout(request):
    
    if request.method == "POST": 
        form = CommentaireForm(request)
        if form.is_valid():
            Commentaire= form.save() 
            list_data = list(models.Commentaire.objects.all())
            return render(request, "banque/Commentaire/affiche_commentaire.html", {"liste" : list_data})
        else:
            return render(request,"banque/Commentaire/ajout_commentaire.html",{"form": form})
    else :
        form = CommentaireForm() 
        return render(request,"banque/Commentaire/commentaire.html",{"form" : form})
    
def traitement(request, id):
    lform = CommentaireForm(request.POST)
    if lform.is_valid():
        commentaire = lform.save()
        list_data = list(models.Commentaire.objects.all())
        return render(request, "banque/Commentaire/all_commentaire.html", {"liste" : list_data})
    else:
        return render(request,"banque/Commentaire/ajout_commentaire.html",{"form": lform})

def affiche_all(request):
    list_data = list(models.Commentaire.objects.all())
    return render(request, "banque/Commentaire/all_commentaire.html", {"liste" : list_data})

def modifier(request, id):
    commentaire = models.Commentaire.objects.get(id=id)
    lform = CommentaireForm(commentaire.__dict__)
    return render(request, "banque/Commentaire/modifier_commentaire.html", {"lform" : lform, "id" : id})

def sauvegarder_modif(request, id):
    n_form = CommentaireForm(request.POST)
    if n_form.is_valid():
        sauvegarde = n_form.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        list_data = list(models.Magasin.objects.all())
        return render(request, "banque/Commentaire/all_commentaire.html", {"liste" : list_data})

def supprimer(request, id):
    commentaire = models.Commentaire.objects.get(id=id)
    lform = CommentaireForm(commentaire.__dict__)
    return render(request, "banque/Commentaire/supprimer_commentaire.html", {"lform" : lform, "id" : id})

def stock(request, id):
    commentaire = models.Commentaire.objects.get(id=id)
    list_data = list(models.Commentaire.objects.all())
    return render(request, "banque/Commentaire/stock_commentaire.html", {"liste" : list_data, "id" : id})

