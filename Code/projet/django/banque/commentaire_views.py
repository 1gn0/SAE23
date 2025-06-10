from django.shortcuts import render
from .forms import CommentaireForm
from . import models

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
            return render(requegst,"banque/Commentaire/ajout_commentaire.html",{"form": form})
    else :
        form = CommentaireForm() 
        return render(request,"banque/Commentaire/commentaire.html",{"form" : form})

def traitement(request, id):
    film = models.Film.objects.get(id=id)
    form = GuitareForm(request.POST)
    if form.is_valid():
        commentaire = form.save(commit=False)
        commentaire.film = film
        commentaire.save()
        return redirect('stock', id=commentaire.id)
    else:
        return render(request, "banque/commentaire/ajout.html", {"form": form, "id": id})


def read(request, id):
    film = models.Film.objects.get(id=id)
    return render(request, "banque/commentaire/affiche_commentaire.html", {"film" : film})