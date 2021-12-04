# 10 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
import os

list_nota = []
for i in range(4):
    nota = int(input(f"Nota {i+1}: "))
    list_nota.append(nota)

media = sum(list_nota) / len(list_nota)

os.system("cls||clear")

for i in range(len(list_nota)):
    print(f"Nota {i+1}: {list_nota[i]}")

print(f"Media: {media}")