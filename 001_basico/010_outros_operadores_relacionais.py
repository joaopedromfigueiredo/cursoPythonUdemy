
"""

Outros Operadores Relacionais

== igualdade
> maior que
>= maior ou igual que
< menor que
<= menor ou igual que
!= diferente de


"""

# Fazer um algoritmo que retorne que uma pessoa só pode fazer um empréstimo se tiver entre 18 e 50 anos

nome = input('Qual é o seu nome? ')
idade = int(input('Qual sua idade? '))

if 18 <= idade <= 50:
    print(f'Você, {nome}, pode fazer um empréstimo')
elif idade < 18:
    print(f'Você, {nome}, NÃO pode fazer um empréstimo pois é muito novo')
elif idade > 50:
    print(f'Você, {nome}, NÃO pode fazer um empréstimo pois está acima da idade permitida')
