from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from loja.models import Produto, Categoria, CarrinhoItem, Cliente, Area
from ecommerce.forms import ClienteForm, ProdutoForm, CategoriaForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

def index(request):
    produtos = Produto.objects.all()
    categoria = Categoria.objects.all()

    if request.method == 'POST':
        query_pesquisa = request.POST.get("search", None)
        if query_pesquisa is not None:
            produtos = produtos.filter(nome__icontains=query_pesquisa)

    return render(request, 'index.html', {'produtos': produtos, 'categorias': categoria})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            django_login(request, user)
            return redirect('index')

    return render(request, 'login.html')

def logout(request):
    django_logout(request)

    return redirect('index')

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            user = form.save() 
            user.set_password(form.cleaned_data['password'])
            user.save()
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
            user = form.save() 
            user.set_password(form.cleaned_data['password'])
            user.save()
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

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona para a página inicial ou qualquer página desejada
    else:
        form = CategoriaForm()
    return render(request, 'categorias/cadastrar_categoria.html', {'form': form})

def editar_categoria(request, id):
    # Obtém a categoria pelo ID ou retorna um erro 404
    categoria = get_object_or_404(Categoria, id=id)  

    if request.method == 'POST':
        # Manipula o formulário enviado
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('administrador') 
    else:
        # Exibe o formulário com os dados da categoria existente
        form = CategoriaForm(instance=categoria)

    return render(request, 'categorias/editar_categoria.html', {'form': form})

def remover_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria = Categoria.objects.get(id=id)
    categoria.delete() 
    return redirect('administrador')
    #return render(request, 'clientes/remover_cliente.html', {'cliente': cliente})  # Exibe confirmação para remover


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

def ofertas(request):
    try:
        area_ofertas = Area.objects.get(nome="Ofertas") 
        produtos_em_oferta = Produto.objects.filter(area=area_ofertas) 
    except Area.DoesNotExist:
        produtos_em_oferta = [] 
    categorias = Categoria.objects.all()
    return render(request, 'ofertas.html', {'produtos': produtos_em_oferta, 'categorias': categorias})


def lancamentos(request):
    try:
        area_lancamentos = Area.objects.get(nome="Lançamento") 
        produtos_em_lancamento = Produto.objects.filter(area=area_lancamentos) 
    except Area.DoesNotExist:
        produtos_em_lancamento = [] 
    categoria = Categoria.objects.all()
    return render(request, 'lancamentos.html', {'produtos': produtos_em_lancamento, 'categorias': categoria})

def roupas(request):
    produtos = Produto.objects.filter(categoria__nome="Roupas") 
    categorias = Categoria.objects.all()
    return render(request, 'roupas.html', {'produtos': produtos, 'categorias': categorias})

def calcados(request):
    produtos = Produto.objects.filter(categoria__nome="Calçados")  
    categorias = Categoria.objects.all()
    return render(request, 'calcados.html', {'produtos': produtos, 'categorias': categorias})

def informatica(request):
    produtos = Produto.objects.filter(categoria__nome="Informática")  
    categorias = Categoria.objects.all()
    return render(request, 'informatica.html', {'produtos': produtos, 'categorias': categorias})
