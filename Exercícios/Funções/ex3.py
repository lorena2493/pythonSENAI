def recolhe_numero():
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Digite um numeral, se necessário, use um ponto final como separador. Ex: 1.5")


def menu_escolha():
    print("Menu:\n [0] sair \n [1] adição \n [2] subtração \n [3] multiplicação \n [4] divisão \n ")
    while True:
        try:
            escolha = int(input("Digite: "))
            if escolha >= 0 and escolha <= 4:
                return escolha
            else:
                print("Valor invalido, digite um número inteiro entre 0 e 4")
        except ValueError:
            print("Valor invalido, digite um numeral entre 0 e 4")


def exibe_resultado(resultado):
    print(resultado)

def adicao(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtracao(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicacao(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def divisao(numero1, numero2):
    resultado = numero1 / numero2
    return resultado

def operacao_numeros(escolha, numero1, numero2):

    while escolha != 0:

        if escolha == 1:
            return adicao(numero1, numero2)
        elif escolha == 2:
            return subtracao(numero1, numero2)
        elif escolha == 3:
            return multiplicacao(numero1, numero2)
        elif escolha == 4:
            return divisao(numero1, numero2)

print("Bem-vindo a calculadora!")

escolha = menu_escolha()
while escolha != 0:

    numero1 = recolhe_numero()
    numero2 = recolhe_numero()
    operacao = operacao_numeros(escolha, numero1, numero2)
    exibe_resultado(operacao)
    escolha = menu_escolha()