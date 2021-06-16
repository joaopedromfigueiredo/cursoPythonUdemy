"""

Manipulando strings

"""

# Acessando indices de strings

nome = 'Juscelly'
qtde_caracteres = len(nome)

print(qtde_caracteres)

# Juscelly tem 8 caracteres, logo, o indice da string formada vão de 0 a 7, onde o J da primeira posição tem indice 0

print(f'A primeira letra de {nome} é {nome[0]}')
print(f'A segunda letra de {nome} é {nome[1]}')
print(f'A terceira letra de {nome} é {nome[2]}')
print(f'A quarta letra de {nome} é {nome[3]}')
print(f'A quinta letra de {nome} é {nome[4]}')
print(f'A sexta letra de {nome} é {nome[5]}')
print(f'A sétima letra de {nome} é {nome[6]}')
print(f'A oitava letra de {nome} é {nome[7]}')

# Podemos também fatiar uma string, mostrando apenas determinados indices

print(nome[2:5]) # imprimir a variável "nome" apenas do indice 2 a 5


# Podemos também acessar os elementos de uma string usando números negativos, por exemplo -1 mostra o último indice, -2 o penultimo, e assim por diante

print(nome[-1])
print(nome[-2])
print(nome[-3])

# Pode ser impresso também pulando caracteres, o sinal de :: faz isso, enquanto que o intervalo [0::2] indica "a partir do 0 de 2 em 2"

print(nome[0::2])
