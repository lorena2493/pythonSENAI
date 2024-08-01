while True:
    print("Você estará aprovado ou reprovado? (Insira duas notas entre 0 e 100)")
    try:
        nota1 = int(input("Coloque a primeira nota "))
        if nota1 > 0 and nota1 < 100:
            break
        else:
            print("Digite um número inteiro entre 0 e 100")
    except ValueError:
        print("Digite um numeral entre 0 e 100. Ex: 50")
while True:
    try:
        nota2 = int(input("Coloque a segunda nota "))
        if nota1 > 0 and nota1 < 100:
            break
        else:
            print("Digite um número inteiro entre 0 e 100")
    except ValueError:
        print("Digite um numeral entre 0 e 100. Ex: 50")
soma = nota1 + nota2
media = soma / 2
if media >= 70:
    print(f"Você foi aprovado com uma média de {media} pontos!")
elif media > 0 < 70:
    print(f"Você foi reprovado com uma média de {media} pontos...")
else:
    print("O valor inserido é inválido")