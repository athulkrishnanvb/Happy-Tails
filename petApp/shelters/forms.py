from django import forms
from.models import Shelter

class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ['name','address','contact_info']
        widgets = {

        }