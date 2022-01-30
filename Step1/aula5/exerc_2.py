# 6 - Faca um programa que leia um nome de usuario e asua senha e nao aceite a senha igual ao nome
# Mostrando uma mensagem de erro e voltando a pedir as informacoes

import os
import time

os.system('cls||clear')
name = input("Digite seu nome: ")

while True:
    pws = input("Digite uma senha: ")

    if (name.lower() == pws.lower()):
        os.system('cls||clear')
        print("Senha inválida. Tente novamente!")
        time.sleep(1)
        os.system('cls||clear')
        continue
    break

print(f"Cadastro efetuado com sucesso, Obrigado {name}!!")