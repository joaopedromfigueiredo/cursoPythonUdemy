# A função split divide uma string e podemos retorna-la em uma lista

frase = 'Esse curso de Python é interessante, fácil e divertido'
lista1 = frase.split(' ')  # criando uma lista em que os elementos estão em "frase", separados por espaço

print(lista1)

lista2 = frase.split(',')  # criando uma lista em que os elementos estão em "frase", separados por vírgula

print(lista2)

for palavra in lista1:
    print(f'A palavra {palavra} apareceu {lista1.count(palavra)} vezes na lista')

# A função join converte uma lista em uma string

frase2 = '-'.join(lista1)  # convertendo lista1 em uma string novamente, utilizando traço como separador

print(frase2)

# A função enumerate numera os itens de uma lista

for i, v in enumerate(lista1):
    print(i, v)  # o v poderia ser substituído por lista[i]

