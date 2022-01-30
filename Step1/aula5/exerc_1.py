# 5 - Faca um programa que peca uma nota entre zero e dez.
# Mostre uma mensagem caso o valor seja invalido e continue pedindo ate que o valor seja valido

import os
import time

while True:
    nota = int(input("Digite uma nota de 0 a 10: "))

    if (nota < 0 or nota > 10):
        os.system('cls||clear')
        print("Nota inválida. Digite novamente!!")
        time.sleep(1)
        os.system('cls||clear')
        continue
    else:
        break

print(f"Nota: {nota}")