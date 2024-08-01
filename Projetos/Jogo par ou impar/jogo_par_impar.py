import random
numero_aleatorio = random.randint(1, 10)

print(" \nBem-vindo ao jogo 'Par ou Impar?'! \n \nIntruções de jogo: \n 1. Escolha se quer apostar no par ou no impar "
      "\n 2. Escolha um número de 1 a 10 \n 3. Aguarde o programa escolher um número aleatório e somar "
      "e verificar se é par ou impar \n Quem apostou na opção correta ganha!!")

while True:
    try:
        opcao_escolhida = int(input("Digite: \n [0] Sair do jogo \n "
                                    "[1] para apostar na opção 'par' \n [2] para apostar na opção 'impar' "))
        if 0 < opcao_escolhida < 3:
            break
        else:
            print("Valor inserido inválido. Tente novamente")
    except ValueError:
        print("Digite '0' ou '1' ou '2'")

while opcao_escolhida != 0:
    while True:
        try:
            numero_escolhido = int(input("Digite um número de 1 a 10: "))
            soma = numero_escolhido + numero_aleatorio
            resto = soma % 2
            print(f"O sistema escolheu o número {numero_aleatorio}")
            print(f"A soma foi igual a {soma}")
            if numero_escolhido > 0 and numero_escolhido < 10:
                break
        except ValueError:
            print("Digite um numeral entre 1 a 10")
    if resto == 0:
        opcao_vencedora = 1
        if opcao_escolhida == opcao_vencedora:
            print("Você venceu porque o resultado da soma é um número par, parabéns!!")
        else:
            print("Não foi dessa vez, o resultado é um número par, sinto muito...")
    else:
        opcao_vencedora = 2
        if opcao_escolhida == opcao_vencedora:
            print("Você venceu porque o resultado da soma é um número ímpar, parabéns!!")
        else:
            print("Não foi dessa vez, o resultado é um número ímpar, sinto muito...")
    while True:
        try:
            opcao_escolhida = int(input("Digite: \n [0] Sair do jogo \n "
                                        "[1] para apostar na opção 'par' \n [2] para apostar na opção 'impar' "))
            if 0 < opcao_escolhida < 3:
                break
            else:
                print("Valor inserido inválido. Tente novamente")
        except ValueError:
            print("Digite '0' ou '1' ou '2'")

print("Você saiu do jogo com sucesso")