from dataclasses import fields
from tkinter import Widget
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'
       
class AjouterPersonnel(forms.ModelForm):
    class Meta:
        model = models.Personnel
        fields = '__all__'
        widgets = {
            'date_arrivee': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'type': 'date'}),
        }
        
class AjouterDepartement(forms.ModelForm):
    class Meta:
        model = models.Departement
        fields = '__all__'
        
class SupprimerDepartement(forms.Form):
    supDepart = forms.BooleanField(initial=True)