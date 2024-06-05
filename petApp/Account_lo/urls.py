from django.urls import path
from.import views

urlpatterns = [
    path('home/',views.homepage, name='homepage'),
    path('signup/',views.signup, name='signup'),
    path('logi/',views.login_view, name='login_view'),
    path('logou/',views.logout_view, name='logout_view'),
    path('profile/', views.profile_view, name='profile_view')

]