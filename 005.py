itens = ["pizza", "suco", "bolo", "refrigerante"]
precos = [10, 5, 7, 8]

total = 0

print("===== CARDÁPIO DA CANTINA =====")

for i in range(len(itens)):
    print(f"{i + 1} - {itens[i]}: R$ {precos[i]}")

print("-1 - Finalizar pedido")

opcao = 0

while opcao != -1:
    opcao = int(input("\nEscolha um item pelo número: "))

    if opcao == -1:
        break

    if opcao >= 1 and opcao <= len(itens):
        total += precos[opcao - 1]
        print(f"{itens[opcao - 1]} adicionado ao pedido!")
    else:
        print("Opção inválida!")

print("\n===== RESUMO DA COMPRA =====")
print(f"Valor total: R$ {total:.2f}")
print("Obrigado pela preferência!")