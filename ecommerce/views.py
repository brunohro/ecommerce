from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from loja.models import Produto, Categoria, CarrinhoItem, Cliente
from ecommerce.forms import ClienteForm, ProdutoForm

def index(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'index.html', {'produtos': produto, 'categorias': categoria})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona para a página inicial ou qualquer página desejada
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastrar_cliente.html', {'form': form})


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save() 
            return redirect('index')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cadastrar_cliente.html', {'form': form})


def remover_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente = Cliente.objects.get(id=id)
    cliente.delete() 
    return redirect('administrador')
    #return render(request, 'clientes/remover_cliente.html', {'cliente': cliente})  # Exibe confirmação para remover


def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona para a página inicial ou qualquer página desejada
        form = ProdutoForm(request.POST)
    else:
        form = ProdutoForm()
    return render(request, 'produtos/cadastrar_produtos.html', {'form': form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto = Produto.objects.get(id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('administrador')  # Redireciona para a página inicial ou qualquer página desejada
        form = ProdutoForm(request.POST)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produtos.html', {'form': form})

def remover_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto = Produto.objects.get(id=id)
    produto.delete() 
    return redirect('administrador')


def ofertas(request):
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, 'ofertas.html', {'produtos': produto, 'categorias': categoria})
def carrinho(request):
    return render(request, 'carrinho.html')


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
    return render(request, 'carrinho.html', context)

def remover_produto_carrinho(request, id):
    
    # Obtém o carrinho da sessão
    carrinho = request.session.get('carrinho', {})

    # Adiciona ou incrementa o produto no carrinho
    if str(id) in carrinho:
        del carrinho[str(id)]

    # Salva o carrinho na sessão
    request.session['carrinho'] = carrinho

    return redirect('carrinho')

def adm(request):
    cliente = Cliente.objects.all()
    produto = Produto.objects.all()
    categoria = Categoria.objects.all()

    list = Cliente.objects.all()
    paginator = Paginator(list, 3)  # Show 3 contacts per page.
    page_number = request.GET.get("page1")
    page_obj = paginator.get_page(page_number)

    list = Produto.objects.all()
    paginator = Paginator(list, 8)  # Show 8 contacts per page.
    page_number = request.GET.get("page2")
    page_obj2 = paginator.get_page(page_number)
    return render(request, 'administrador/adm.html', {'clientes': cliente, 'categorias': categoria, 'produtos': produto, "page_obj": page_obj, "page_obj2": page_obj2})


