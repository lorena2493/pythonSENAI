# 1. plataforma escolher numero 2. usuario dar um chute 3. plataforma dar dicas até a pessoa acertar
import random
numero_secreto = random.randint(1, 100)

print("\nBem vindo ao jogo 'Adivinhe o número secreto'!. \n Instruções de jogo:\n "
      "1. Aguarde a plataforma escolher um número aleatório entre 1 e 100;"
      " \n 2. Dê um chute; \n 3. Caso esteja errado, a plataforma te dará dicas "
      "até você dar o chute correto. \n \n Boa sorte!! \n")

while True:
    try:
        opcao = int(input("Digite: \n [0] para sair do jogo \n [1] para jogar "))
        if opcao == 0 or opcao == 1:
            break
        else:
            print("Valor inserido inválido. Tente novamente")
    except ValueError:
        print("Valor inserido inválido, Tente novamente")

while opcao != 0:

    while True:
        try:
            chute = int(input("Adivinhe o número: "))
            if chute > 0 and chute <= 100:
                break
            else:
                print("Valor inserido inválido, Tente novamente")
        except ValueError:
            print("Valor inserido inválido, tente novamente")

    if chute == numero_secreto:
        print("\n Você acertou o número secreto, parabéns!")
        while True:
            try:
                opcao = int(input("Digite: \n [0] para sair do jogo \n [1] para jogar "))
                if opcao == 0 or opcao == 1:
                    numero_secreto = random.randint(1, 100)

                    break
                else:
                    print("Valor inserido inválido. Tente novamente")
            except ValueError:
                print("Valor inserido inválido, Tente novamente")

    elif chute < numero_secreto:
        print("O número escolhido é maior que o número inserido, tente novamente")

    elif chute > numero_secreto:
        print("O número escolhido é menor que o número inserido, tente novamente")

print("Você saiu do jogo com sucesso")