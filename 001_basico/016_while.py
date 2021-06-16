"""

While: Laço de repetição "enquanto", se mantém rodando enquanto a condição for verdadeira.

"""

x = 0

# Iremos fazer um laço while, que se mantém rodando, enquanto o x for menor ou igual a 5

while x <= 5:
    print(x)
    x = x + 1

print('O programa X encerrou-se \n')

# A função "continue" faz o laço de repetição pular uma rodada do processo.

y = 0

while y <= 5:

    if y == 4:
        y = y + 1  # Usamos essa linha, senão o y seria sempre 4, já que a linha 28 não seria executada
        continue

    print(y)
    y = y + 1

print('O programa Y encerrou-se \n')

# A função "break" faz o laço de repetição encerrar-se se determinada condição for atendida.

z = 0

while z <= 5:

    if z == 4:
        break

    print(z)
    z = z + 1

print('O programa Z encerrou-se \n')

# Detalhe: x = x + 1 pode ser substituído por x += 1
