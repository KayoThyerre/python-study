mat = []

for i in range(3):
    linha = []
    for j in range(3):
        print("Insira o elemento da linha", i, "coluna", j)
        dado = int(input())
        linha.append(dado)
    mat.append(linha)
    
for i in range(3):
    for j in range(3):
        print("O elemento da linha", i, "coluna", j, "é: ", mat[i][j])