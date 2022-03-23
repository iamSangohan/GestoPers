from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import DateInput


class User(AbstractUser):
    pass

class Departement(models.Model):
    nomDepartement = models.CharField(max_length=100)
    
class Personnel(models.Model):
    nom = models.CharField(max_length=30, null=False)
    prenom = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    date_arrivee = models.DateField()
    departement = models.ForeignKey(Departement, null= True, on_delete=models.SET_NULL)