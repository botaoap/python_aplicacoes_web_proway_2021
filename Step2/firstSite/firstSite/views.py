from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from cliente.models import EstadoCivil, TpPessoa, CPFCNPJ, UF, Cidade, Cliente
from produto.models import Categoria, Produto, Servico
from cliente.forms import FormCidade, FormCliente, FormCPFCNPJ, FormTpPessoa, FormUF
from produto.forms import FormCategoria, FormProduto, FormServico

def home(request):
    return render(request,'home.html')
# ------ LISTAS ------
@login_required
def lista_produto(request):
    search = request.GET.get('txtSearch')
    hasSearch = False

    if search:
        produto = Produto.objects.filter(nome__icontains=search)
        hasSearch = True
    else:
        produto = Produto.objects.all()

    total = produto.count
    return render(request,'lista-produto.html', {'produto': produto, 'total': total, 'hasSearch': hasSearch})

def lista_cliente(request):
    search = request.GET.get('txtSearch')
    hasSearch = False
    
    if search:
        cliente = Cliente.objects.filter(nome__icontains=search)
        hasSearch = True
    else:
        cliente = Cliente.objects.all()
    
    total = cliente.count
    return render(request,'lista-cliente.html', {'cliente': cliente, 'total': total, 'hasSearch': hasSearch})

@login_required
def lista_servico(request):
    search = request.GET.get('txtSearch')
    hasSearch = False

    if search:
        servico = Servico.objects.filter(nome__icontains=search)
        hasSearch = True
    else:
        servico = Servico.objects.all()

    total = servico.count
    return render(request,'lista-servico.html', {'servico': servico, 'total': total, 'hasSearch': hasSearch})

@login_required
def lista_tp_pessoa(request):
    search = request.GET.get('txtSearch')
    hasSearch = False

    if search:
        tp_pessoa = TpPessoa.objects.filter(nome__icontains=search)
        hasSearch = True
    else:
        tp_pessoa = TpPessoa.objects.all()

    total = tp_pessoa.count
    return render(
        request,
        'lista-tp-pessoa.html', 
        {'tp_pessoa' : tp_pessoa, 'total': total, 'hasSearch': hasSearch}
    )

@login_required
def lista_uf(request):
    search = request.GET.get('txtSearch')
    hasSearch = False

    if search:
        uf = UF.objects.filter(nome__icontains=search)
        hasSearch = True
    else:
        uf = UF.objects.all()

    total = uf.count
    return render(request,'lista-uf.html', {'uf': uf, 'total': total, 'hasSearch': hasSearch})

@login_required
def lista_cidade(request):
    search = request.GET.get('txtSearch')
    hasSearch = False
    uf = UF.objects.all()

    if search:
        cidade = Cidade.objects.filter(nome__icontains=search)
        hasSearch = True
    else:
        cidade = Cidade.objects.all().order_by('nome')

    total = cidade.count

    return render(
        request,
        'lista-cidade.html', 
        {'cidade': cidade, 'total': total, 'hasSearch': hasSearch, 'uf': uf})

@login_required
def lista_categoria(request):
    search = request.GET.get('txtSearch')
    hasSearch = False
    
    if search:
        categoria = Categoria.objects.filter(nome__icontains=search)
        hasSearch = True
    else:
        categoria = Categoria.objects.all() 
    
    total = categoria.count
    return render(
        request, 
        'lista-categoria.html', 
        {'categoria': categoria, 'total': total, 'hasSearch': hasSearch}
    )

# ------ CADASTROS ------
@login_required
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

@login_required
def cadastro_cliente(request):
    cidade = Cidade.objects.all().order_by('nome')
    cpfcnpj = CPFCNPJ.objects.all()
    estado_civil = EstadoCivil.objects.all()
    estado = UF.objects.all()
    form = FormCliente(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect(lista_cliente)

    return render(
        request,
        'cadastro-cliente.html', 
        {
            'cidade': cidade, 
            'cpfcnpj': cpfcnpj, 
            'estado_civil': estado_civil,
            'estado': estado,
            'form': form
        }
    )

@login_required
def cadastro_servico(request):
    form = FormServico(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_servico)

    return render(request,'cadastro-servico.html', {'form': form})

@login_required
def cadastro_tp_pessoa(request):
    form = FormTpPessoa(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_tp_pessoa)

    return render(request,'cadastro-tp-pessoa.html', {'form': form})

@login_required
def cadastro_uf(request):
    form = FormUF(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_uf)

    return render(request,'cadastro-uf.html', {'form': form})

@login_required
def cadastro_cidade(request):
    uf = UF.objects.all()

    form = FormCidade(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_cidade)

    return render(request,'cadastro-cidade.html', {'uf': uf, 'form': form})

@login_required
def cadastro_categoria(request):
    form = FormCategoria(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(lista_categoria)

    return render(request,'cadastro-categoria.html', {'form': form})

# ------ ALTERA ------
@login_required
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

@login_required
def altera_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cidade_all = Cidade.objects.all()
    cidade_value = Cidade.objects.get(id=cliente.cidade_id)
    estado_civil_all = EstadoCivil.objects.all()
    estado_civil_value = EstadoCivil.objects.get(id=cliente.estado_civil_id)
    format_date = cliente.data_nasc.strftime('%d/%m/%Y')
    form = FormCliente(request.POST, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect(lista_cliente)

    dados = {
        'cliente': cliente,
        'cidade_all': cidade_all,
        'cidade_value': cidade_value,
        'estado_civil_all': estado_civil_all,
        'estado_civil_value': estado_civil_value,
        'format_date': format_date,
        'form': form
    }
    return render(request,'altera-cliente.html', dados)

@login_required
def altera_servico(request, id):
    servico = Servico.objects.get(id=id)
    form = FormServico(request.POST, instance=servico)
    if form.is_valid():
        form.save() 
        return redirect(lista_servico)

    return render(request,'altera-servico.html', {'servico': servico, 'form': form})

@login_required
def altera_tp_pessoa(request, id):
    tp_pessoa = TpPessoa.objects.get(id=id)
    form = FormTpPessoa(request.POST, instance=tp_pessoa)
    if form.is_valid():
        form.save()
        return redirect(lista_tp_pessoa)

    return render(request,'altera-tp-pessoa.html', {'tp_pessoa': tp_pessoa, 'form': form})

@login_required
def altera_uf(request, id):
    uf = UF.objects.get(id=id)
    form = FormUF(request.POST, instance=uf)
    if form.is_valid():
        form.save()
        return redirect(lista_uf)

    return render(request,'altera-uf.html', {'uf': uf, 'form': form})

@login_required
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

@login_required
def altera_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect(lista_categoria)

    return render(request,'altera-categoria.html', {'categoria': categoria, 'form': form})

# ------ EXCLUI ------

@login_required
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

@login_required
def exclui_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cidade_all = Cidade.objects.all()
    cidade_value = Cidade.objects.get(id=cliente.cidade_id)
    estado_civil_all = EstadoCivil.objects.all()
    estado_civil_value = EstadoCivil.objects.get(id=cliente.estado_civil_id)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect(lista_cliente)

    dados = {
        'cliente': cliente, 
        'cidade_all': cidade_all,
        'cidade_value': cidade_value,
        'estado_civil_all': estado_civil_all,
        'estado_civil_value': estado_civil_value
        }

    return render(request,'exclui-cliente.html',dados)

@login_required
def exclui_servico(request, id):
    service = Servico.objects.get(id=id)
    if request.method == 'POST':
        service.delete()
        return redirect(lista_servico)

    return render(request,'exclui-servico.html', {'service': service})

@login_required
def exclui_tp_pessoa(request, id):
    tp_pessoa = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        tp_pessoa.delete()
        return redirect(lista_tp_pessoa)

    return render(request,'exclui-tp-pessoa.html', {'tp_pessoa': tp_pessoa})

@login_required
def exclui_uf(request,id):
    uf = UF.objects.get(id=id)
    if request.method == 'POST':
        uf.delete()
        return redirect(lista_uf)

    return render(request,'exclui-uf.html',{'uf': uf})

@login_required
def exclui_cidade(request, id):
    cidade = Cidade.objects.get(id=id)
    uf = UF.objects.get(id=cidade.uf_id)
    if request.method == 'POST':
        cidade.delete()
        return redirect(lista_cidade)

    return render(request,'exclui-cidade.html', {'cidade': cidade, 'uf': uf})

@login_required
def exclui_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect(lista_categoria)

    return render(request,'exclui-categoria.html', {'categoria': categoria})

# ------ DETALHE ------
@login_required
def detalhe_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cidade_all = Cidade.objects.all()
    cidade_value = Cidade.objects.get(id=cliente.cidade_id)
    estado_civil_all = EstadoCivil.objects.all()
    estado_civil_value = EstadoCivil.objects.get(id=cliente.estado_civil_id)

    dados = {
        'cliente': cliente, 
        'cidade_all': cidade_all,
        'cidade_value': cidade_value,
        'estado_civil_all': estado_civil_all,
        'estado_civil_value': estado_civil_value
        }

    return render(request,'detalhe-cliente.html',dados)

# ------ CUSTOM VIEWS ------
@login_required
def getCity(request, id):
    cidade = [cidade for cidade in Cidade.objects.filter(uf_id=id)]
    
    return HttpResponse(str(cidade))
    
@login_required
def getIdOfCity(request, nome):
    cidade_id = [cidade.id for cidade in Cidade.objects.filter(nome=nome)]

    return HttpResponse(str(cidade_id))