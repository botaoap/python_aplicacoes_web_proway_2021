from django import forms
from django.forms import ModelForm
from .models import TpPessoa, CPFCNPJ, Cliente, UF, Cidade

class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['id','nome','email','data_nasc','cpfcnpj','cidade','genero','profissao','renda','carro','estado_civil','filho']
        db_table = 'cliente'

class FormCidade(ModelForm):
    class Meta:
        model = Cidade
        fields = ['id','nome','uf']
        db_table = 'cidade'

class FormUF(ModelForm):
    class Meta:
        model = UF
        fields = ['id','nome','sigla']
        db_table = 'uf'

class FormCPFCNPJ(ModelForm):
    class Meta:
        model = CPFCNPJ
        fields = ['id','tipo','valor']
        db_table = 'cpfcnpj'

class FormTpPessoa(ModelForm):
    class Meta:
        model = TpPessoa
        fields = ['id','nome']
        db_table = 'tppessoa'