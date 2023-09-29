numero = []
par = []
res = 0

for c in range (5):
    numero.append(int(input('Digete os numeros da lista: ')))

for c in numero:
    if c % 2 == 0:
        par.append(c)
for c in par:
    res += c 

print(f' A soma dos números pares é: {res}')