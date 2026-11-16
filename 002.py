# Lista de itens do cardápio
cardapio = ['pastel', 'pizza', 'coxinha']

# Item que o utilizador quer pedir
pedido = 'refrigerante'

# Verificar se o item está presente na lista
if pedido in cardapio:
    print(f"O item '{pedido}' está no cardápio!")
else:
    print(f"'{pedido}' não está no cardápio. Que tal pedir um destes itens: {', '.join(cardapio)}?")



lista_nomes = ['pastel', 'pizza', 'coxinha']

# Adicionar um novo item à lista
lista_nomes.append('refrigerante')

# Remover um item da lista
lista_nomes.remove('pizza')

# Exibir a lista atualizada
print("Lista de itens atualizada:")
for item in lista_nomes:
    print(f"- {item}")



# Lista de itens do cardápio
cardapio = ['pastel', 'pizza', 'coxinha']

# Item que o utilizador quer pedir
pedido = 'refrigerante'

# Verificar se o item está presente na lista
if pedido in cardapio:
    print(f"O item '{pedido}' está no cardápio!")
else:
    print(f"'{pedido}' não está no cardápio. Que tal pedir um destes itens: {', '.join(cardapio)}?")

# Lista de nomes
lista_nomes = ['pastel', 'pizza', 'coxinha']

# Adicionar um novo item à lista
lista_nomes.append('refrigerante')

# Remover um item da lista
lista_nomes.remove('pizza')

# Exibir a lista atualizada
print("Lista de itens atualizada:")

for item in lista_nomes:
    print(f"- {item}")

# Adicionar mais itens à lista
lista_nomes.append('hambúrguer')
lista_nomes.append('suco')

# Exibir a quantidade de itens
print(f"Quantidade de itens na lista: {len(lista_nomes)}")

# Verificar se um item está na lista
if 'pastel' in lista_nomes:
    print("Pastel está na lista!")

# Exibir todos os itens novamente
print("Cardápio final:")
for item in lista_nomes:
    print(f"- {item}")

lista_comidas = ['pastel', 'pizza', 'coxinha', 'hambúrguer']

lista_comidas.append('lasanha')
lista_comidas.remove('pizza')
lista_comidas.insert(0, 'pizza')
lista_comidas.pop(1)

print(lista_comidas)