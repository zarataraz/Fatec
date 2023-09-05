ano_de_nascimento = int(input("coloque seu ano de nascimento: "))
ano_atual = int(input("informe o ano atual: "))
idade = ano_atual - ano_de_nascimento
meses = idade * 12
dias = idade * 365
semanas = idade * 52

print(f"você tem \n {idade} anos\n {meses} meses\n {semanas} semanas\n dias {dias}")
