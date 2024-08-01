def tensao():
    while True:
        try:
            tensao = int(input("Digite o valor da tensão elétrica (em Volts): "))
            if tensao > 0:
                return tensao
        except ValueError:
            print("Valor inserido inválido, digite um número inteiro")
def corrente():
    while True:
        try:
            corrente = float(input("Digite o valor da corrente (em Amperes): "))
            if corrente > 0:
                return corrente
        except ValueError:
            print("Valor inserido inválido, digite um número usando o ponto como separador")
def resistencia():
    while True:
        try:
            resistencia = int(input("Digite o valor da resistência (em Ohms): "))
            if resistencia > 0:
                return resistencia
        except ValueError:
            print("Valor inserido inválido, digite um valor inteiro")
def tensao_fonte():
    while True:
        try:
            tensao_fonte = float(input("Digite a tensão elétrica (em Volts) da fonte: "))
            if tensao_fonte > 0:
                return tensao_fonte
        except ValueError:
            print("Valor inserido inválido, digite um valor inteiro")
def tensao_LED():
    while True:
        try:
            tensao_LED = float(input("Digite a tensão elétrica (em Volts) da LED: "))
            if tensao_LED > 0:
                return tensao_LED
        except ValueError:
            print("Valor inserido inválido, digite um valor inteiro")
def corrente_LED():
    while True:
        try:
            corrente_LED = float(input("Digite a corrente elétrica (em Amperes) da LED: "))
            if corrente_LED > 0:
                return corrente_LED
        except ValueError:
            print("Valor inserido inválido, digite um valor inteiro")