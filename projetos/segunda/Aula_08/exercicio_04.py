frase = input('escreva uma frase qualquer: ')
conta_A = frase.lower().count("a")
conta_E = frase.lower().count("e")
conta_I = frase.lower().count("i")
conta_O = frase.lower().count("o")
conta_U = frase.lower().count("u")

soma = conta_A+conta_E+conta_I+conta_O+conta_U
print(soma)