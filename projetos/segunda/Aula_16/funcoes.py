def ehprimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(n):
    if n <= 1:
        return 0
    soma = 0
    count = 0
    for num in range(2, n + 1):
        if ehprimo(num):
            count += 1
            soma = soma + num
    return count,soma

def qntcp(total_cabecas,total_pes):

    coelhos = ((total_pes - total_cabecas * 2) / 2)

    if coelhos <= 0:
        patos = ((total_cabecas - coelhos * 4) / 2)
        coelhos = coelhos * -1
        patos = patos - coelhos
        coelhos = coelhos * -1
    else:
        patos = ((total_cabecas - coelhos * 4) / 2)

    patos = int(patos)
    coelhos = int(coelhos)

    return patos,coelhos