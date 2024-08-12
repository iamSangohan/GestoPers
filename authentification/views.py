from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import logout, authenticate


def pageIndex(request):
    if request.user.is_authenticated:
        return redirect('accueil')

    return render(request, 'authentification/index.html')

@login_required
def deconnexion(request):
    logout(request)
    return redirect('login')

@login_required
def page_ajout(request):
    return render(request, 'authentification/ajouter.html',)

@login_required
def page_ajout_personnel(request):
    form = forms.AjouterPersonnel()
    if request.method == 'POST':
        form = forms.AjouterPersonnel(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/ajouter_personnel.html', context={'form': form})

def page_ajout_departement(request):
    form = forms.AjouterDepartement()
    if request.method == 'POST':
        form = forms.AjouterDepartement(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/ajouter_personnel.html', context={'form': form})
        