
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
from loja.views import index, cadastrar_cliente, carrinho, add_ao_carrinho, remover_produto
>>>>>>> 12715ad282f6a3ed0dc8154e05090918195f8dd1
from main import settings
from django.conf.urls.static import static
from loja.views import cadastrar, carrinho
from ecommerce.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('cadastrar/', cadastrar_cliente, name="cadastrar_cliente"),
    path('add_ao_carrinho/<int:id>/', add_ao_carrinho, name='add_ao_carrinho'),
    path('remover_produto/<int:id>/', remover_produto, name='remover_produto'),
    path('carrinho/', carrinho, name="carrinho"),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)