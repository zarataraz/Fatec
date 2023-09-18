numero_a_ser_dividido = int(input("Digite o numero a ser verificado se a divisão por 3 e 5 será um numero inteiro: "))

divisao_por_3 = numero_a_ser_dividido % 3

divisao_por_5 = numero_a_ser_dividido % 5

if divisao_por_5 == 0 and divisao_por_3 == 0:
    print(f"o numero {numero_a_ser_dividido} é divisivel por 3 e 5 ao mesmo tempo")

else:
    print(f"o numero {numero_a_ser_dividido} não pode ser divido por 3 e 5 ao mesmo tempo")
