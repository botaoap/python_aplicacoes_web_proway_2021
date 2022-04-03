# 1 - Criar jogo da forca (Sem necessidade de classes(DEFs))

# O que é necessario para o jogo da forca:
# - palavra chave
# - verificar de acertou ou errou

import os
import time

key_word = "abacaxi"
key_word_lower = key_word.lower()

list_answer = []
timing_stop = 2
gb_hit = 0
gb_miss = 0

def clear_terminal():
    os.system('cls||clear')

def stop_terminal(timer):
    time.sleep(timer)

def setup_errou():
    print("Errou")
    stop_terminal(timing_stop)
    clear_terminal()

def setup_acertou():
    print("Acertou")
    stop_terminal(timing_stop)
    clear_terminal()

def setup_exist():
    print("Errou. Essa letra ja foi!")
    stop_terminal(timing_stop)
    clear_terminal()

def stick_err(count):
    msg = ""
    if count == 1:
        msg = """  
         0  
        """
    elif count == 2:
        msg += """
         0
        / 
        """
    elif count == 3:
        msg += """ 
         0
        /|  
        """
    elif count == 4:
        msg += """ 
         0
        /|\ 
        """
    elif count == 5:
        msg += """ 
         0
        /|\ 
        / 
        """
    elif count >= 6:
        msg += """ 
         0
        /|\ 
        / \ 
        """
    return msg

clear_terminal()


while True:
    if (gb_miss >= 6):
        clear_terminal()
        stop_terminal(timing_stop)
        print("Voce perdeu!")
        print(stick_err(gb_miss))
        break
    trying = input("Digite uma letra: ").lower()

    if (trying in list_answer):
        setup_exist()
        gb_miss+=1
    elif (trying not in key_word_lower):
        setup_errou()
        gb_miss+=1
    else:
        setup_acertou()
        gb_hit += key_word_lower.count(trying)
        if (gb_hit == len(key_word_lower)):
            print("Parabens, voce acertou todas as letras!")
            print(f"A palavra era: {key_word_lower}")
            stop_terminal(timing_stop)
            break
    print(stick_err(gb_miss))
    list_answer.append(trying)
    continue