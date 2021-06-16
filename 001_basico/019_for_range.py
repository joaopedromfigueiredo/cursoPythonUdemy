"""

For & Range

Range recebe três argumentos

Range (star, stop, step)
Por exemplo, Range (1, 5, 1) == Comece do 1 até o 4, pulando de 1 em 1
Por exemplo, Range (2, 20, 3) == Comece do 2 até o 19, pulando de 3 em 3

"""

nome = 'Francisca Juscelly da Silva'

for n in range(1, 22, 1):  # Irá imprimir do 1 até o 21, pulando de 1 em 1, o 22 não está incluso
    print(n)


for i in nome:  # o "i" é o que está dentro do índice, que no caso são as letras.
    print(i)
