from django.shortcuts import render

def index(request):
    return render(request, 'loja/index.html')

def cadastrar(request):
    return render(request, 'loja/cadastrar.html')
