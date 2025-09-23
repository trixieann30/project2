from django.urls import path
from . import views

urlpatterns = [
    # The home page for the calculator app.
    path('', views.index, name='index'),
    
    # A path for the calculation logic.
    path('calculate/', views.calculate, name='calculate'),
]
