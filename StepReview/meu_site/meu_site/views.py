from django.shortcuts import redirect, render
from cliente.models import Cliente, TpPessoa, UF, Cidade
from produto.models import Produto, Servico, Categoria
from cliente.forms import FormUF, FormCidade, FormTpPessoa, FormCliente
from produto.forms import FormCategoria, FormServico, FormProduto

def home(request):
    return render(request,'inicio.html')

def lista_cursos(request):
    cursos = ['Python','HTML','CSS','JavaScript','Java','Lógica de Programação']
    linhas = len(cursos)
    return render(request,'cursos.html',{'cursos' : cursos, 'total' : linhas})

def lista_categorias(request):
    categoria = Categoria.objects.all()
    totalCategoria = categoria.count
    return render(request,'lista-categorias.html',{'categoria' : categoria, 'total' : totalCategoria})

def cadastra_categoria(request):
    form = FormCategoria(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_categorias)
    return render(request,'cadastrar-categoria.html',{'form' : form})

def altera_categoria(request,id):
    categoria = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST,instance=categoria)

    if form.is_valid():
        form.save()
        return redirect(lista_categorias)
    
    return render(request,'alterar-categoria.html',{'form' : form,'categoria' : categoria})

def exclui_categoria(request,id):
    categoria = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect(lista_categorias)
    
    return render(request,'excluir-categoria.html',{'categoria' : categoria})

def lista_produtos(request):
    produto = Produto.objects.all().order_by('nome')
    totalProduto = produto.count
    return render(request,'lista-produtos.html',{'produto' : produto, 'total' : totalProduto})

def cadastra_produto(request):
    categorias = Categoria.objects.all().order_by('nome')
    form = FormProduto(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_produtos)

    return render(request,'cadastrar-produto.html',{'categoria' : categorias, 'form' : form})

def altera_produto(request,id):
    produto = Produto.objects.get(id=id)
    form = FormProduto(request.POST,instance=produto)
    categoria = Categoria.objects.get(id=produto.categ_id)
    listaCategoria = Categoria.objects.all()

    if form.is_valid():
        form.save()
        return redirect(lista_produtos)

    return render(request,'alterar-produto.html',{'produto' : produto, 'form' : form, 'categoriaProd' : categoria, 'listaCategoria' : listaCategoria})

def exclui_produto(request,id):
    produto = Produto.objects.get(id=id)
    categoria = Categoria.objects.get(id=produto.categ_id)

    if request.method == 'POST':
        produto.delete()
        return redirect(lista_produtos)
    
    return render(request,'excluir-produto.html',{'produto' : produto, 'categoria' : categoria})

def lista_clientes(request):
    cliente = Cliente.objects.all()
    totalCliente = cliente.count
    return render(request,'lista-clientes.html',{'cliente' : cliente, 'total' : totalCliente})

def cadastra_cliente(request):
    cidade = Cidade.objects.all().order_by('nome')
    form = FormCliente(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_clientes)

    return render(request,'cadastrar-cliente.html',{'cidade' : cidade, 'form' : form})

def altera_cliente(request,id): 
    cliente = Cliente.objects.get(id=id)
    form = FormCliente(request.POST,instance=cliente)
    cidade = Cidade.objects.all()
    cidadeCliente = Cidade.objects.get(id=cliente.cidade_id)

    if form.is_valid():
        form.save()
        return redirect(lista_clientes)

    return render(request,'alterar-cliente.html',{'form' : form, 'cidade' : cidade, 'cliente' : cliente, 'cidadeCliente' : cidadeCliente})

def exclui_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    cidade = Cidade.objects.get(id=cliente.cidade_id)
    estadocivil = ['Solteiro(a)','Casado(a)','Divorciado(a)','Viúvo(a)','Desquitado(a)','União Estável']
    opEstCivil = estadocivil[cliente.EstCivil-1]

    if request.method == 'POST':
        cliente.delete()
        return redirect(lista_clientes)
    
    return render(request,'excluir-cliente.html',{'cliente' : cliente, 'cidade' : cidade,'CliEstCivil' : opEstCivil})

def lista_tipos_pessoa(request):
    tipo = TpPessoa.objects.all()
    totalTipo = tipo.count
    return render(request,'lista-tps-pessoa.html',{'tipo' : tipo, 'total' : totalTipo})

def cadastra_tipos_pessoa(request):
    form = FormTpPessoa(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_tipos_pessoa)

    return render(request,'cadastrar-tipos-pessoa.html',{'form' : form})

def altera_tipos_pessoa(request,id):
    tipo = TpPessoa.objects.get(id=id)
    form = FormTpPessoa(request.POST,instance=tipo)

    if form.is_valid():
        form.save()
        return redirect(lista_tipos_pessoa)

    return render(request,'alterar-tipos-pessoa.html',{'form' : form, 'tipo' : tipo})

def exclui_tipos_pessoa(request,id):
    tipo = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        tipo.delete()
        return redirect(lista_tipos_pessoa)
    return render(request,'excluir-tipos-pessoa.html',{'tipo' : tipo})

def lista_ufs(request):
    uf = UF.objects.all().order_by('nome')
    totalUF = uf.count
    return render(request,'lista-uf.html',{'uf' : uf, 'total' : totalUF})

def cadastra_uf(request):    
    form = FormUF(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_ufs)
    
    return render(request,'cadastrar-uf.html',{'form' : form})

def altera_uf(request,id):
    uf = UF.objects.get(id=id)
    form = FormUF(request.POST,instance=uf)

    if form.is_valid():
        form.save()
        return redirect(lista_ufs)
    
    return render(request,'alterar-uf.html',{'uf' : uf,'form':form})

def exclui_uf(request,id):
    uf = UF.objects.get(id=id)
    if request.method == 'POST':
        uf.delete()
        return redirect(lista_ufs)
    return render(request,'excluir-uf.html',{'uf' : uf})

def lista_cidades(request):
    cidade = Cidade.objects.all().order_by('nome')
    totalCidade = cidade.count
    return render(request,'lista-cidades.html',{'cidade' : cidade, 'total' : totalCidade})

def cadastra_cidade(request):
    uf = UF.objects.all().order_by('nome')
    form = FormCidade(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_cidades)

    return render(request,'cadastrar-cidade.html',{'uf' : uf ,'form' : form})

def altera_cidade(request,id):
    cidade = Cidade.objects.get(id=id)
    form = FormCidade(request.POST,instance=cidade)
    estado = UF.objects.all()
    uf = UF.objects.get(id=cidade.uf_id)

    if form.is_valid():
        form.save()
        return redirect(lista_cidades)
    
    return render(request,'alterar-cidade.html',{'cidade' : cidade, 'form' : form,'uf' : uf, 'estado' : estado})

def exclui_cidade(request,id):
    cidade = Cidade.objects.get(id=id)
    estado = UF.objects.get(id=cidade.uf_id)

    if request.method == 'POST':
        cidade.delete()
        return redirect(lista_cidades)
    
    return render(request,'excluir-cidade.html',{'cidade' : cidade, 'estado' : estado})

def lista_servicos(request):
    servico = Servico.objects.all()
    totalServicos = servico.count
    return render(request,'lista-servicos.html', {'servico' : servico, 'total' : totalServicos})

def cadastra_servico(request):
    form = FormServico(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(lista_servicos)

    return render(request,'cadastrar-servico.html',{'form' : form})

def altera_servico(request,id):
    servico = Servico.objects.get(id=id)
    form = FormServico(request.POST,instance=servico)

    if form.is_valid():
        form.save()
        return redirect(lista_servicos)

    return render(request,'alterar-servico.html',{'form' : form,'servico' : servico})

def exclui_servico(request,id):
    servico = Servico.objects.get(id=id)
    if request.method == 'POST':
        servico.delete()
        return redirect(lista_servicos)
    return render(request,'excluir-servico.html',{'servico' : servico})