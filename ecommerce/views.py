from django.shortcuts import render
from loja.models import Produto, Categoria, CarrinhoItem, Cliente
from loja.forms import ClienteForm

def index(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'base.html', {'produtos': produto, 'categorias': categoria})

def ofertas(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'ofertas.html', {'produtos': produto, 'categorias': categoria})
