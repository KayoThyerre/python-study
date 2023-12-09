def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort() 
    for numero in numeros:
        print(numero, end=' ')

valor1, valor2, valor3 = map(float, input("Digite três valores numéricos reais separados por espaço: ").split())

ordenar_numeros(valor1, valor2, valor3)