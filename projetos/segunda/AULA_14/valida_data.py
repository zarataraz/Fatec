from datetime import datetime

def valida_data():
    hoje = datetime.now().date()
    nasc = input('Digite a data de nascimento no formato: dd/mm/aaaa: ')
    while len(nasc) > 10 or len(nasc) < 10:
        print('Digite uma data válida.')
        return False
    ano = int(nasc[6:10])
    mes = int(nasc[3:5])
    dia = int(nasc[0:2])
    idade = hoje.year - ano
    while idade > 100:
        print('Digite uma data válida.')
        return False

    if dia <= 31 and mes <= 12 and ano <= hoje.year:
        data_nasc = datetime(ano, mes, dia).date()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        if idade < 18:
            print(f"Você deve ter mais de 18 anos para se cadastrar.")
        else:
            return True
    else:
        print('Data inválida, por favor digite uma data válida')
        return False
