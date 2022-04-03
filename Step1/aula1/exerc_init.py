# Criar algoritmo utilisando dia e Mes trazendo um personagem aleatorio

# Dicas
# Pode-se Utilizar listas para guardar os personagens

# # mes = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
# # tipo_mes = ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8", "i9", "j10", "k11", "l12"]
# # tipo_dia = []
# # for i in range(31):
# #     tipo_dia.append(str(i))

# # input_mes = input("Digite o mes: ")
# # input_dia = int(input("Digite o dia: "))

# # record_mes = ""
# # record_dia = ""
# # pos_mes = 0
# # pos_dia = 0

# # for item in mes:
# #     if (item == input_mes):
# #         record_mes = tipo_mes[pos_mes]
# #     pos_mes += 1

# # for item in range(len(tipo_dia)):
# #     pos_dia += 1
# #     if (item+1 == (input_dia)):
# #         record_dia = tipo_dia[pos_dia]

# # print(f"{record_mes} {record_dia}")


dict_mes = {"jan":"a1","fez":"b2","mar":"c3","abr":"d4","mai":"f5","jun":"g6","jul":"h7","ago":"i8","set":"j9","out":"k10","nov":"l11", "dez":"m12"}

tipo_dia = []
[tipo_dia.append(str(i)) for i in range(31)]

input_mes = input("Digite o mes: ")
input_dia = int(input("Digite o dia: "))

print(dict_mes[input_mes] + " " + tipo_dia[input_dia])