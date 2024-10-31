
from django.contrib import admin
from django.urls import path, include
from main import settings
from django.conf.urls.static import static
from loja.views import cadastrar, carrinho
from ecommerce.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('cadastrar/', cadastrar, name="cadastrar"),
    path('carrinho/', carrinho, name="carrinho"),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)