import random
import time

def jogar():
    print("Escolha: \n 1 - Cara \n 2 - Coroa ")

    while True:
        escolha_jogador = input("(1 ou 2): ").lower()
        time.sleep(1)
        opcoes = ["1", "2"]
        if escolha_jogador not in ["1", "2"]:
            print("Escolha uma opção válida.")
            continue
        break

    print("Lançando a moeda")
    time.sleep(0.8)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)

    if escolha_jogador == "1":
        escolhajogador = "Cara"
    else:
        escolhajogador = "Coroa"

    escolha_computador = random.choice(opcoes)

    if escolha_computador == "1":
        resultado = "Cara"
    else:
        resultado = "Coroa"

    if escolha_computador == escolha_jogador:
        print(f"A moeda caiu em {resultado}, você escolheu {escolhajogador}, você ganhou!")
    else:
        print(f"A moeda caiu em {resultado}, você escolheu {escolhajogador}, você perdeu.")
        

    

while True:

    time.sleep(0.8)
    # MENU
    print("============================")
    print("|       CARA OU COROA      |")
    print("============================")

    # FUNÇÃO JOGAR
    jogar()

    time.sleep(2)
    
    # SAIR DO PROGRAMA
    resposta = input(
        ' Digite "sair" para encerrar o programa \n ou pressione enter para jogar novamente \n '
    )
    if resposta == "sair":
        time.sleep(0.8)
        print("Obrigado por usar meu programa, Deus abençoe =)")
        break
    else:
        time.sleep(0.8)
