"""
Tipo String
"""

# Áspas simples
texto = 'Aspas simples'
print(texto)
print(type(texto))

# Áspas Duplas
texto = "Aspas duplas"
print(texto)
print(type(texto))

# Áspas simples triplas
texto = '''Aspas simples triplas'''
print(texto)
print(type(texto))

# Áspas simples
texto = """Aspas duplas triplas"""
print(texto)
print(type(texto))

# Escape
texto = "Francesco's test"
print(texto)
print(type(texto))

# New Line
texto = "Linha 1 \n Linha 2"
print(texto)
print(type(texto))

# Upper
texto = "Francesco's test"
print(texto.upper())

# Lower
texto = "Francesco's test"
print(texto.lower())

# Split
texto = "Francesco's test"
print(texto.split())

# Slice. O último índice não é incluído.
texto = "Francesco's test"
print(texto[0:9])

# Split indexado
texto = "Francesco's test"
print(texto.split()[1])

# Do primeiro ao último invertendo
texto = "Francesco's test"
print(texto[::-1])

# Substituir
texto = "Francesco's test"
print(texto.replace('c', 'C'))
