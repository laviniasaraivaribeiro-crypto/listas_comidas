itens = ["pizza", "suco", "bolo", "refrigerante"]
precos = [10, 5, 7, 8]

total = 0

print("CARDÁPIO")
for i in range(len(itens)):
    print(i + 1, "-", itens[i], "- R$", precos[i])

while True:
    escolha = int(input("Digite o número do item ou -1 para finalizar: "))

    if escolha == -1:
        break

    if escolha >= 1 and escolha <= len(itens):
        posicao = escolha - 1
        total = total + precos[posicao]
        print(itens[posicao], "adicionado ao pedido!")
    else:
        print("Opção inválida. Tente novamente.")

print("O valor total da compra é: R$", total)
