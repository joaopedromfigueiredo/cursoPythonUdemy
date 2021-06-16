
nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print(f'Seu nome é curto, possui apenas {len(nome)} letras')
elif 5 <= len(nome) <= 9:
    print(f'Seu nome é normal, possui {len(nome)} letras')
else:
    print(f'Seu nome é grande, possui {len(nome)} letras')
