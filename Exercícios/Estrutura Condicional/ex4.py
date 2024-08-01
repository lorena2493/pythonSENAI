while True:
    print("qual número é maior?")
    try:
        num1 = float(input("informe o primeiro número: "))
        break
    except ValueError:
        print("Valor inserido inválido, insira um numeral (se necessário usar ponto como separador). Ex: 2.6")


while True:
    try:
        num2 = float(input("informe o segundo número: "))
        break
    except ValueError:
        print("Valor inserido inválido, insira um numeral (se necessário usar ponto como separador). Ex: 0.4")


if num1 > num2:
  print("o primeiro número é maior")
elif num1 < num2:
  print("o segundo número é maior")
else:
    print("números são iguais ou o valor inserido é inválido")