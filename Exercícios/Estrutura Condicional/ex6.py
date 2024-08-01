print("INFORME 3 NÚMEROS PARA CHECAR QUAL O MAIOR ENTRE ELES")
while True:
    try:
        num1 = int(input("informe o primeiro número: "))
        break
    except ValueError:
        print("Valor inserido inválido, digite um numeral")
while True:
    try:
        num2 = int(input("informe o segundo número: "))
        break
    except ValueError:
        print("Valor inserido inválido, digite um numeral")
while True:
    try:
        num3 = int(input("informe o terceiro número: "))
        break
    except ValueError:
        print("Valor inserido inválido, digite um numeral")
if num1 > num2 and num1 > num3:
    print("o primeiro número é o maior")
elif num2 > num1 and num2 > num3:
    print("o segundo número é o maior")
elif num3 > num2 and num3 > num1:
    print("o terceiro número é o maior")
else:
    print("o valor informado é inválido, insira 3 numerais de valor diferente. Ex: 1, 2 e 3")
