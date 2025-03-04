from dataclasses import fields
from xml.parsers.expat import model
from django.forms import ModelForm,TextInput

from . models import Weatherdetails
class Weatherform(ModelForm):
    class Meta:
        model=Weatherdetails
        fields=['city','temperature','description','humidity','pressure','country','sunrise','sunset','windspeed']
