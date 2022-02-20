from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def lista_produto(request):
    return render(request,'lista-produto.html')

def cadastro_produto(request):
    return render(request,'cadastro-produto.html')

def altera_produto(request):
    return render(request,'altera-produto.html')

def exclui_produto(request):
    pass

def lista_cliente(request):
    return render(request,'lista-cliente.html')

def cadastro_cliente(request):
    return render(request,'cadastro-cliente.html')

def altera_cliente(request):
    return render(request,'altera-cliente.html')

def exclui_cliente(request):
    pass

def lista_servico(request):
    return render(request,'lista-servico.html')

def cadastro_servico(request):
    return render(request,'cadastro-servico.html')

def altera_servico(request):
    return render(request,'altera-servico.html')

def exclui_servico(request):
    pass
    
def lista_tp_pessoa(request):
    return render(request,'lista-tp-pessoa.html')

def cadastro_tp_pessoa(request):
    return render(request,'cadastro-tp-pessoa.html')

def altera_tp_pessoa(request):
    return render(request,'altera-tp-pessoa.html')

def exclui_tp_pessoa(request):
    pass

def lista_uf(request):
    return render(request,'lista-uf.html')

def cadastro_uf(request):
    return render(request,'cadastro-uf.html')

def altera_uf(request):
    return render(request,'altera-uf.html')

def exclui_uf(request):
    pass

def lista_cidade(request):
    return render(request,'lista-cidade.html')

def cadastro_cidade(request):
    return render(request,'cadastro-cidade.html')

def altera_cidade(request):
    return render(request,'altera-cidade.html')

def exclui_cidade(request):
    pass