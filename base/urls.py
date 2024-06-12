from django.urls import path
from . import views

urlpatterns = [
    path('home',views.Home, name='home'),
    path('about',views.About, name='about'),
    path('place',views.Place, name='place'),



]
