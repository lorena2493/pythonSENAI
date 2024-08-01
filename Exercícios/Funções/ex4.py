def lado_triangulo():
    while True:
        try:
            lado_triangulo = int(input("Digite o lado do triangulo: "))
            return lado_triangulo

        except ValueError:
            print("Valor inválido, insira um númeral, se necessário, use ponto como separador. Ex: 1.5")
def classificador_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:

        # Equilátero se todos os lados possuem a mesma medida
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        # Isósceles se dois lados possuem a mesma medida
        return "Isósceles"
    else:
        # Escaleno se todos os lados possuem medidas diferentes.
        return "Escaleno"

print("Bem vindo ao Classificador de triangulos")
print("digite o numero de cada lado do triagulo e veja se é equilátero, isósceles ou escaleno")
print("")

lado1 = lado_triangulo()
lado2 = lado_triangulo()
lado3 = lado_triangulo()


lado_triangulos = classificador_triangulo(lado1, lado2, lado3)
print(f"O triângulo é: {lado_triangulos}")
