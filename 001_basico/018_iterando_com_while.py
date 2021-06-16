# Iterando com While (Percorrendo cada índice)


frase = 'Francisca Juscelly da Silva'
contador = 0

while contador < len(frase):  # Enquanto o contador estiver menor que o tamanho da frase
    print(frase[contador], contador + 1)
    contador += 1

print()
print(f'O nome {frase} tem {len(frase)} caracteres')
