
from django.contrib import admin
from django.urls import path
from loja.views import index, cadastrar_cliente, carrinho, add_ao_carrinho, remover_produto
from main import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('cadastrar/', cadastrar_cliente, name="cadastrar_cliente"),
    path('add_ao_carrinho/<int:id>/', add_ao_carrinho, name='add_ao_carrinho'),
    path('remover_produto/<int:id>/', remover_produto, name='remover_produto'),
    path('carrinho/', carrinho, name="carrinho"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)