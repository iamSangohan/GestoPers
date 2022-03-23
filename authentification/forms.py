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
        Widget = {
            'date_arrivee': DateInput,
        }