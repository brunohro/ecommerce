from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, CarrinhoItem, Cliente
from .forms import ClienteForm
def index(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'loja/index.html', {'produtos': produto, 'categorias': categoria})

def carrinho(request):
    return render(request, 'loja/carrinho.html')


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

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        form = ClienteForm()
    return render(request, 'loja/cadastrar.html', {'form': form})
