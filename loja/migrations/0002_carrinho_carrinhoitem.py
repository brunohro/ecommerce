# Generated by Django 5.1.2 on 2024-10-28 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
                ('total_produto', models.FloatField(blank=True, max_length=10, null=True)),
                ('produto', models.ManyToManyField(to='loja.produto')),
            ],
        ),
        migrations.CreateModel(
            name='CarrinhoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.produto')),
            ],
        ),
    ]