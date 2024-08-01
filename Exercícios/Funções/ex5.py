#Majú e lolo 💋❤
def medida_peso():
    while True:
        try:
            medida_peso = float(input("Digite seu peso em kg: "))
            if medida_peso > 0:
                return medida_peso
            else:
                print("Digite um valor maior que zero")
        except ValueError:
            print("Valor inválido, insira um numero")


def medida_altura():
    while True:
        try:
            medida_altura = float(input("Digite sua altura em metros: "))
            if medida_altura > 0:
                return medida_altura
            else:
                print("Digite um valor maior que zero")
        except ValueError:
            print("Valor inválido, insira um numero")


def calculo_imc():
    peso = medida_peso()
    altura = medida_altura()
    imc = peso / (altura * altura)
    return imc


def classificador():
    imc = calculo_imc()
    if imc < 18.5:
        classificador = "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        classificador = "Peso ideal"
    elif imc >= 25 and imc < 30:
        classificador = "Sobrepeso"
    elif imc >= 30 and imc < 35:
        classificador = "Obesidade grau I"
    elif imc >= 35 and imc < 40:
        classificador = "Obesidade grau II"
    elif imc >= 40:
        classificador = "Obesidade grau III"

    return classificador


print("Bem vindo a calculadora de IMC")
print(f"O seu IMC está na faixa {classificador()}")