"""
ADIVINHE O NÚMERO SECRETO
"""

import random

numero_secreto = random.randint(1, 15)
adivinhou = False

while True:
    palpite = int(input("Adivinhe o número (entre 1 e 15): "))
    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break
    else:
        print("Tente novamente!")