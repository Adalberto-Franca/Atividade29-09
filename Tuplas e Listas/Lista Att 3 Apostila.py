def calcular_diferenca(lista):
    if len(lista) == 0:
        return None  
    
    maior = lista[0]
    menor = lista[0]

    for valor in lista:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    return maior - menor

valor = []
n = int(input("Digite o número de elementos na lista: "))

for i in range(n):
    elemento = float(input("Digite o valor do elemento: "))
    valor.append(elemento)

diferenca = calcular_diferenca(valor)

if diferenca is not None:
    print("A diferença entre o maior e o menor elemento é:", diferenca)
else:
    print("A lista está vazia.")