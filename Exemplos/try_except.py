# O WHILE REPETE TUDO QUE ESTÁ DENTRO DELE
while True:
    # O TRY VAI TENTAR EXECUTAR ESSE BLOCO DE CÓDIGO
    try:
        idade = int(input("Digite sua idade em numeral: "))
        # O IF VERIFICA SE A INFORMAÇÃO É VALIDA
        if idade > 0 and idade <= 120:
            # O BREAK SAI DO WHILE
            break
        else:
            print("Valor inserido inválido. Tente novamente")
    #CASO DER ERRO, EXECUTA AQUI
    except ValueError:
        print("Digite um número inteiro válido. Ex: 10 ")
print("Idade: ", idade)