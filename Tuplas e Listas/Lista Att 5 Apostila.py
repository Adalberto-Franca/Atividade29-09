listaA = []
listaB = []
listaAux = []

for c in range (5):
    listaA.append(int(input('Digete os numeros da lista A: ')))

for c in range (5):
    listaB.append(int(input('Digete os numeros da lista B: ')))

listaAux = listaA

listaA = listaB
listaB = listaAux

print(f'Os valores da lista A são: {listaA}')
print(f"Os valores da lista B são: {listaB}")

