lista = []
menor = 100000
indice = 0

for c in range(5):
    lista.append(int(input('Digite os valores da lista: ')))
    if lista[c] < menor:
        menor = lista [c]
        indice = c

print(f'O menor numero da lista é: {menor} e sua posiçao é: {indice}.')