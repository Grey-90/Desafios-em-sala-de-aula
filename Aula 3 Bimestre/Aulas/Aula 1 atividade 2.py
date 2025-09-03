

import re


def verificar_senha(senha):

    if len(senha) < 8:
        return "Senha muito curta! Mínimo 8 caracteres"

    if not re.search(r"[A-Z]", senha):
        return "A senha deve conter pelo menos uma letra maiúscula."

    if not re.search(r"[a-z]", senha):
        return "A senha deve conter pelo menos uma letra minúscula."

    if not re.search(r"[0-9]", senha):
        return "A senha deve conter pelo menos um número"

    if not re.search(r"[!@#$%&*()\-_=+]", senha):
        return "A senha deve conter pelo menos um caractere especial (!@#$%^&*()-_+=)."


senha_usuario = input("Digite sua senha para verificação:")
resultado = verificar_senha
print(resultado)