#quero trabalhar fatiamento com phyton
itens_de_comida_com_cardapio = ['pizza','bolo','salgado','hamburguer']
items_de_bebida_do_cardapio = ['suco','refrigerante','agua', 'café']


# Juntar as listas
cardapio = itens_de_comida_com_cardapio + items_de_bebida_do_cardapio

# Exibir todos os itens
print("Cardápio completo:")
print(cardapio)

# Exibir somente as comidas
print("\nSomente as comidas:")
print(cardapio[0:4])

# Exibir somente as bebidas
print("\nSomente as bebidas:")
print(cardapio[4:])