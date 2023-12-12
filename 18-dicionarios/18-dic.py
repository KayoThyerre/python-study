produto = {
    'codigo': 0
    'descricao': "",
    'preco': 0.0,
    'quantidade': 0.0
}

produto['codigo'] = int(input("Digite um código do produto: \n"))
produto['descricao'] = input("Digite a descrição do produto: \n")
produto['preco'] = float(input("Digite o preço do produto: \n"))
produto['quantidade'] = float(input("Digite a quantidade em estoque do produto: \n"))

print("Código: ", produto['codigo'])
print("Descrição: ", produto['descricao'])
print("Preço: ", produto[preco])
print("Quantidade: ", produto[quantidade])