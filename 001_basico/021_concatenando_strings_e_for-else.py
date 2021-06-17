
# concatenando strings

frase = ''
frase += 'J'  # a string recebe apenas o J
frase += 'u'  # a string recebe o que ela já tem mais o U

print(frase)

"""

digitado = ''
frase_formada = ''


while digitado != 'fim':
    digitado = input('Digite algo para incluir na string, para finalizar digite "fim". ')

    if digitado != 'fim':
        frase_formada += digitado

    print(frase_formada)

"""
# for/else
# o else no for é sempre executado, a não ser que ocorra um break

par = list(range(2, 50, 3))

for i in par:
    print(i)

    if i % 2 == 1:
        print('Existe um número ímpar na lista, programa encerrado')
        break
else:
    print("Só existem número pares na lista")
