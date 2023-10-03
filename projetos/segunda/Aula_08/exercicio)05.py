frase = input('digite a frase: ').lower()
palavra = input('digite a palavra a ser contada dentro da frase: ').lower()

print(f'a palavra {palavra} se repete {frase.count(palavra)} vezes e a frase possui no total {frase.count(" ")+1} palavras')
