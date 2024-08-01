while True:
    try:
        num = float(input("Coloque um número para conferir se é positivo ou negativo: "))
        break
    except ValueError:
        print("Valor inserido inálido, digite um numeral.")
    if num > 0:
        print(num, "é um número positivo.")
    elif num < 0:
        print(num, "é um número negativo.")
    else:
        print("o número informado é inválido ou 0 (número neutro)")