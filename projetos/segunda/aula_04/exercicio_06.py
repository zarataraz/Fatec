salario = float(input("\ninforme seu salario atual: "))
aumento = float(input("informe o percentual de aumento: "))
aumento_salario = aumento * salario / 100 + salario
print(f"com um aumento de {aumento}% seu salario vai ser --> R$ {round(aumento_salario, 2)}")
