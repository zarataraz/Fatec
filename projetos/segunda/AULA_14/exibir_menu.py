from exibir_mensagem import exibir_mensagem
from valida_data import  valida_data
from valida_cpf import valida_cpf
def exibir_menu():

    escolha = int(input("Digite a opção desejada: "))
    while True:
        if escolha != 3 and escolha != 2 and escolha != 1:
            print("escolha uma opção valida")
            return escolha

        else:
            if escolha == 3:
                print("Bye Bye!")
                return escolha
            if escolha == 1:
                a = input("NOME: ")
                a= input("SOBRENOME: ")
                while not (valida_cpf()):
                    print("Digite um CPF VALIDO")
                while not (valida_data()):
                    print("")
                a= input("Renda bruta: ")

                print("Menu de opções: \n 1- Cadastrar \n 2- Exibir frase \n 3- Sair")
                return escolha
            if escolha == 2:
                exibir_mensagem()
                return escolha


