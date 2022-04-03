# 7.1 - No exercicio acima, adicionar quebra no nome para obter apenas o sonbrenome
# pedir para o usuario digitar nome e sobrenome
# Digite nome sobrenome: Jorge Santos

#  Output
# Nome: Jorge
# Sobrenome: Santos

name = input("Digite nome e sobrenome: ")

name_split = name.split()

if (len(name_split) >= 3):
    print(f'''
Nome: {name_split[0]}
Segundo nome: {name_split[1]}
Sobrenome: {name_split[2]}
''')
else:
    print(f'''
Nome: {name_split[0]}
Sobrenome: {name_split[1]}
''')
