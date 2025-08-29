from django.urls import path
from . import views

app_name = 'races'

urlpatterns = [
    # Vista principal
    path('', views.index, name='index'),
    
    # API endpoints
    path('pilotos/', views.lista_pilotos, name='lista_pilotos'),
]