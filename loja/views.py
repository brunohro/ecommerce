from django.shortcuts import render
from .models import Produto, Categoria
def index(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'loja/index.html', {'produtos': produto, 'categorias': categoria})

def cadastrar(request):
    return render(request, 'loja/cadastrar.html')
