def soma(num1, num2):
    total.append(num1 + num2)

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

resultado = []

soma(n1, n2, resultado)

print("A soma é", resultado)