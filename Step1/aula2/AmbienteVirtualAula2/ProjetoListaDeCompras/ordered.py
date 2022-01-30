dict_lista_compras = {}

#dict_lista_compras= {'1':'Beterraba','2':'Pãozinho','3':'Café'}

# Criar Forma Dinamica de Adicionar Itens no Dicionario dict_lista_compras

qt_produots = int(input("Quantos Produtos Deseja em Sua Lista? \n"))

while(True):
    if (qt_produots == 0):
        break
    else:
        produto = input("Digite um Produto: \n")
        dict_lista_compras[qt_produots] = produto
        qt_produots =  qt_produots -1


id_produtos = dict_lista_compras.keys()

lista_id_produtos = []

for produto in id_produtos:
    lista_id_produtos.append(produto)

print("\n")

print (lista_id_produtos[:-1])

print("\n")

for id in lista_id_produtos[:-1]:
    print(dict_lista_compras[id])
    print("\n")