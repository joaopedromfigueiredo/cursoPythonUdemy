lista = ['Juscelly', 'João Pedro', 'Gorette', 'João Figueiredo']

# A lista possui indices que vão do 0 até o tamanho da lista -1

eu = lista[1]
print(eu)

n1, n2, n3, n4 = lista  # Só funciona se o número de variáveis declaradas for do mesmo tamanho da lista

lista2 = list(range(0, 51, 5))
print(lista2)

# as 3 primeiras variáveis receberão os 3 primeiros valores, lista3 irá receber os valores restantes
i1, i2, i3, *lista3 = lista2
print(lista3)

'''

Se eu fizesse *lista3, i1, i2, i3 = lista2, as variáveis soltas receberiam os 3 últimos valores
Esse raciocínio serve também, se a *lista3 estivesse no meio

'''

# Trocando valores de variáveis entre elas:

x = "João"
y = "Juscelly"

x, y = y, x

print(f'O valor de x é {x} e o valor de y é {y}')

# Ao contrário de C e Java, não precisamos criar uma variável temporária, basta fazermos o processo acima.
