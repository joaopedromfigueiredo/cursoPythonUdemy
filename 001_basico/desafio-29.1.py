
numero = input('Digite um número inteiro ')

if numero.isnumeric():
    numero = int(numero)

    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')

else:
    print('O valor digitado não é um número inteiro')
