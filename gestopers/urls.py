from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
import authentification.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.pageIndex, name='index'),
    path('connexion/', LoginView.as_view(
        template_name = "authentification/connexion.html",
        redirect_authenticated_user = True
    ), name='connexion'),
    path('accueil/', authentification.views.page_accueil, name='accueil'),
    path('ajouterPersonnel/', authentification.views.page_inscription, name='ajouterPersonnel'),
]