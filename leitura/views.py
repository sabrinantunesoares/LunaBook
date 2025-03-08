from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Livro

class IndexView(TemplateView):
    template_name = 'leitura/index.html'

def biblioteca_view(request):
    return render(request, 'leitura/biblioteca.html')

def historico_view(request):
    return render(request, 'leitura/historico.html')


def lista_livros(request):
    livros = Livro.objects.filter(estante='na_estante')  
    return render(request, 'livros/lista_livros.html', {'livros': livros})