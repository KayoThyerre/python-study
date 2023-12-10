lista = []

for i in range(10):
    print("Digite o elemento da posição", i)
    dado = int(input())
    lista.append(dado)

print("Lista preenchida.")

for i in range(10):
    print("O elemento da posição", i, "é", lista[i])