cpf = input('Digite seu cpf, apenas os números: ')
soma1 = 0
soma2 = 0

# Conferindo o décimo dígito do CPF

# Fazendo a multiplicação dos nove primeiros por 10, 9, 8 [...] até o 2 e gerando uma soma:
for i, v in enumerate(range(10, 1, -1)):
    soma1 += int(cpf[i]) * v

# Gerando o décimo digito
condicao_digito10 = 11 - (soma1 % 11)

if condicao_digito10 > 9:
    digito10 = 0
else:
    digito10 = condicao_digito10

# Conferindo o décimo-primeiro dígito do CPF
# Fazendo a multiplicação dos dez primeiros por 11, 10, 9 [...] até o 2 e gerando uma soma:
for j, k in enumerate(range(11, 1, -1)):
    soma2 += int(cpf[j]) * k

# Gerando o décimo primeiro dígito
condicao_digito11 = 11 - (soma2 % 11)
digito11 = condicao_digito11

if condicao_digito11 > 9:
    digito11 = 0
else:
    digito11 = condicao_digito11

novo_cpf = ''

for g in range(0, 9):  # Igualando os nove primeiros dígitos
    novo_cpf += cpf[g]

novo_cpf += str(digito10) + str(digito11)  # Recebendo os últimos dois dígitos gerados

# Conferindo se o CPF digitado é o mesmo do CPF gerado com os dois últimos dígitos
print(f'O CPF {cpf} é válido') if novo_cpf == cpf else print(f'O CPF {cpf} não é válido')
