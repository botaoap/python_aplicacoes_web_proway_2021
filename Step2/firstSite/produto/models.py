from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    valor = models.DecimalField(max_digits=5,decimal_places=2, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    class Meta:
        db_table = 'servico'

    def __str__(self):
        return self.nome