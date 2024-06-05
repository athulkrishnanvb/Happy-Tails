from django.urls import path
from.views import shelter_add
from.import views

urlpatterns = [
    path('shelteradd/',views.shelter_add, name='shelter_add')
]