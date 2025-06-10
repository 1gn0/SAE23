from django.shortcuts import render
from .forms import CommentaireForm
<<<<<<< HEAD
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
=======
from . import models
>>>>>>> 098ee0ac360b3761a44810ecc0d5ed569efcfd07
