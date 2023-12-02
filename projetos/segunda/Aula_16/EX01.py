from funcoes import qntcp

total_cabecas = int(input("insira o total de cabeças: "))
total_pes = int(input("insira o total de pés: "))

patos, coelhos = qntcp(total_cabecas, total_pes)


print(f"Total de patos: {patos}")
print(f"Total de coelhos: {coelhos}")
