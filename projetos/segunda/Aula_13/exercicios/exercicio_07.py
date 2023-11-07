from funcoes import contar_primos

numero = int(input("Digite um número inteiro positivo maior que zero: "))
quantidade_primos = contar_primos(numero)
print(f"A quantidade de números primos entre 1 e {numero} é: {quantidade_primos + 1}")