from django.shortcuts import render
from .forms import CommentaireForm
<<<<<<< HEAD
<<<<<<< HEAD
=======
from . import models

from django.shortcuts import render
from .forms import CommentaireForm
>>>>>>> 8d26062502397acc8161227b8fb45723d01d325b
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
<<<<<<< HEAD
            return render(request,"banque/Commentaire/ajout_commentaire.html",{"form": form})
    else :
        form = CommentaireForm() 
        return render(request,"banque/Commentaire/commentaire.html",{"form" : form})
=======
from . import models
>>>>>>> 098ee0ac360b3761a44810ecc0d5ed569efcfd07
=======
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
<<<<<<< HEAD
>>>>>>> 8d26062502397acc8161227b8fb45723d01d325b
=======

def modifier(request, id):
    commentaire = models.Commentaire.objects.get(id=id)
    lform = CommentaireForm(commentaire.__dict__)
    return render(request, "banque/commentaire/modifier_commentaire.html", {"lform" : lform, "id" : id})

def sauvegarder_modif(request, id):
    n_form = CommentaireForm(request.POST)
    if n_form.is_valid():
        sauvegarde = n_form.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        list_data = list(models.Film.objects.all())
        return render(request, "banque/commentaire/all_commentaire.html", {"liste" : list_data})

def supprimer(request, id):
    commentaire = models.Commentaire.objects.get(id=id)
    if n_form.is_valid():
        sauvegarde = n_form.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        list_data = list(models.Film.objects.all())
        return render(request, "banque/commentaire/all_commentaire.html", {"liste" : list_data})

def suppression(request, id):
    commentaire = models.Commentaire.objects.get(id=id)
    commentaire.delete()
    list_data = list(models.Film.objects.all())
    return render(request, "banque/commentaire/all_commentaire.html", {"liste" : list_data})
>>>>>>> 2e34b2ca496337786251209473e6095307066b5a
