lista = []

print("Deseja cadastrar uma pessoa? (y/n)")
op = input()

while op == 'y':
    pessoa = {
        'nome': "",
        'telefone': "",
    }

    print("Insira o nome da pessoa:")
    pessoa['nome'] = input()
    print("Insira o telefone da pessoa:")
    pessoa['telefone'] = input()
    lista.append(pessoa)

    print()
    print("Os dados cadastrados são:")
    print()

    for i, pessoa in enumerate(lista):
        print("Pessoa", i + 1, ":")
        print("Nome:", pessoa['nome'])
        print("Telefone:", pessoa['telefone'])
        print()

    print("Deseja cadastrar outra pessoa? (y/n)")
    op = input()