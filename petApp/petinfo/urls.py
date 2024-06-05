from django.urls import path
from.import views

urlpatterns = [
    path('add/',views.petadd, name='petadd'),
    path('pet_list/', views.pet_list, name='pet_list'),
    path('update/<int:id>/',views.p_update, name='p_update'),
    path('delete/<int:id>/',views.p_delete, name='p_delete'),
    path('filter/',views.filtered_pet_list, name='filtered_pet_list'),
]