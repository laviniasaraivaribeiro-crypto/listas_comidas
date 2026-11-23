lista = [2, 5, 3, 4, 1]

print(lista)

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print(lista)
            numeros = [5, 2]

print(numeros[0] > numeros[1])
print("precisa trocar")
numeros = [5, 2, 3]

for i in range(len(numeros)):
    if numeros[0] > numeros[1]:
        numeros[0], numeros[1] = numeros[1], numeros[0]
    print(numeros)
    numeros = [5, 2, 3]

for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
        print(numeros)
        numeros = [5, 2, 3, 4, 1]

for rodada in range(len(numeros)):
    for i in range(len(numeros) - 1):
        if numeros[i] > numeros[i+1]:
            numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
            print(numeros)
            