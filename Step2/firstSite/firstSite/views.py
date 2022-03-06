from ast import Is
from math import prod
import os
from re import U
from django.forms import all_valid
from django.shortcuts import redirect, render
from cliente.models import TpPessoa, CPFCNPJ, UF, Cidade, Cliente
from produto.models import Categoria, Produto, Servico
from cliente.forms import FormCidade, FormCliente, FormCPFCNPJ, FormTpPessoa, FormUF
from produto.forms import FormCategoria, FormProduto, FormServico

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
    return render(
        request,
        'lista-tp-pessoa.html', 
        {'tp_pessoa' : tp_pessoa, 'total': total}
    )

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
    return render(
        request, 
        'lista-categoria.html', 
        {'categoria': categoria, 'total': total}
    )

# ------ CADASTROS ------
def cadastro_produto(request):
    categoria = Categoria.objects.all()
    form = FormProduto(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_produto)

    return render(
        request,
        'cadastro-produto.html', 
        {'categoria': categoria, 'form': form}
    )

def cadastro_cliente(request):
    cidade = Cidade.objects.all().order_by('nome')
    cpfcnpj = CPFCNPJ.objects.all()
    form = FormCliente(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_cliente)

    return render(
        request,
        'cadastro-cliente.html', 
        {'cidade': cidade, 'cpfcnpj': cpfcnpj, 'form': form}
    )

def cadastro_servico(request):
    form = FormServico(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_servico)

    return render(request,'cadastro-servico.html', {'form': form})

def cadastro_tp_pessoa(request):
    form = FormTpPessoa(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_tp_pessoa)

    return render(request,'cadastro-tp-pessoa.html', {'form': form})

def cadastro_uf(request):
    form = FormUF(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_uf)

    return render(request,'cadastro-uf.html', {'form': form})

def cadastro_cidade(request):
    uf = UF.objects.all()

    form = FormCidade(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_cidade)

    return render(request,'cadastro-cidade.html', {'uf': uf, 'form': form})

def cadastro_categoria(request):
    form = FormCategoria(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_categoria)

    return render(request,'cadastro-categoria.html', {'form': form})

# ------ ALTERA ------
def altera_produto(request,id):
    produto = Produto.objects.get(id=id)
    all_categoria = Categoria.objects.all()
    id_categoria = Categoria.objects.get(id=produto.categoria_id)
    form = FormProduto(request.POST, instance=produto)
    if form.is_valid():
        form.save()
        return redirect(lista_produto)

    return render(
        request,
        'altera-produto.html',
        {
            'produto': produto, 
            'all_categoria': all_categoria,
            'id_categoria': id_categoria,
            'form': form
        }
    )

def altera_cliente(request):
    return render(request,'altera-cliente.html')

def altera_servico(request, id):
    servico = Servico.objects.get(id=id)
    form = FormServico(request.POST, instance=servico)
    if form.is_valid():
        form.save() 
        return redirect(lista_servico)

    return render(request,'altera-servico.html', {'servico': servico, 'form': form})

def altera_tp_pessoa(request, id):
    tp_pessoa = TpPessoa.objects.get(id=id)
    form = FormTpPessoa(request.POST, instance=tp_pessoa)
    if form.is_valid():
        form.save()
        return redirect(lista_tp_pessoa)

    return render(request,'altera-tp-pessoa.html', {'tp_pessoa': tp_pessoa, 'form': form})

def altera_uf(request, id):
    uf = UF.objects.get(id=id)
    form = FormUF(request.POST, instance=uf)
    if form.is_valid():
        form.save()
        return redirect(lista_uf)

    return render(request,'altera-uf.html', {'uf': uf, 'form': form})

def altera_cidade(request, id):
    cidade = Cidade.objects.get(id=id)
    uf = UF.objects.get(id=cidade.uf_id)
    all_uf = UF.objects.all()
    form = FormCidade(request.POST,instance=cidade)

    if form.is_valid():
        form.save()
        return redirect(lista_cidade)

    return render(
        request,
        'altera-cidade.html',
        {
            'cidade': cidade, 
            'uf': uf, 
            'all_uf': all_uf, 
            'form': form
        }
    )


def altera_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect(lista_categoria)

    return render(request,'altera-categoria.html', {'categoria': categoria, 'form': form})

# ------ EXCLUI ------
def exclui_produto(request, id):
    produto = Produto.objects.get(id=id)
    categoria = Categoria.objects.get(id=produto.categoria_id)
    if request.method == 'POST':
        produto.delete()
        return redirect(lista_produto)

    return render(
        request, 
        'exclui-produto.html', 
        {'produto': produto, 'categoria': categoria}
    )

def exclui_cliente(request):
    return render(request,'exclui-cliente.html')

def exclui_servico(request, id):
    service = Servico.objects.get(id=id)
    if request.method == 'POST':
        service.delete()
        return redirect(lista_servico)

    return render(request,'exclui-servico.html', {'service': service})

def exclui_tp_pessoa(request, id):
    tp_pessoa = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        tp_pessoa.delete()
        return redirect(lista_tp_pessoa)

    return render(request,'exclui-tp-pessoa.html', {'tp_pessoa': tp_pessoa})

def exclui_uf(request,id):
    uf = UF.objects.get(id=id)
    if request.method == 'POST':
        uf.delete()
        return redirect(lista_uf)

    return render(request,'exclui-uf.html',{'uf': uf})

def exclui_cidade(request, id):
    cidade = Cidade.objects.get(id=id)
    uf = UF.objects.get(id=cidade.uf_id)
    if request.method == 'POST':
        cidade.delete()
        return redirect(lista_cidade)

    return render(request,'exclui-cidade.html', {'cidade': cidade, 'uf': uf})

def exclui_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect(lista_categoria)

    return render(request,'exclui-categoria.html', {'categoria': categoria})