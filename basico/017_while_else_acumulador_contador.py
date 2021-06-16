"""

While/Else

Acumulador/Contador

"""


contador = 1
acumulador = 1


while contador <= 30:
    print(contador, acumulador)
    acumulador = acumulador + contador  # acumula um valor recursivamente
    contador += 1
else:  # executado depois do while acabar, se tiver um "break" não é executado
    print("Acabou!")
