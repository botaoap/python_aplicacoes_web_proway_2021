# Colocar Input dos exercicios anteriores

nome = input("Digite nome: ")
list_notes = []

for x in range(3):
    nota = int(input(f"Nota {x + 1}: "))
    list_notes.append(nota)    

media = sum(list_notes) / len(list_notes)

list_media = [7,5,4]
list_result = ["Aprovado", "Recuperação", "Reprovado"]
count = 0

for x in list_media:
    if (media >= x):
        status_list = list_result[count]
        break
    count += 1

print(f"""
Aluno: {nome}
Nota 1: {list_notes[0]}
Nota 2: {list_notes[1]}
Nota 3: {list_notes[2]}
Media: {round(media,2)}
Stattus: {status_list}
""")