
from django.contrib import admin
from django.urls import path
from loja.views import index, cadastrar, carrinho
from main import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('cadastrar/', cadastrar, name="cadastrar"),
    path('carrinho/', carrinho, name="carrinho"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)