import dataset

# Conectando ao banco de dados em memória
db = dataset.connect('sqlite:///:memory:')

# Criando ou acessando a tabela "contacts"
contacts = db['contacts']

# Funções do CRUD
# CREATE: Adicionar um novo contato
def add_contact(name, phone):
    contacts.insert(dict(name=name, phone=phone))
    print(f"Contato {name} adicionado com sucesso!")

# READ: Ler todos os contatos
def get_contacts():
    for contact in contacts:
        print(f"Nome: {contact['name']}, Telefone: {contact['phone']}")

# UPDATE: Atualizar o telefone de um contato existente
def update_contact(name, new_phone):
    contact = contacts.find_one(name=name)
    if contact:
        contacts.update(dict(id=contact['id'], name=name, phone=new_phone), ['id'])
        print(f"Telefone de {name} atualizado para {new_phone}.")
    else:
        print(f"Contato {name} não encontrado.")

# DELETE: Remover um contato
def delete_contact(name):
    contact = contacts.find_one(name=name)
    if contact:
        contacts.delete(id=contact['id'])
        print(f"Contato {name} removido com sucesso.")
    else:
        print(f"Contato {name} não encontrado.")

# Demonstração
add_contact("Luis", "1234-5678")
add_contact("Joana", "9876-5432")

print("\nLista de contatos:")
get_contacts()

update_contact("Luis", "5555-5555")
delete_contact("Joana")

print("\nLista de contatos atualizada:")
get_contacts()
