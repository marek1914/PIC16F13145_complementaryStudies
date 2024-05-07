"""
Listas:
- Vetores ou Matrizes
- Qualquer tipo de dado
- Dinâmico

"""

print(type([]))

lista1 = [ 14 , 4 , 29 , 8 , 99 , 15 , 143 , 16 , 256 , 23 , 512 , 42 ]
lista2 = [ 'F', 'r', 'a', 'n', 'c', 'e', 's', 'c', 'o', ' ', 'S', 'a', 'c', 'c', 'o' ]
lista3 = []
lista4 = list( range(11) )
lista5 = list( 'Francesco Sacco programando python' )

# Checar se valor está na lista.
if 8 in lista4:
    print('Encontrei o 8')
else:
    print('Não encontrei o 8')

if 18 in lista4:
    print('Encontrei o 18')
else:
    print('Não encontrei o 18')

if 'S' in lista2:
    print('Encontrei a letra S')
else:
    print('Não encontrei a letra S')

# Ordenação de lista.
print( lista1 )
lista1.sort()
print( lista1 )

# Ocorrências de um valor.
print( lista2.count('a') )

# Adicionando valores na lista.
print( lista1 )
lista1.append( 1024 )
print( lista1 )
lista1.append( [4, 8, 15, 16, 23, 42] )
print( lista1 )
lista1.extend( [4, 8, 15, 16, 23, 42] )
print( lista1 )

# Inserindo valor informando posição.
print( lista4 )
lista4.insert(2,99)
print( lista4 )

# Juntando listas.
print( lista1 + lista4 )

# Inverter a lista
print(lista5)
print(lista5[::-1])
lista5.reverse()
print(lista5)

# Tamanho de lista.
print(len(lista5))

# Removendo elemento da lista.
print( lista1 )
print( lista1.pop() )
print( lista1 )
print( lista1.pop( 2 ) )
print( lista1 )

# Apagando a lista.
print( lista1 )
lista1.clear()
print( lista1 )

# Multiplicando a lista
lista1.extend( [ 1 , 2 , 3 ] )
print( lista1 )
print( lista1 * 3 )

# Dividindo lista.
texto = 'Texto longo com espaços para poder separar'
print(texto)
lista6 = texto.split()
print(lista6)
print( ' '.join(lista6) )

# Iterando na lista
for elemento in lista1:
    print( elemento, end=' ')
print()

# Indexando
cores = [ 'Verde' , 'Vermelho' , 'Azul' , 'Roxo' , 'Amarelo' ]
print( cores[ 0 ] )
print( cores[ 1 ] )
print( cores[ 2 ] )
print( cores[ 3 ] )
print( cores[ 4 ] )
print( cores[ -1 ] )
print( cores[ -2 ] )
print( cores[ -3 ] )
print( cores[ -4 ] )
print( cores[ -5 ] )

# Enumarate
for indice, cor in enumerate( cores ):
    print( indice, cor )

# Achando um indice
print( lista4.index( 3 ) )

# Operadores matemáticos.
print( sum(lista4) )
print( min(lista4) )
print( max(lista4) )
print( len(lista4) )

# Desempacotar listas.
print(lista1)
var1, var2, var3 = lista1
print( var1 )
print( var2 )
print( var3 )

# Deep Copy
lista2.clear()
lista2 = lista1.copy()
print( lista1 )
print( lista2 )
lista2.append(4)
print( lista1 )
print( lista2 )

# Shallow Copy
lista2.clear()
lista2 = lista1
print( lista1 )
print( lista2 )
lista2.append(4)
print( lista1 )
print( lista2 )


