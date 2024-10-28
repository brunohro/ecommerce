<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, CarrinhoItem
=======
from django.shortcuts import render, redirect
from .models import Produto, Categoria, Cliente
from .forms import ClienteForm
>>>>>>> c2003ad6e8523a2f2ddb5a5eb6259759398b3a73
def index(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'loja/index.html', {'produtos': produto, 'categorias': categoria})
def carrinho(request):
    return render(request, 'loja/carrinho.html')

def cadastrar(request):
<<<<<<< HEAD
    return render(request, 'loja/cadastrar.html')


def add_ao_carrinho(request, id):
    # Obtém o produto pelo ID
    produto = get_object_or_404(Produto, id=id)
    
    # Obtém o carrinho da sessão
    carrinho = request.session.get('carrinho', {})

    # Adiciona ou incrementa o produto no carrinho
    if str(id) in carrinho:
        carrinho[str(id)]['quantidade'] += 1
    else:
        carrinho[str(id)] = {
            'produto_nome': produto.nome,
            'preco': str(produto.preco),
            'quantidade': 1
        }

    # Salva o carrinho na sessão
    request.session['carrinho'] = carrinho

    return redirect('carrinho')


def carrinho(request):
    carrinho = request.session.get('carrinho', {})
    preco_total = sum(float(item['preco']) * item['quantidade'] for item in carrinho.values())

    context = {
        'carrinho': carrinho.items(),
        'preco_total': preco_total
    }
    return render(request, 'loja/carrinho.html', context)

def remover_produto(request, id):
    
    # Obtém o carrinho da sessão
    carrinho = request.session.get('carrinho', {})

    # Adiciona ou incrementa o produto no carrinho
    if str(id) in carrinho:
        del carrinho[str(id)]

    # Salva o carrinho na sessão
    request.session['carrinho'] = carrinho

    return redirect('carrinho')
=======
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form = ClienteForm()
    return render(request, 'loja/cadastrar.html', {'form': form})
>>>>>>> c2003ad6e8523a2f2ddb5a5eb6259759398b3a73
