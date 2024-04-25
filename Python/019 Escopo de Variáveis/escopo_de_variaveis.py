"""
- Variáveis Globais
  Reconhecidas em todo o programa.
- Variáveis Locais
  Limitado ao bloco onde foram declarados.
"""
numero = 42
print(numero)
print(type(numero))

if numero > 10:
    nova_var1 = 20
    print( "Nova variavel 1 vista de dentro " + str( nova_var1 ) )

print( "Nova variavel 1 vista de fora " + str( nova_var1 ) )

if numero < 10:
    nova_var2 = 20
    print( "Nova variavel 2 vista de dentro " + str( nova_var2 ) )

print( "Nova variavel 2 vista de fora " + str( nova_var2 ) )
