from re import A
from django.db import models

# Create your models here.
class TpPessoa(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False, unique=True)

    class Meta:
        db_table = 'TpPessoa'
    
    def __str__(self):
        return self.nome

class CPFCNPJ(models.Model):
    valor = models.CharField(max_length=11, blank=False, null=False, unique=True)
    tipo = models.ForeignKey(TpPessoa, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'CPFCNPJ'
    
    def __str__(self):
        return self.valor

class UF(models.Model):
    sigla = models.CharField(max_length=2, unique=True, blank=False, null=False)

    class Meta:
        db_table = 'UF'
    
    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'Cidade'
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    data_nasc = models.DateField()
    cpfcnpj = models.OneToOneField(CPFCNPJ, on_delete=models.CASCADE, blank=False, null=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'cliente'
    
    def __str__(self):
        return self.nome