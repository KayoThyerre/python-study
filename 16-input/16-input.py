nome = input ("Digite seu primeiro nome: \n")
sobrenome = input ("Digite seu sobrenome: \n")

tamanho = len(nome)
print("O comprimento do nome é:", tamanho)

nome = nome + " " + sobrenome
print("Após concatenar as strings temos:", nome)

if sobrenome in nome:
    print("O sobrenome", sobrenome, "está contido no nome", nome, ".")
    
print("O nome completo em minúsculo é:", nome.lower())
print("O nome completo em maiúsculo é:", nome.upper())