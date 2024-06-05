from django.shortcuts import render,redirect
from.models import Shelter
from.forms import ShelterForm
from Account_lo.views import homepage
from django.contrib.auth.models import User

# Create your views here.

def shelter_add(request):
    if request.method == 'POST':
        form = ShelterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homepage)
        
    else:
        form = ShelterForm()
    # users = User.objects.all()
    return render(request, 'add_shelter.html', {'form': form})
