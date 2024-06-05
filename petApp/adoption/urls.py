from django.urls import path
from.views import adopt_pet
from.import views

urlpatterns = [
    path('adopt/<int:id>/', adopt_pet, name='adopt_pet'),
    path('contact_shelter/', views.contact_shelter, name='contact_shelter')
]