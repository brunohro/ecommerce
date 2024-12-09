# Generated by Django 5.1.2 on 2024-12-09 10:48

import loja.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_cliente_last_login_cliente_password'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='cliente',
            managers=[
                ('objects', loja.models.CustomManager()),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]