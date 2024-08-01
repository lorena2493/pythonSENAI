print("Verifque o desconto do Imposto de Renda de acordo com sua renda anual")
desconto = 0
while True:
    try:
        renda_anual = float(input("Qual a sua renda anual? "))
        break
    except ValueError:
        print("Insira um numeral, se necessário use ponto como separador. Ex: 2.50")
if renda_anual > 0 and renda_anual <= 56072:
    desconto = 0
elif renda_anual >= 56072.01 and renda_anual <= 238532:
    desconto = renda_anual * 0.075
elif renda_anual >= 238532.01 and renda_anual <= 522400:
    desconto = renda_anual * 0.15
elif renda_anual >= 522400.01 and renda_anual <= 987600:
    desconto = renda_anual * 0.225
elif renda_anual >= 987600.01:
    desconto = renda_anual * 0.275
print(f"Será descontado R$ {desconto} de sua renda anual")