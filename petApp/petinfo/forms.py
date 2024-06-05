from django import forms
from.models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['photo','name','breed','age','gender','health_status','description','available']
        widgets = {
            
        }