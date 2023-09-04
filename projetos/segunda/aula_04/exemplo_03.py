from math import sqrt, pow
print("insira as coordenadas da primeira posição")
primeira_posicao_X = int(input("X: "))
primeira_posicao_Y = int(input("Y: "))


print("insira as coordenadas da segunda posição:")
segunda_posicao_X = int(input("X: "))
segunda_posicao_Y = int(input("Y: "))


diferenca_entre_X = segunda_posicao_X - primeira_posicao_X
diferenca_entre_Y = segunda_posicao_Y - primeira_posicao_Y

distancia_entre_primeira_e_segunda_posição = sqrt(pow(diferenca_entre_X,2) + pow(diferenca_entre_Y,2))

print(round(distancia_entre_primeira_e_segunda_posição, 2))
