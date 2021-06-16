nome = 'João Pedro'
altura = 1.65
peso = 89.5
idade = 28
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / altura**2

print(f'{nome} tem {altura}m de altura \n'
      f'Ele pesa {peso}kg e tem {idade} anos de idade, nascendo em {ano_nascimento}\n'
      f'Seu imc é de {imc:.2f}')
