"""
range( valor_de_parada )
range( valor_de_inicio , valor_de_parada )
range( valor_de_inicio , valor_de_parada , passo )
"""

# Forma 1
for num in range( 11 ):
    print(num , end=' ')
print()

# Forma 2
for num in range(1, 11):
    print(num , end=' ')
print()

# Forma 3.1
for num in range(1, 10, 2):
    print(num , end=' ')
print()

# Forma 3.2
for num in range(10, 0, -1):
    print(num , end=' ')
print()
