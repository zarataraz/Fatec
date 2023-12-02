from funcoes import ehprimo, contar_primos

n1 = int(input("insira um numero inteiro: "))

retorno = ehprimo(n1)

if retorno == True:
    print(f"{n1} é primo")
else:
    print(f"{n1} não é primo")

retorno2, retornosoma = contar_primos(n1)

print(f"a soma dos numeris primos até {n1} é {retornosoma}")