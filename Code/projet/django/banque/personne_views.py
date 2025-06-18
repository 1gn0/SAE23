from django.shortcuts import render, redirect, reverse
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
    
def traitement(request, id):
    lform = PersonneForm(request.POST)
    if lform.is_valid():
        personne = lform.save()
        list_data = list(models.Personne.objects.all())
        return render(request, "banque/Personne/all_personne.html", {"liste" : list_data})
    else:
        return render(request,"banque/Personne/ajout_personne.html",{"form": lform})

def affiche_all(request):
    list_data = list(models.Personne.objects.all())
    return render(request, "banque/Personne/all_personne.html", {"liste" : list_data})

def modifier(request, id):
    categorie = models.Personne.objects.get(id=id)
    lform = PersonneForm(categorie.__dict__)
    return render(request, "banque/Film/modifier_film.html", {"lform" : lform, "id" : id})

def sauvegarder_modif(request, id):
    n_form = FilmForm(request.POST)
    if n_form.is_valid():
        sauvegarde = n_form.save(commit=False)
        sauvegarde.id = id
        sauvegarde.save()
        list_data = list(models.Magasin.objects.all())
        return render(request, "banque/Film/all_film.html", {"liste" : list_data})

def supprimer(request, id):
    film = models.Film.objects.get(id=id)
    lform = FilmForm(film.__dict__)
    return render(request, "banque/Film/supprimer_film.html", {"lform" : lform, "id" : id})

def stock(request, id):
    film = models.Film.objects.get(id=id)
    list_data = list(models.Film.objects.all())
    return render(request, "banque/Film/stock_film.html", {"liste" : list_data, "id" : id})

def login(request, film_id):
    creation_form = PersonneForm()

    if request.method == 'POST':
        if 'login_submit' in request.POST:
            mail = request.POST.get('mail')
            mot_de_passe = request.POST.get('mot_de_passe')

            try:
                personne = Personne.objects.get(mail=mail, mot_de_passe=mot_de_passe)
                return redirect(reverse('ajout_commentaire') + f'?personne_id={personne.id}&film_id={film_id}')
            except Personne.DoesNotExist:
                erreur_login = "Identifiants invalides."
                return render(request, 'banque/personne/login.html', {
                    'creation_form': creation_form,
                    'film_id': film_id,
                    'erreur_login': erreur_login
                })

        elif 'creation_submit' in request.POST:
            creation_form = PersonneForm(request.POST)
            if creation_form.is_valid():
                personne = creation_form.save()
                return redirect(reverse('ajout_commentaire') + f'?personne_id={personne.id}&film_id={film_id}')
    return render(request, 'banque/personne/login.html', {
        'creation_form': creation_form,
        'film_id': film_id
    })