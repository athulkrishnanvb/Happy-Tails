from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from.models import AdoptionApplication
from petinfo.models import Pet
from shelters.models import Shelter
from.forms import AdoptionForm

# Create your views here.

# @login_required(login_url='/Account/login_view/')
def adopt_pet(request, id):
    pet = get_object_or_404(Pet, id=id)

    if request.method=='POST':
        application=AdoptionApplication.objects.create(
            user = request.user,
            pet=pet,
            status = 'submitted'
        )

        pet.available=False
        pet.save()
        return render(request, 'not_avail.html', {'pet':pet, 'status':'submitted'})
    return render(request, 'adopt_pet.html', {'pet':pet})

def contact_shelter(request):
    shelter_id = request.GET.get('shelter_id')
    shelter = get_object_or_404(Shelter, id=shelter_id)
    context = {
        'shelter': shelter
    }
    return render(request, 'contact_s.html', context)


    
    # if request.method=='POST':
    #     form = AdoptionForm(request.POST)
    #     if form.is_valid():
    #         adoption = form.save(commit=False)
    #         adoption.pet = pet
    #         adoption.user = request.user
    #         adoption.save()
    #         pet.available = False
    #         pet.save()
    #         return redirect('adoption_succ')
    #     else:
    #         form = AdoptionForm()

    #     return render(request,'adopt_pet.html', {'form':form, 'pet':pet})
