from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from.models import Pet
from shelters.models import Shelter
# from.forms import PetForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

def petadd(request):
    if request.method=='POST':
        myfile=request.FILES['photo']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)

        obj=Pet()
        obj.photo=filename
        obj.name=request.POST.get('name')
        obj.breed=request.POST.get('breed')
        obj.age=request.POST.get('age')
        obj.gender=request.POST.get('gender')
        obj.health_status=request.POST.get('health_status')
        obj.description=request.POST.get('description')
        obj.available=request.POST.get('available')=='on'

        shelter_id = request.POST.get('shelter')
        obj.shelter = Shelter.objects.get(id=shelter_id)

        obj.save()
        return redirect('pet_list')
    
    else:
        shelters = Shelter.objects.all()
        return render(request, "pet_details.html", {'shelters': shelters})

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pet_list.html', {'pets': pets})

def p_update(request, id):
    pet = get_object_or_404(Pet, id=id)
    shelters = Shelter.objects.all()

    if request.method == 'POST':
        pet.photo = request.FILES.get('photo')
        pet.name = request.POST.get('name')
        pet.breed = request.POST.get('breed')
        pet.age = request.POST.get('age')
        pet.gender = request.POST.get('gender')
        pet.health_status = request.POST.get('health_status')
        pet.description = request.POST.get('description')
        pet.available = request.POST.get('available') == 'on'
        pet.shelter_id = request.POST.get('shelter')
        pet.save()
        return redirect('pet_list') 
    
    return render(request, 'pet_update.html', {'pet': pet, 'shelters': shelters})

def p_delete(request, id):
    obj=Pet.objects.get(id=id).delete()
    return pet_list(request)

def filtered_pet_list(request):
    breed_filter = request.GET.get('breed')
    shelter_filter = request.GET.get('name')

    pets = Pet.objects.all()

    if breed_filter:
        pets = pets.filter(breed=breed_filter)

    if shelter_filter:
        pets = pets.filter(name=shelter_filter)

    return render(request, 'pet_list.html', {'pets': pets})