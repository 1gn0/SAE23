from django.shortcuts import render
from .forms import FilmForm
from . import models

from .models import Categorie_Film
# Create your views here.

def ajout(request):
    
    if request.method == "POST": 
        form = Categorie_FilmForm(request)
        if form.is_valid():
            Categorie_Film= form.save() 
            list_data = list(models.Categorie_Film.objects.all())
            return render(request, "banque/Categorie/all_categorie.html", {"liste" : list_data})
        else:
            return render(request,"banque/Categorie/ajout_categorie.html",{"form": form})
    else :
        form = Categorie_FilmForm() 
        return render(request,"banque/Categorie/ajout_categorie.html",{"form" : form})
        