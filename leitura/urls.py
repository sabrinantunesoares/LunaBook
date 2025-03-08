from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  
    path('biblioteca/', views.biblioteca_view, name='biblioteca'), 
    path('historico/', views.historico_view, name='historico'),   
    path('livros/', views.lista_livros, name='lista_livros'),
]