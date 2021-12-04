# Usando metodos para nao usar WHILE

# Exercicio 7

import os

def redigite(campo):
    return input("Digite novamente o(a): " + campo + " \n")

def validacao(qt_letras_nome, idade, sexo, salario, est_civ):
    if qt_letras_nome <=3:
        print("Nome muito curto")
        nome = redigite("Nome")
        qt_letras_nome = len(nome)
        validacao(qt_letras_nome,idade)
    if idade < 0:
        print("Valor para idade incorreto")
        idade = int(redigite("Idade"))
        validacao(qt_letras_nome,idade)
    elif idade > 150:
        print("Valor para idade incorreto")
        idade = int(redigite("Idade"))
        validacao(qt_letras_nome,idade)
    elif sexo  not in tps_sexo:
        print(" Sexo invalido")
    elif salario <=0:
        print("Salario invalido")
    elif est_civ not in tps_est_civ:
        print ("Estado civil invalido")

    return
    
tps_sexo = "mf"
tps_est_civ = "scvd"

nome = input("Digite o Nome: ")
idade = int(input("Digite a Idade: "))

qt_letras_nome = len(nome)

sexo = input ("Digite o Sexo: \n"+
                "m - masculino \n" +
                "f - feminino \n")
salario = float(input("Digite o Salario: "))

est_civ = input ("Digite o Estado Civil: \n"+
                "s- solteiroo \n" +
                "c - casado \n"+
                " v - viuvo \n"+
                "d - divorciado \n")


validacao(qt_letras_nome,idade, sexo, salario, est_civ)

os.system('cls||clear')

print(f'''
Nome: {nome}
Idade: {idade}
Salario: {salario}
Genero: {sexo}
Estato Civil: {est_civ}
''')