"""
SOMANDO NÚMEROS
"""

soma = 0 # LISTA (armazena uma fila de números)

while True:
    numero = int(input("Digite um número (0 para parar): "))
    soma += numero
    if numero == 0:
        break

print(f"A soma total é: {soma}")