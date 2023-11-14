def valida_cpf():
    cpf = input('Digite o cpf no formato xxx.xxx.xxx-xx: ')
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    acumulador= 0
    acumulador2 = 0

    if len(cpf_numeros) != 11:
        return False

    if cpf_numeros == cpf_numeros[0] * 11:
        return False
    for i in range(0, 9):
        acumulador = acumulador + (int(cpf_numeros[i]) * (10-i))
    if (acumulador % 11) < 2:
        digito1 = 0
    else:
        digito1 = 11 - (acumulador % 11)

    for i in range(0, 10):
        acumulador2 = acumulador2 + (int(cpf_numeros[i]) * (11-i))
    if acumulador2 % 11 < 2:
        digito2 = 0
    else:
        digito2 = 11 - (acumulador2 % 11)

    if digito1 == int(cpf_numeros[9]) and digito2 == int(cpf_numeros[10]):
            return True
    else:
            return False
