valor_X = int(input(" digite o valor de X: "))
valor_y = int(input(" digite o valor de y: "))
valor_z = int(input(" digite o valor de z: "))

comp_X = valor_z + valor_y
comp_z = valor_X + valor_y
comp_y = valor_X + valor_z

if valor_X < comp_X and valor_y < comp_y and valor_z < comp_z:
    if valor_X == valor_y == valor_z:
        print(" é um triangulo equilatero")
    if valor_X == valor_y  and valor_X != valor_z or valor_X == valor_z and valor_X != valor_y or valor_y == valor_z and valor_y != valor_X:
       print("é um triangulo isóceles")
    if valor_X != valor_y and valor_y != valor_z and valor_z != valor_X:
        print("é um triangulo escaleno")
else:
    print("não é um triangulo")