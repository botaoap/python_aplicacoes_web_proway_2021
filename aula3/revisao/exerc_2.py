# Colocar condicoes para o aluno
# Aprovado > 7
# Recuperacao entre 5 e 6
# Reprovado < 5

nota_um = 7
nota_dois = 6
nota_tres = 8

media = (nota_um + nota_dois + nota_tres) / 3
nome = "Jorge"

# if (media >= 7):
#     status = "Aprovado"
# elif (media >= 5 and media <= 6):
#     status = "Rcuperação"
# else:
#     status = "Reprovado"

# Forma diferente com lista

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
Primeira nota: {nota_um}
Segunda nota: {nota_dois}
Terceira nota: {nota_tres}
Media: {round(media,2)}
Stattus: {status_list}
""")