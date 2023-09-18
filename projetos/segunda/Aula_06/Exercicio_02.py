
Valor_da_compra = float(input("Digite o valor total da compra: "))
primeiro_desconto = (Valor_da_compra-(Valor_da_compra * 10 / 100))
segundo_desconto = (Valor_da_compra-(Valor_da_compra * 20 / 100))
terceiro_desconto = (Valor_da_compra-(Valor_da_compra * 30 / 100))

if Valor_da_compra < 1000.01:

    print(f" o valor total a ser pago de sua compra é: {primeiro_desconto}")

else:
    if Valor_da_compra > 1000.00 < 5000.01:
        print(f" o valor total a ser pago de sua compra é: {segundo_desconto}")
    else:
        print(f" o valor total a ser pago de sua compra é: {terceiro_desconto}")


