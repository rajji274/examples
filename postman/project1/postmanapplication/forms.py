from django.forms import forms
from . models import registration
from django import forms
class registartionform(forms.ModelForm):

    class Meta:
        model=registration
        fields="__all__"

    