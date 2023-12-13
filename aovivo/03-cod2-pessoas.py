# Criação da lista vazia para armazenar os dicionários
agenda = []

# Solicita ao usuário o nome e telefone e armazena na lista de dicionários
quantidade_pessoas = int(input("Quantas pessoas deseja adicionar? "))

for i in range(quantidade_pessoas):
    nome = input("Informe o nome da pessoa: ")
    telefone = input("Informe o telefone da pessoa: ")
    contato = {'Nome': nome, 'Telefone': telefone}
    agenda.append(contato)

# Imprime os dados da lista de dicionários
print("\nLista de Contatos:")
for pessoa in agenda:
    print(f"Nome: {pessoa['Nome']} - Telefone: {pessoa['Telefone']}")