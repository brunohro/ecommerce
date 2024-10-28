from django.contrib import admin
from .models import Categoria, Produto, Carrinho, CarrinhoItem

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)  

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome',) 

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('valor',)

@admin.register(CarrinhoItem)
class CarrinhoItemAdmin(admin.ModelAdmin):
    list_display = ('quantidade',)  
