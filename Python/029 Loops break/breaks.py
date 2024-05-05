"""
break sai do loop.
"""

for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num, end=' ')
print()

while True:
    comando = input('Sair?')
    if comando == 'sair':
        break
