print("insira abaixo as dimenções do aposento e o tamanho da lata de tinta:")
largura = float(input("largura: "))
comprimento = float(input("comprimento: "))
tamanho_lata = int(input("selecione pelo numero o tamanho da lata em litros 1 = Litro 1L / 2 = galão 3l / 3 = LATA 18L "))

parede_largura = ((largura * 2.8)*2 - (0.8 * 2.10))
parede_comprimento = ((comprimento * 2.8) * 2)
area_total = parede_comprimento + parede_largura
lata = round((area_total / 3) / 18 + 0.5)
galao = round((area_total / 3) / 3 + 0.5)
litro = round((area_total / 3) + 0.5)



if tamanho_lata > 3 or tamanho_lata < 1:
    print(" o tamanho indicado é invalido selecione um valor valido ( 1 ,2 ou 3)")
else:
    print(f"o tamanho total do comodo é de {area_total}m²")
    if tamanho_lata == 1:
        print(f" serão nescessarios {area_total / 3} litros de tinta totalizando a compra de {litro}para pintar o comodo")
    else:
        if tamanho_lata == 2:
            print(f" serão nescessarios {area_total / 3} litros de tinta totalizando a compra de  {galao} galões")
        else:
            print(f" serão nescessarios {area_total / 3} litros de tinta totalizando a compra de {lata} latas")
