import operator

class Purchases:
    def __init__(self, key,value) -> None:
        self.key = key
        self.value = value
    
    dict_list_purchase = {}

    def register_purchase(self):
        self.dict_list_purchase.update({self.key: self.value})
    
    def show_list_purchase(self, reverse = False):
        dict_desc = sorted(self.dict_list_purchase.items(), key=operator.itemgetter(1), reverse=True)
        dict_asc = sorted(self.dict_list_purchase.items(), key=operator.itemgetter(1))
        if (reverse != False):
            return dict_desc
        return dict_asc

    def create_file(self):
        file = open('/home/botao/Documents/GitHub/python_aplicacoes_web_proway_2021/aula2/AmbienteVirtualAula2/ProjetoListaDeCompras/list_purchase.txt', 'w')
        
        for i in range(len(self.show_list_purchase(reverse=False))):
            format_purchase = str(self.show_list_purchase(reverse=False)[i]).replace(",", " =")
            format_purchase = format_purchase.replace("(", "")
            format_purchase = format_purchase.replace(")", "")
            file.writelines(format_purchase + "\n")
        file.close

count = 0

while (True):
    quest = input("Digite uma fruta: ")
    
    count += 1

    product = Purchases(key= count, value= quest)
    product.register_purchase()

    more_purchase = input("Gostaria de adicionar mais um produto?(S/N) ")

    if (more_purchase.lower() == "s"):
        continue
    elif (more_purchase.lower() == "n"):
        break

print(product.show_list_purchase(reverse= True))
product.create_file()