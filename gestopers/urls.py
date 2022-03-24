from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
import authentification.views
import gestion.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.pageIndex, name='index'),
    path('connexion/', LoginView.as_view(
        template_name = "authentification/connexion.html",
        redirect_authenticated_user = True
    ), name='connexion'),
    path('logout/', LogoutView.as_view(), name='deconnexion'),
    path('accueil/', gestion.views.page_accueil, name='accueil'),
    path('ajouter/', authentification.views.page_ajout, name='ajouter'),
    path('ajouter/Personnel/', authentification.views.page_ajout_personnel, name='ajouterPersonnel'),
    path('ajouter/Departement/', authentification.views.page_ajout_departement, name='ajouterDepartement'),
    path('departement/<slug:departement_nom>', gestion.views.page_departement, name='departement'),
    path('departement/<int:personnel_id>', gestion.views.page_personnel, name='personnel'),
]