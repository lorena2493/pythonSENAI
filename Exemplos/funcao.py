from datetime import datetime

# menu calculadora
def menu_calculadora():
    print("Calculadora \n 1- adição \n 2- subtração \n 3- multiplicação \n 4- divisão")

# calcular idade
def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

# exibir idade
def exibir_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    print(f"A sua idade é {idade} anos")

# calcular idade
def solicita_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento: "))
            if ano_nascimento > datetime.now().year:
                print("Digite um ano válido")
            else:
                return ano_nascimento
        except ValueError:
            print("Digite um numero inteiro. Exemplo: 1980")


#exibe o menu da calculadora
menu_calculadora()

#exibe idade
ano_nascimento = solicita_ano_nascimento()

exibir_idade(ano_nascimento = ano_nascimento)
