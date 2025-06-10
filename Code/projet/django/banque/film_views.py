from django.shortcuts import render
from .forms import FilmForm
from . import models

from .models import Film
# Create your views here.

def ajout(request):
    
    if request.method == "POST": 
        form = FilmForm(request)
        if form.is_valid():
            Film= form.save() 
            list_data = list(models.Film.objects.all())
            return render(request, "banque/Film/affiche_film.html", {"liste" : list_data})
        else:
            return render(request,"banque/Film/ajout_film.html",{"form": form})
    else :
        form = FilmForm() 
        return render(request,"banque/Film/film.html",{"form" : form})