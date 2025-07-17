import random
from dado import dado
import time

# Function to create a rainbow effect for the text
# This function will color each letter of the text with a different color
# to create a rainbow effect when printed in the terminal.
def arco_iris(texto):
    cores = [
        '\033[31m', # vermelho
        '\033[33m', # amarelo
        '\033[32m', # verde
        '\033[36m', # ciano
        '\033[34m', # azul
        '\033[35m', # magenta
    ]
    reset = '\033[0m'
    resultado = ''
    for i, letra in enumerate(texto):
        cor = cores[i % len(cores)]
        resultado += f"{cor}{letra}"
    resultado += reset
    return resultado

# Function to handle user's decision on how many dice to roll
def decisao_user():
    while True:
        quant_dados = input("\nVocê quer lançar 1 ou 2 dados? ")
        if quant_dados == '1':
            print("\n\033[0mVocê escolheu lançar 1 dado.")
            print("\nLançando o dado...")
            time.sleep(1)  # Simula um pequeno atraso para aumentar a expectativa
            dado1 = dado()
            time.sleep(1)
            if dado1 != 2 and dado1 != 3:
                resultado = dado1
                print(f"\n\033[032mVocê ganhou {resultado} pontos nesta rodada!\033[0m")
                return resultado
            else:
                print("\n\033[031mVocê perdeu os pontos dessa rodada, que pena!!\033[0m")
                return 0
        elif quant_dados == '2':
            print("\nVocê escolheu lançar 2 dados.")
            print("\nLançando os dados...")
            time.sleep(1)
            dado1 = dado()
            time.sleep(1)
            dado2 = dado()
            time.sleep(1)
            if dado1 != 2 and dado1 != 3 and dado2 != 2 and dado2 != 3:
                resultado = dado1 + dado2
                print(f"\n\033[032mVocê ganhou {resultado} pontos nesta rodada!\033[0m")
                return resultado
            else:
                print("\n\033[031mVocê perdeu os pontos dessa rodada\033[033m, que pena!!")
                return 0
        else:
            print("\n\033[031mOpção inválida. Por favor, escolha 1 ou 2.\033[0m")
            return 0

#Function to the decision of the computer
def computador_decisao():
    print("\nO computador está lançando os dados...")
    time.sleep(1)
    dado1 = dado()
    time.sleep(1)
    dado2 = dado()
    time.sleep(1)
    if dado1 != 2 and dado1 != 3 and dado2 != 2 and dado2 != 3:
        resultado = dado1 + dado2
        return resultado
    else:
        print("\n\033[031mEu perdi os pontos dessa rodada :( \033[033m, vencerei você na próxima!!")
        return 0
      

        
#start of the game
print(arco_iris("\n\nBEM-VINDO AO DADO MALUCO!"))
time.sleep(1)
print("\n\033[33mVocê pode jogar 1 ou 2 dados.")

print("Vamos ver o que o destino reserva para você!")

decisao = str(input("\nVocê quer jogar o dado? (s/n): ").strip().lower())

if decisao == 's':
    pontos_usuario = 0
    pontos_computador = 0
    print("\nVocê escolheu jogar!")
    time.sleep(1)
    print(arco_iris("\nREGRAS DO JOGO:"))
    print("\n\033[033m1. O objetivo é chegar a 30 pontos.")
    print("2. Se você tirar 2 ou 3, \033[031mPERDE OS PONTOS\033[033m dessa rodada.")
    time.sleep(1)
    print("\nVamos começar!")
    
    #loop for the game
    while pontos_usuario < 30 and pontos_computador < 30:
        rodada_usuario = decisao_user()
        pontos_usuario += rodada_usuario
        time.sleep(2)
        rodada_computador = computador_decisao()
        pontos_computador += rodada_computador
        time.sleep(2)
        print(f"\n\033[033mSeus pontos: {pontos_usuario}, Pontos do computador: {pontos_computador}\033[0m")
        time.sleep(2)
        if pontos_usuario >= 30:
            print(f"\n\033[032mVocê ganhou! :) | Seus pontos: {pontos_usuario}, Pontos do computador: {pontos_computador}\033[0m")
            break
        elif pontos_computador >= 30:
            print(f"\n\033[031mVocê perdeu! :0 | Seus pontos: {pontos_usuario}, Pontos do computador: {pontos_computador}\033[0m")
            break
        else:
            decisao = input("\nVocê quer continuar jogando? (s/n): ").strip().lower()
            if decisao != 's':
                break
    print(arco_iris("\nObrigado por jogar Dado Maluco!\n"))
else:
    print(arco_iris("\nJogo encerrado. Até a próxima!\n"))

