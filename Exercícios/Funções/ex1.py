import datetime
tempo = datetime.datetime.now()

def nome():
    while True:
        try:
            nome = input('Qual o seu nome? ')
            return nome
        except ValueError:
            print('Por favor, digite apenas nome')


hora = tempo.hour
if hora >= 0 and hora < 6:
    print(f"Boa madruga {nome()}!")
elif hora >= 6 and hora < 12:
    print(f"Bom dia {nome()}!")
elif hora >= 12 and hora < 18:
    print(f"Boa tarde {nome()}!")
elif hora >= 18 and hora < 24:
    print(f"Boa noite {nome()}!")
