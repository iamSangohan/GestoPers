from django.conf import settings
from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import login, authenticate

def pageIndex(request):
    return render(request, 'authentification/index.html')

# def pageConnexion(request):
#     form = connexionForm()
#     if request.method == 'POST':
#         form = connexionForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('accueil')
#     return render(request, 'authentification/connexion.html', context={'form': form})     

#@login_required
def page_accueil(request):
    return render(request, 'authentification/accueil.html')

def page_inscription(request):
    form = forms.AjouterPersonnel()
    if request.method == 'POST':
        form = forms.AjouterPersonnel(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/ajouter_personnel.html', context={'form': form})