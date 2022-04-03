# Back End lista de compras

# Pre-requisitos Sistema
# 1 - Nao utilizar Classes
# 2 - Utilizar pelo menos 2 metodos(Def/Functions)

# Pre-requisitos Negocio
# 1 - Produto: Nome do produto, Quantidade, Valor
# 2 - Lista nao pode ter itens zerados
# 3 - Possuir Validacao de itens parecidos
#   Ex: Se tiver Queijo Marca x e Queijo Marca y, informar ao usuario que está comprando produtos similares

import os
import time
os.system('cls||clear')
dict_db_produto = {}

def func_produto(id, marca, produto, quantidade, valor_unit):
    dict_produto = {
        'marca' : marca,
        'produto' : produto,
        'qtd' : quantidade,
        'valor_unit' : valor_unit
    }

    dict_produto_local = {
        id : dict_produto
    }

    dict_db_produto.update(dict_produto_local)

def validation(value):
    if (value == ''):
        return True
    return False

def clean_terminal():
    os.system('cls||clear')

def timer_terminal(timer):
    time.sleep(timer)

def field_empty(timer):
    clean_terminal()
    print('Preencha todos os campos!')
    timer_terminal(timer)
    clean_terminal()

def option_continue(option):
    while True:
        if (option.lower() == 'S'.lower()):
            break
        elif (option.lower() == 'N'.lower()):
            break
        else:
            print("Opção invpalida!")
            continue
    clean_terminal()
    return option
# produto(1,'Sadia','Presunto',2, 10.0)
# produto(2,'Perdicao','Queijo',2, 10.0)

# print(dict_db_produto)
id = 0
while True:
    while True:
        marca = input("Marca: ")
        produto = input("Produto: ")
        quantidade = input("Quantidade: ")
        valor_unit = input("Valor Unitário: ")
        if (validation(marca) and validation(produto)):
            field_empty(timer=1)
            continue
        elif (validation(quantidade) and validation(valor_unit)):
            field_empty(timer=1)
            continue
        else:
            break
    id += 1
    func_produto(id=id, marca=marca, produto=produto,quantidade=int(quantidade), valor_unit=float(valor_unit))

    option = input('''
Para cadastar mais produtos digite: 'S'
Para sair do sistema digite: 'N'
-> ''')
    
    option_continue(option)

    if (option.lower() == 'S'.lower()):
        continue
    elif (option.lower() == 'N'.lower()):
        break

# if (dict_db_produto['produto'] == produto):
#     print("AVISO! Comprou o mesmo produto de marca diferente!")
#     timer_terminal(1)


# for item in dict_db_produto.keys():
#     print(item)

# for items in :
#     print(items)

print(dict_db_produto)

    

