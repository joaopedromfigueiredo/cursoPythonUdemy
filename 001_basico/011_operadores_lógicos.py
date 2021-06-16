
"""

Operadores Lógicos

and == duas condições verdadeiras
or == uma das condições serem verdadeiras
not == inverter a condição

in == Checar se um determinado elemento existe dentro de outro.
not in == Checar se um determinado elemento não existe dentro de outro

"""

# Checar se usuário e senha estão corretos

usuario_cadastrado = 'joaopedromfigueiredo'
senha = 'abcdef'  # senha genérica


usuario_digitado = input('Digite seu nome de usuário ')
password = input('Digite sua senha ')

if usuario_digitado in usuario_cadastrado and password in senha:
    print('Login Feito com Sucesso')
else:
    print('Usuário ou Senha Incorretos')
