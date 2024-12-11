from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome
    
class Area(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        null=True, 
        blank=True 
    )
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)  # Campo opcional para imagem

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    produto = models.ManyToManyField(Produto)
    valor = models.FloatField(blank=True, null=True)
    total_produto = models.FloatField(max_length=10, blank=True, null=True)


class CarrinhoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.produto

class CustomManager(UserManager):
    def create_user(self, email, password, **data):
        user = Cliente(email=email, **data)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_super_user(self, email, password, **data):
        user = Cliente(email=email, **data)
        user.set_password(password)
        user.save(using=self._db)

        return user
        
    
class Cliente(AbstractUser):
    # Identificação básica do cliente
    username = models.CharField(max_length=100, null=True)
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    
    # Endereço do cliente
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)  # Exemplo: 'SP', 'RJ'
    cep = models.CharField(max_length=10)

    # Informações adicionais
    cpf = models.CharField(max_length=14, unique=True)  # Formato: 000.000.000-00
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo', 'username', 'cpf']

    objects = CustomManager()

    def __str__(self):
        return self.nome_completo

