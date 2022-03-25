from django.template import Library
from authentification.models import Personnel

register = Library()

@register.filter
def nbrePersonnel(value):
    persoDepart = Personnel.objects.filter(departement_id = value.id)
    nbPers = persoDepart.count()
    return nbPers