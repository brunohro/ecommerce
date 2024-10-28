from django.contrib import admin
<<<<<<< HEAD
from .models import Categoria, Produto, Carrinho, CarrinhoItem
=======
from .models import Categoria, Produto, Cliente
>>>>>>> c2003ad6e8523a2f2ddb5a5eb6259759398b3a73

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)  

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome',) 
<<<<<<< HEAD

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('valor',)

@admin.register(CarrinhoItem)
class CarrinhoItemAdmin(admin.ModelAdmin):
    list_display = ('quantidade',)  
=======
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo',) 

>>>>>>> c2003ad6e8523a2f2ddb5a5eb6259759398b3a73
