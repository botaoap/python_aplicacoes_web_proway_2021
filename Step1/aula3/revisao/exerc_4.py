# Usar Dict para ter mais de um Aluno

dict_student = {}

for x in range(3):
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
    dict_notes = {
        nome: {
            'nota_um': list_notes[0],
            'nota_dois': list_notes[1],
            'nota_tres': list_notes[2],
            'media': round(media,2),
            'status': status_list
        }
    }
    dict_student.update(dict_notes)

for aluno in dict_student.keys():
    print(f"""
    Aluno: {aluno}
    Nota 1: {dict_student[aluno]['nota_um']}
    Nota 2: {dict_student[aluno]['nota_dois']}
    Nota 3: {dict_student[aluno]['nota_tres']}
    Media: {dict_student[aluno]['media']}
    Status: {dict_student[aluno]['status']}
    """)
