import random
import pyperclip
import string

def gerar_senha(tamanho=12):
    """Função que gera uma senha aleatória de tamanho 'tamanho'."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    """Função principal que gera e copia a senha."""
    senha = gerar_senha()
    pyperclip.copy(senha)  # Copia a senha para a área de transferência
    print(f"Senha gerada e copiada para a área de transferência: {senha}")
