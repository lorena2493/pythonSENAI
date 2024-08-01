print("INSIRA UM NUMERO PARA VERIFICAR O MÊS CORRESPONDENTE")
while True:
    try:
        num = int(input("Insira um numeral entre 1 e 12: "))
        if num >= 1 and num <= 12:
            break
    except ValueError:
        print("Valor inserido inválido. Insira um numeral")
if num == 1:
    print("O número corresponde a janeiro")
elif num == 2:
    print("O número corresponde a fevereiro")
elif num == 3:
    print("O número corresponde a março")
elif num == 4:
    print("O número corresponde a abril")
elif num == 5:
    print("O número corresponde a maio")
elif num == 6:
    print("O número corresponde a junho")
elif num == 7:
    print("O número corresponde a julho")
elif num == 8:
    print("O número corresponde a agosto")
elif num == 9:
    print("O número corresponde a setembro")
elif num == 10:
    print("O número corresponde a outubro")
elif num == 11:
    print("O número corresponde a novembro")
elif num == 12:
    print("O número corresponde a dezembro")
else:
    print("O número informado é inválido")
