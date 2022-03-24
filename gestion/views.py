from authentification import models
from authentification.models import Personnel
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


@login_required
def page_accueil(request):
    personnel = Personnel.objects.all()
    
    return render(request, 'gestion/accueil.html', {'liste': personnel})

def page_departement(request, departement_nom):
    depart = get_object_or_404(models.Departement, nomDepartement=departement_nom)
    personDepart = Personnel.objects.filter(departement_id=depart.id)
    return render(request, 'gestion/departement.html', {'departement': depart, 'personnel': personDepart})
    
def page_personnel(request, personnel_id):
    pers = get_object_or_404(models.Personnel, id=personnel_id)
    return render(request, 'gestion/personnel.html', {'personnel': pers})