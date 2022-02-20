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
    tipo = models.ForeignKey(TpPessoa, on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = 'CPFCNPJ'
    
    def __str__(self):
        return self.valor

class UF(models.Model):
    nome = models.CharField(max_length=20,unique=True, blank=False, null=False)
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
    GENDER = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    CAR = [
        ('S','Sim'),
        ('N', 'Não'),
    ]
    CIVIL_STATE = [
        (1,'Solteiro(a)'),
        (2,'Casado(a)'),
        (3,'Divorcido(a)'),
        (4,'Viuvo(a)'),
        (5,'Desquitado(a)'),
        (6,'União Estável'),
    ]

    CHILD = [
        ('S','Sim'),
        ('N','Não')
    ]
    nome = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    data_nasc = models.DateField(null=True, blank=True)
    cpfcnpj = models.OneToOneField(CPFCNPJ, on_delete=models.CASCADE, blank=False, null=False)
    cidade = models.ManyToManyField(Cidade)
    genero = models.CharField(max_length=1,choices=GENDER, null=True,  blank=True)
    profissao = models.CharField(max_length=50,null=True,  blank=True)
    renda = models.DecimalField(max_digits=8, decimal_places=2,null=True,  blank=True)
    carro = models.CharField(max_length=1,choices=CAR,null=True,  blank=True)
    estadoCivil = models.IntegerField(choices=CIVIL_STATE, default=1, null=True,  blank=True)
    filho = models.CharField(max_length=1,choices=CHILD, null=True,  blank=True)

    class Meta:
        db_table = 'cliente'
    
    def __str__(self):
        return self.nome