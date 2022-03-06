import imp
from pydoc import cli
import re
from django.shortcuts import render
from cliente.models import TpPessoa, CPFCNPJ, UF, Cidade, Cliente
from produto.models import Categoria, Produto, Servico

def home(request):
    return render(request,'home.html')
# ------ LISTAS ------
def lista_produto(request):
    produto = Produto.objects.all()
    total = produto.count
    return render(request,'lista-produto.html', {'produto': produto, 'total': total})

def lista_cliente(request):
    cliente = Cliente.objects.all()
    total = cliente.count
    return render(request,'lista-cliente.html', {'cliente': cliente, 'total': total})

def lista_servico(request):
    servico = Servico.objects.all()
    total = servico.count
    return render(request,'lista-servico.html', {'servico': servico, 'total': total})

def lista_tp_pessoa(request):
    tp_pessoa = TpPessoa.objects.all()
    total = tp_pessoa.count
    return render(request,'lista-tp-pessoa.html', {'tp_pessoa' : tp_pessoa, 'total': total})

def lista_uf(request):
    uf = UF.objects.all()
    total = uf.count
    return render(request,'lista-uf.html', {'uf': uf, 'total': total})

def lista_cidade(request):
    cidade = Cidade.objects.all().order_by('nome')
    total = cidade.count
    return render(request,'lista-cidade.html', {'cidade': cidade, 'total': total})

def lista_categoria(request):
    categoria = Categoria.objects.all()
    total = categoria.count
    return render(request, 'lista-categoria.html', {'categoria': categoria, 'total': total})

# ------ CADASTROS ------
def cadastro_produto(request):
    categoria = Categoria.objects.all()
    return render(request,'cadastro-produto.html', {'categoria': categoria})

def cadastro_cliente(request):
    cidade = Cidade.objects.all().order_by('nome')
    return render(request,'cadastro-cliente.html', {'cidade': cidade})

def cadastro_servico(request):
    return render(request,'cadastro-servico.html')

def cadastro_tp_pessoa(request):
    return render(request,'cadastro-tp-pessoa.html')

def cadastro_uf(request):
    return render(request,'cadastro-uf.html')

def cadastro_cidade(request):
    uf = UF.objects.all()
    return render(request,'cadastro-cidade.html', {'uf': uf})

def cadastro_categoria(request):
    return render(request,'cadastro-categoria.html')

# ------ ALTERA ------
def altera_produto(request):
    return render(request,'altera-produto.html')

def altera_cliente(request):
    return render(request,'altera-cliente.html')

def altera_servico(request):
    return render(request,'altera-servico.html')

def altera_tp_pessoa(request):
    return render(request,'altera-tp-pessoa.html')

def altera_uf(request):
    return render(request,'altera-uf.html')

def altera_cidade(request):
    return render(request,'altera-cidade.html')

def altera_categoria(request):
    return render(request,'altera-categoria.html')

# ------ EXCLUI ------
def exclui_produto(request):
    return render(request, 'exclui-produto.html')

def exclui_cliente(request):
    return render(request,'exclui-cliente.html')

def exclui_servico(request):
    return render(request,'exclui-servico.html')

def exclui_tp_pessoa(request):
    return render(request,'exclui-tp-pessoa.html')

def exclui_uf(request):
    return render(request,'exclui-uf.html')

def exclui_cidade(request):
    return render(request,'exclui-cidade.html')

def exclui_categoria(request):
    return render(request,'exclui-categoria.html')