from django import forms
from django.forms import ModelForm
from .models import Categoria, Produto, Servico

class FormCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['id','nome']
        db_table = 'categoria'

class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = ['id','nome','valor', 'categoria']
        db_table = 'produto'

class FormServico(ModelForm):
    class Meta:
        model = Servico
        fields = ['id','nome','valor']
        db_table = 'servico'