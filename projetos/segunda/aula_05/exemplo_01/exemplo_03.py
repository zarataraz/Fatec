dia = int(input("entre co o numero do dia: "))

match dia:

    case 1:
        nome = "Domingo"
    case 2:
        nome = "Segunda"
    case 3:
        nome = "terça"
    case 4:
        nome = "quarta"
    case 5:
         nome = "quinta"
    case 6:
        nome = "sexta"
    case 7:
        nome = "sabado"
    case _:

        nome = f" o valor {dia} é invalido"

print(nome)
