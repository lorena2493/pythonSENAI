from utils import tensao, corrente, resistencia, tensao_fonte, tensao_LED, corrente_LED
medida = int(input("Digite o que deseja fazer? \n [0] Sair da calculadora \n [1] Calcular "))
while medida != 0:
    medida = int(input("\n O que deseja fazer? \n [0] Sair da calculadora \n [1] Calcular Resistência Elétrica \n [2] Calcular Tensão Elétrica"
                   " \n [3] Calcular Corrente elétrica \n [4] Calcular Resistência necessária para um resistor "))
    if medida == 1:
        tensao = tensao()
        corrente = corrente()
        resistencia = tensao / corrente
        print(f"A resistência elétrica é igual a {resistencia} Ω (Ohms)")

    elif medida == 2:
        resistencia = resistencia()
        corrente = corrente()
        tensao = resistencia * corrente
        print(f"A tensão elétrica é igual a {tensao} V (Volts)")

    elif medida == 3:
        tensao = tensao()
        resistencia = resistencia()
        corrente = tensao / resistencia
        print(f"A corrente elétrica é igual a {corrente} A (Amperes)")

    elif medida == 4:
        tensao_fonte = tensao_fonte()
        tensao_LED = tensao_LED()
        corrente_LED = corrente_LED()
        re_resistor = (tensao_fonte - tensao_LED) / corrente_LED
        print(f"A resistência necessária para o resistor é de {re_resistor} Ω (Ohms)")

    else:
        print("\n O valor inserido é inválido ou você saiu da calculadora com sucesso")