
hora = input('Que horas são? ')

if hora.isnumeric():
    hora = int(hora)

    if 0 <= hora <= 11:
        print(f'Bom dia! São {hora} horas')

    elif 12 <= hora <= 17:
        print(f'Boa Tarde! São {hora} horas')

    elif 18 <= hora <= 23:
        print(f'Boa Noite! São {hora} horas')

    else:
        print('Você deveria ter digitado um valor entre 0 e 24')

else:
    print("O valor digitado não é um número inteiro")
