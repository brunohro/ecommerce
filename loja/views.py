from django.shortcuts import render, redirect
from .models import Produto, Categoria, Cliente
from .forms import ClienteForm
def index(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'loja/index.html', {'produtos': produto, 'categorias': categoria})
def carrinho(request):
    return render(request, 'loja/carrinho.html')

def cadastrar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form = ClienteForm()
    return render(request, 'loja/cadastrar.html', {'form': form})