primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a primeira nota: "))
terceira_nota = float(input("Digite a primeira nota: "))

media_antes_do_exame = (primeira_nota + segunda_nota + terceira_nota)/3
media_exame = ((6 - (media_antes_do_exame/2))*2)

if media_antes_do_exame < 3.0:
    print("reprovado")
else:
    if media_antes_do_exame < 7.0:
        print(f"deverá fazer exame e tirar no minimo {media_exame}")
    else:
        print("aprovado: ")
