"""
Operadores Unários
 - not
Operadores Binários
 - and, or, is
"""

ativo = True
logado = False

if ativo and logado:
    print("Usuário ativo e logado.")
else:
    print("Usuário não ativo e/ou logado.")

if not ativo:
    print("Primeiro ative!")
else:
    print("Já está ativo.")

if ativo is True:
    print("Já está ativo.")
