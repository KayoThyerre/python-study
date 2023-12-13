print("Quantas pessoas queremos cadastrar ?")
tam = int(input())

lista = []

for i in range(0, tam, 1):
    pessoa = {
        'nome': "",
        'telefone': "",
    }
    print("Insira o nome da pessoa", i+1, ":")
    pessoa['nome'] = input()
    print("Insira o telefone da pessoa", i+1, ":")
    pessoa['telefone'] = input()
    lista.append(pessoa)

print()
print()    
print("Os dados cadastrados foram:")
print()
    
for i in range(tam):
    print("Pessoa", i+1, ":")
    print("Nome", lista[i]['nome'])
    print("Nome", lista[i]['telefone'])
    print()