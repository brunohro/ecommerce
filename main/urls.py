
from django.contrib import admin
from django.conf import settings

from django.urls import path, include

from django.urls import path
from django.conf.urls.static import static
from ecommerce.views import index, ofertas, roupas, informatica, carrinho, calcados, add_ao_carrinho, remover_produto_carrinho, adm, lancamentos
from ecommerce.views import cadastrar_cliente, editar_cliente, remover_cliente
from ecommerce.views import cadastrar_produto, editar_produto, remover_produto
from ecommerce.views import cadastrar_categoria, editar_categoria, remover_categoria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('cadastrar/', cadastrar_cliente, name="cadastrar_cliente"),
    path('cadastrar_produto/', cadastrar_produto, name="cadastrar_produto"),
    path('cadastrar_categoria/', cadastrar_categoria, name="cadastrar_categoria"),
    path('editar/<int:id>/', editar_cliente, name="editar_cliente"),
    path('editar_produto/<int:id>/', editar_produto, name="editar_produto"),
    path('editar_categoria/<int:id>/', editar_categoria, name="editar_categoria"),
    path('remover/<int:id>/', remover_cliente, name="remover_cliente"),
    path('remover_produto/<int:id>/', remover_produto, name='remover_produto'),
    path('remover_categoria/<int:id>/', remover_categoria, name='remover_categoria'),
    path('add_ao_carrinho/<int:id>/', add_ao_carrinho, name='add_ao_carrinho'),
    path('remover_produto_carrinho/<int:id>/', remover_produto_carrinho, name='remover_produto_carrinho'),
    path('administrador/', adm, name='administrador'),
    path('carrinho/', carrinho, name="carrinho"),
    path("__reload__/", include("django_browser_reload.urls")),
    path('ofertas/', ofertas, name='ofertas'),
    path('roupas/', roupas, name='roupas'),
    path('calcados/', calcados, name='calcados'),
    path('informatica/', informatica, name='informatica'),
    path('lancamentos/', lancamentos, name='lancamentos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)