def menu_escolha():
    print("Menu:\n [0] sair \n [1] converter para fahrenheit \n [2] converter para kelvin")
    while True:
        try:
            escolha = int(input("Digite: "))
            if escolha < 0 or escolha > 2:
                print("Valor invalido, digite um numeral entre 0 e 2")
            else:
                return escolha
        except ValueError:
            print("Valor invalido, digite um numeral entre 0 e 2")
def temperatura_c():
    while True:
        try:
            temperatura = float(input("Digite a temperatura em graus celsius: "))
            return temperatura
        except ValueError:
            print("Valor invalido, digite um numeral, usando o ponto como separador")


escolha = 1

while escolha != 0:
    escolha = menu_escolha()
    if escolha == 1:
        conversao_f = temperatura_c() * 1.8 + 32
        print(f"Isso corresponde a {conversao_f} graus fahrenheit")
    elif escolha == 2:
        conversao_k = temperatura_c() + 273
        print(f"Isso corresponde a {conversao_k} graus kelvin")

print("Saindo do programa...")