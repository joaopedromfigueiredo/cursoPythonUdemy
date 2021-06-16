"""

Formatação de valores com modificadores

:s -> string
:d -> int
:f -> float
:.(numero)f -> quantidade de casas decimais em um float
:(caractere)><^(quantidade -> Quantidade de caracteres antes de um variável #Exemplo 1

"""

# Exemplo 1 - Mostrar o número  5 em um caractere de 10 dígitos

nome = 'João Pedro'

print(f'{nome:#>15}')

""" 
Posso fazer a mesma coisa com a função ljust, quando você quer colocar os caracteres a direita da variável,
porém ljust não funciona com valores int

"""
print(nome.ljust(15, '#'))

print(nome.lower())  # Tudo minúsculo
print(nome.upper())  # Tudo maiúsculo
print(nome.title())  # Primeiras letras de cada palavra maiúscula
print(nome.capitalize())  # Primeira letra maiúscula
