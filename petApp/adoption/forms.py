from django import forms
from.models import AdoptionApplication

class AdoptionForm(forms.ModelForm):
    class Meta:
        fields = ['adoption_informaion']
