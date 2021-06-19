

n = int(input('Digite um número inteiro qualquer: '))

if n % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

# Em python também podemos fazer da seguinte forma:

print('O número é par') if n % 2 == 0 else print('O número é ímpar')

expoente = n**2 if n % 2 == 0 else n**3
print(expoente)

'''
Um If/Else pode ser simplificado com a condicional or

Por exemplo:

'''

nome = input('Digite seu nome: ')
print(nome or 'Você não digitou nada')  # A primeira condição verdadeira será impressa no log

