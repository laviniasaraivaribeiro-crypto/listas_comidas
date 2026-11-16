# Gerando números aleatórios
import random

numero = [10, 67, 7, 4, 3, 2, 1, 5, 6, 8, 9]

random.shuffle(numero)  # Embaralha a lista

sorteado = numero[0]
numero.remove(sorteado)

print(f'Número sorteado: {sorteado}')
print(f'Lista atualizada: {numero}')

print('--------------------')

# Números aleatórios
numeros = []

while len(numeros) < 10:
    numero = random.randint(1, 100)

    if numero not in numeros:
        numeros.append(numero)

print(f'Lista de números: {numeros}')