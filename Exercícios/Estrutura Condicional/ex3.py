print("Verifique se você é maior ou menor de idade:")
while True:
    try:
        ano = int(input("Coloque seu ano de nascimento: "))
        idade = 2024 - ano
        if idade > 125:
          print("o valor inserido é inválido")
        elif idade >= 18:
          print("Você nasceu a", idade, "anos atrás")
          print("Você é maior de idade")
        elif idade >= 0 < 18:
          print("Você nasceu a", idade, "anos atrás")
          print("Você é menor de idade")
        else:
          print("o valor inserido é inválido")
    except ValueError:
         print("Valor inserido inválido, insira um numeral entre 1 e 125")