"""

Listas

"""

lista1 = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']

lista3 = lista1 + lista2  # essa operação junta os valores das duas listas em uma só
print("Lista 3: ", lista3, '\n')

lista1.extend(lista2)  # o valor de lista2 será incorporado em lista1
lista2.append('g')  # adicionando o valor "g" a lista2
lista2.insert(0, 'c')  # adicionando o valor "c" no índice 0 da lista2
lista2.pop()  # removendo o último valor da lista2

lista4 = [10, 20, 30, 40, 50, 60, 70, 90, 100]
del(lista4[0:2])  # removendo os valores dos indices 0 e 1, o 2 não está incluído.


primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print("Primos: ", primos)
print("Mínimo da Lista 5: ", min(primos))  # imprime o valor mínimo de uma lista
print("Máximo da Lista 5: ", max(primos), '\n')  # imprime o valor máximo de uma lista

"""

Se usarmos lista = range[1,10] a lista não receberá os valores de 1 a 10, para isso devemos usar a função list

"""

lista5 = list(range(1, 11))  # o 11 não entra na lista
print('Lista 5: ', lista5, '\n')

for i in lista5:  # iterando nos valores da lista
    print(i)

multiplos3 = list(range(0, 100, 3))  # lista dos múltiplos de 3 de 0 a 100
print('Múltiplos de 3 até 100: ', multiplos3, '\n')

tipos_lista = ['João', 28, 1.65, True]
for i in tipos_lista:
    print(f'O elemento {i} é do tipo {type(i)}')
