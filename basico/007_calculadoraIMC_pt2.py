"""

Cálculo de IMC

"""

nome = 'João Pedro'  # Definindo a variável 'nome' e atribuindo um valor
idade = 28  # Definindo a variável 'idade' e atribuindo um valor
altura = 1.65  # Definindo a variável 'altura' e atribuindo um valor
peso = 90  # Definindo a variável 'peso' e atribuindo um valor

imc = peso / altura**2  # Definindo a variável imc e atribuindo a fórmula de cálculo

print(f'{nome} tem {idade} anos de idade, sua altura é de {altura}m, ele pesa {peso} Kg e seu Índice de Massa Corpórea é de {imc:.2f}')

print('{} tem {} anos de idade, sua altura é de {}m, ele pesa {} Kg e seu Índice de Massa Corpórea é de {:.2f}'.format(nome, idade, altura, peso, imc))

print('{a} tem {b} anos de idade, sua altura é de {c}m, ele pesa {d} Kg e seu Índice de Massa Corpórea é de {e:.2f}'.format(a=nome, b=idade, c=altura, d=peso, e=imc))
