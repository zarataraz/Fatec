lista = []
i = 0
while i < 10:
    x = int(input("insira um numero: "))
    lista.append(x)
    i=i+1

tupla = tuple(lista)
print(tupla[::-1])
