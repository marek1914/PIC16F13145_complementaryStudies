"""
Recebendo dados do usuário.
"""

# Entrada de Dados.
nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")

# Saída de Dados.
print('Seja bem vindo(a) %s.' % nome)
print('%s tem %s anos.' % (nome, idade))

print('Seja bem vindo(a) {0}.'.format(nome))
print('{0} tem {1} anos.'.format(nome, idade))

print(f'Seja bem vindo(a) {nome}.')
print(f'{nome} tem {idade} anos.')
print(f'{nome} nasceu em {2024 - int(idade)} anos.')
