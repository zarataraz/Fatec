palavra = input('digite uma palavra: ').lower()
inverso = palavra[::-1]

if inverso == palavra:
    print(f'{palavra} é um palindromo')
else:
    print(f'{palavra} não é um palindromo')
