import datetime
tempo = datetime.datetime.now()

hora = tempo.hour
if hora >= 0 and hora <= 6:
    print("Boa madrugada!")
elif hora >= 6 and hora <= 12:
    print("Bom dia!")
elif hora >= 12 and hora <= 18:
    print("Boa tarde!")
elif hora >= 18 and hora <= 24:
    print("Boa noite!")

while True:
    try:
        escolha = int(input("Digite para exibir: \n [1] data (dia/mes/ano) \n [2] horário atual \n [3] dia da semana \n [4] todos acima"))
        if escolha >= 1 and escolha <= 4:
            break
        else:
            print("Valor inválido, insira um numeral entre 1 e 4")
    except ValueError:
        print("Valor inválido, insira um número inteiro. Ex: 3")

minuto = tempo.minute
segundo = tempo.second

dia = tempo.day

num_semana = tempo.strftime("%w")
dia_semana = ""

if num_semana == "0":
    dia_semana = "domingo"
elif num_semana == "1":
    dia_semana = "segunda-feira"
elif num_semana == "2":
    dia_semana = "terça-feira"
elif num_semana == "3":
    dia_semana = "quarta-feira"
elif num_semana == "4":
    dia_semana = "quinta-feira"
elif num_semana == "5":
    dia_semana = "sexta-feira"
elif num_semana == "6":
    dia_semana = "sábado"


num_mes = tempo.strftime("%m")
mes = ""

if num_mes == "01":
    mes = "Janeiro"
elif num_mes == "02":
    mes = "Fevereiro"
elif num_mes == "03":
    mes = "Março"
elif num_mes == "04":
    mes = "Abril"
elif num_mes == "05":
    mes = "Maio"
elif num_mes == "06":
    mes = "Junho"
elif num_mes == "07":
    mes = "Julho"
elif num_mes == "08":
    mes = "Agosto"
elif num_mes == "09":
    mes = "Setembro"
elif num_mes == "10":
    mes = "Outubro"
elif num_mes == "11":
    mes = "Novembro"
elif num_mes == "12":
    mes = "Dezembro"

ano = tempo.strftime("%Y")

if escolha == 1:
    print(f"Data: {dia}/{num_mes}/{ano}")
elif escolha == 2:
    print(f"Horário atual: {hora}:{minuto}:{segundo}")
elif escolha == 3:
    print(f"Dia da semana: {dia_semana}")
elif escolha == 4:
    print(f"Hoje é {dia_semana}, dia {dia} de {mes} de {ano}. Agora são {hora}:{minuto}:{segundo}")