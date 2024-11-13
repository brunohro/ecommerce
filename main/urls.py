
from django.contrib import admin

from django.urls import path, include

from django.urls import path
from django.conf.urls.static import static
from ecommerce.views import index, ofertas, cadastrar_cliente, carrinho, add_ao_carrinho, remover_produto, adm
from ecommerce.views import cadastrar_cliente, editar_cliente, remover_cliente
from main import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('cadastrar/', cadastrar_cliente, name="cadastrar_cliente"),
    path('editar/<int:id>/', editar_cliente, name="editar_cliente"),
    path('remover/<int:id>/', remover_cliente, name="remover_cliente"),
    path('add_ao_carrinho/<int:id>/', add_ao_carrinho, name='add_ao_carrinho'),
    path('remover_produto/<int:id>/', remover_produto, name='remover_produto'),
    path('administrador/', adm, name='administrador'),
    path('ofertas/', ofertas, name='ofertas'),
    path('carrinho/', carrinho, name="carrinho"),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)