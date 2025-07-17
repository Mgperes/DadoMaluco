import random
from dado import dado
import time

# Function to handle user's decision on how many dice to roll
def decisao_user():
    while True:
        quant_dados = input("\nVocê quer lançar 1 ou 2 dados? ")
        if quant_dados == '1':
            print("\nVocê escolheu lançar 1 dado.")
            print("\nLançando o dado...")
            time.sleep(1)  # Simula um pequeno atraso para aumentar a expectativa
            dado1 = dado()
            time.sleep(1)
            if dado1 != 2 and dado1 != 3:
                resultado = dado1
                print(f"\nVocê ganhou {resultado} pontos nesta rodada!")
                return resultado
            else:
                print("\nVocê perdeu os pontos dessa rodada, que pena!!")
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
                print(f"\nVocê ganhou {resultado} pontos nesta rodada!")
                return resultado
            else:
                print("\nVocê perdeu os pontos dessa rodada, que pena!!")
                return 0
        else:
            print("\nOpção inválida. Por favor, escolha 1 ou 2.")
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
        print("\nEu perdi os pontos dessa rodada, vencerei você na próxima!!")
        return 0
      

        
#start of the game
print("\n\nBEM-VINDO AO DADO MALUCO!")
time.sleep(1)
print("\nVocê pode jogar 1 ou 2 dados.")

print("Vamos ver o que o destino reserva para você!")

decisao = str(input("\nVocê quer jogar o dado? (s/n): ").strip().lower())

if decisao == 's':
    pontos_usuario = 0
    pontos_computador = 0
    print("\nVocê escolheu jogar!")
    time.sleep(1)
    print("\nREGRAS DO JOGO:")  
    print("\n1. O objetivo é chegar a 30 pontos.")
    print("2. Se você tirar 2 ou 3, perde os pontos dessa rodada.")
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
        print(f"\nSeus pontos: {pontos_usuario}, Pontos do computador: {pontos_computador}")
        time.sleep(2)
        if pontos_usuario >= 30:
            print(f"\nVocê ganhou! Seus pontos: {pontos_usuario}, Pontos do computador: {pontos_computador}")
            break
        elif pontos_computador >= 30:
            print(f"\nVocê perdeu! Seus pontos: {pontos_usuario}, Pontos do computador: {pontos_computador}")
            break
        else:
            decisao = input("\nVocê quer continuar jogando? (s/n): ").strip().lower()
            if decisao != 's':
                break
    print("\nObrigado por jogar Dado Maluco!")
else:
    print("\nJogo encerrado. Até a próxima!")

