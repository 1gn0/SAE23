from django.shortcuts import render
from .forms import FilmForm
from . import models

from .models import Acteur
# Create your views here.

def ajout(request):
    
    if request.method == "POST": 
        form = ActeurForm(request)
        if form.is_valid():
            Acteur= form.save() 
            list_data = list(models.Acteur.objects.all())
            return render(request, "banque/Acteur/affiche_acteur.html", {"liste" : list_data})
        else:
            return render(request,"banque/Acteur/ajout_cacteur.html",{"form": form})
    else :
        form = ActeurForm() 
        return render(request,"banque/Acteur/acteur.html",{"form" : form})
        