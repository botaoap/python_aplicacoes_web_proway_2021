# Generated by Django 4.0.1 on 2022-01-30 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_categoria_rename_modelproduto_produto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produto',
            new_name='Produtos',
        ),
    ]
