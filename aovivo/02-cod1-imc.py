op = "sim"

while op == "sim":
    
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / (altura * altura)

    print("O IMC é: ", imc)

    if imc < 21:
        print("Abaixo do peso.")
    elif imc >= 21 and imc <=30.75:
            print ("Peso padrão.")
    else:
        if imc > 30.75:
            print("Você está acima do peso.")
    
    op = input("Deseja repetir a operação ? (sim/nao) \n")