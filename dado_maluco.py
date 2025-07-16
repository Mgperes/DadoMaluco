import random
from dado import dado

def decisao_user():
    quant_dados = input("\nVocê quer lançar 1 ou 2 dados? ")
    if quant_dados == '1':
        print("\nVocê escolheu lançar 1 dado.")
        print("\nLançando o dado...")
        dado1 = dado()
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
        dado1 = dado()
        dado2 = dado()
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


def computador_decisao():
    print("\nO computador está lançando os dados...")
    dado1 = dado()
    dado2 = dado()
    if dado1 != 2 and dado1 != 3 and dado2 != 2 and dado2 != 3:
        resultado = dado1 + dado2
        return resultado
    else:
        print("\nEu perdi os pontos dessa rodada, vencerei você na próxima!!")
        return 0
      

        
    
print("\n\nBEM-VINDO AO DADO MALUCO!")
print("\nVocê pode jogar 1 ou 2 dados.")
print("Vamos ver o que o destino reserva para você!")

decisao = str(input("\nVocê quer jogar o dado? (s/n): ").strip().lower())

if decisao == 's':
    
    resultado = 0

    print("\nVocê escolheu jogar!")
    print("\nREGRAS DO JOGO:")  
    print("\n1. O objetivo é chegar a 30 pontos.")
    print("2. Se você tirar 2 ou 3, perde os pontos dessa rodada.")
    print("\nVamos começar!")
    
    while resultado != 30:
        pontos_usuario = decisao_user()
        pontos_computador = computador_decisao()
        
        if pontos_usuario >= 30:
            print(f"\nVocê ganhou! Seus pontos: {pontos_usuario}, Pontos do computador: {pontos_computador}")
        elif pontos_computador >=30 :
            print(f"\nVocê perdeu! Seus pontos: {pontos_usuario}, Pontos do computador: {pontos_computador}")
        else:
            print(f"\nSeus pontos: {pontos_usuario}, Pontos do computador: {pontos_computador}")
            decisao = input("\nVocê quer continuar jogando? (s/n): ").strip().lower()
            if decisao != 's':
                break

        if resultado >= 30:    
            decisao = input("\nVocê quer jogar novamente? (s/n): ").strip().lower()
            if decisao != 's':
                 break
            

    print("\nObrigado por jogar Dado Maluco!")
else:
    print("\nJogo encerrado. Até a próxima!")

