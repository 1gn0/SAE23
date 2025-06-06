from django.shortcuts import render
from .forms import PersonneForm
from . import models

from .models import Personne
# Create your views here.

def ajout(request):
    
    if request.method == "POST": 
        form = PersonneForm(request)
        if form.is_valid():
            Personne= form.save() 
            list_data = list(models.Personne.objects.all())
            return render(request, "banque/Personne/affiche_personne.html", {"liste" : list_data})
        else:
            return render(request,"banque/Personne/ajout_personne.html",{"form": form})
    else :
        form = PersonneForm() 
        return render(request,"banque/Personne/personne.html",{"form" : form})