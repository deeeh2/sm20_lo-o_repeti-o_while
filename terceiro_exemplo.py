"""
DIGITE A SENHA CORRETA
"""
senha_correta = "debinha"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("desbloqueado")
        break
    else:
        print("Senha incorreta! Tente novamente.")