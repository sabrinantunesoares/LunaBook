from django.contrib import admin
from django.urls import path, include
from leitura import views  # Importando a view corretamente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('leitura.urls')),
]