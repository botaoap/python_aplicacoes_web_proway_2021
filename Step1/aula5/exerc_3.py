# 7 - Faca um programa que leia e valide as seguintes informacoes:
# Nome: maior que 3 caracteres
# Idade: Entre 0 e 150
# Salario: maior q zero
# Genero: 'f' ou 'm'
# Estado Civil: 's', 'c', 'v', 'd'

import os
import time

os.system('cls||clear')
dict_civil_state = {
            's' : 'Solteiro(a)' ,
            'c' : 'Casado(a)' ,
            'v' : 'Viuvo(a)',
            'd' : 'Divorciado(a)' 
        }
dict_gender = {
        'f' : 'Feminino',
        'm' : 'Masculino'
    }
def status_civil(name, dict_name):
        for i in dict_name.keys():
            if (i == name):
                return False
        return True

while True:
    name = input("Digite seu nome: ")
    if (len(name) < 3):
        print("Nome precisa ter mais q 2 caracteres! ")
        time.sleep(1)
        os.system('cls||clear')
        continue
    break

while True:
    age = int(input("Digite sua idade: "))
    if (age < 0 or age > 150):
        print("Idade Invalida ")
        time.sleep(1)
        os.system('cls||clear')
        continue
    break

while True:
    salary = int(input("Qual seu salario: "))
    if (salary < 0):
        print("Salario Invalido ")
        time.sleep(1)
        os.system('cls||clear')
        continue
    break

while True:
    gender = input("Qual seu genero 'f' ou 'm': ")
    if (gender == "f" or gender == "m"):
        break        
    print("Genero Invalido ")
    time.sleep(1)
    os.system('cls||clear')
    continue

while True:
    civil_state = input("Estado civil 's','c','v' ou 'd': ")
    if (status_civil(civil_state, dict_civil_state)):
        print("Genero Invalido ")
        time.sleep(1)
        os.system('cls||clear')
        continue
    break

print(f'''
Nome: {name}
Idade: {age}
Salario: {salary}
Genero: {dict_gender[gender]}
Estato Civil: {dict_civil_state[civil_state]}
''')