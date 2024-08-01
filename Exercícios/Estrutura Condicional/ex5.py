print("DIGITE UM NÚMERO PARA CONFERIR O DIA DA SEMANA CORRESPONDENTE (entre 1 e 7)")
while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("Valor inserido inválido, insira um numral entre 1 e 7")
if num == 1:
  print("O número corresponde a domingo")
elif num == 2:
  print("O número corresponde a segunda-feira")
elif num == 3:
  print("O número corresponde a terça-feira")
elif num == 4:
  print("O número corresponde a quarta-feira")
elif num == 5:
  print("O número corresponde a quinta-feira")
elif num == 6:
  print("O número corresponde a sexta-feira")
elif num == 7:
  print("O número corresponde a sábado")
else:
  print("O número informado é inválido")