from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)  # Adicionado campo para imagem

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
