num = int(input("Digite um número inteiro:"))

resto = int(num / 2)
resto = num - (resto*2)

if resto == 0:
    print("Par.")
else:
    print("impar")
