"""
For - Estrutura de repetição

for item in iterável:
    # Execução

Iteráveis:
  - String
  - Listas
  - Range
"""

# Exemplo 1
nome = "Hello World!"
for letra in nome:
    print(letra, end='')
print()

# Exemplo 2
lista = [1,2,3,5,7,11,13]
for numero in lista:
    print(f'{numero} ', end='')
print()

# Exemplo 3
for numero in range(1, 10):
    print(numero)

# Exemplo 4
nome = "Hello World!"
for valor in enumerate(nome):
    print(valor)

# Exemplo 5
qtd = int(input("Quantas vezes deve rodar?"))
for n in range(1, qtd + 1):
    print(f'Rodando {n}')

# Exemplo 6
for num in range(1,11):
    print('\U0001F60D' * num)
