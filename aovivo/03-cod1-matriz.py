# mat = []

# for i in range (0, 3, 1):
#     linha = []
#     for j in range (0, 3, 1):
#         print("Informe o elemento da linha", i, ", coluna", j, ":")
#         dado = int(input())
#         linha.append(dado)
#     mat.append(linha)
    
# print(mat)

mat = []

for i in range (0, 3, 1):
    linha = []
    for j in range (0, 3, 1):
        print("Informe o elemento da linha", i, ", coluna", j, ":")
        dado = int(input())
        linha.append(dado)
    mat.append(linha)

for i in range (0, 3, 1):
    print()
    for j in range (0, 3, 1):
        if(i == j):
            print(mat[i][j], " ", end="")
        else:
            print(" 0 ", end="")