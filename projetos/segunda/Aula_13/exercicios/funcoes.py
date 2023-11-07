from math import pi

def validacao(x):
    if x % 2 == 0:
        return "Verdadeiro"
    else:
        return "falso"

def ehprimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def volume_esfera(n):
    volume = (4*pi*(n**3))/3
    return volume


def segundos(h,m,s):
    horas = h*60*60
    minutos = m * 60

    total = minutos+horas+s
    return total

def contar_primos(ate_num):
    if ate_num <= 1:
        return 0
    count = 0
    for num in range(2, ate_num + 1):
        if ehprimo(num):
            count += 1
    return count