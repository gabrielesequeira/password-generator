# gerador.py

import random
import string
import argparse
import pyperclip

def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    caracteres = list(string.ascii_lowercase)

    if usar_maiusculas:
        caracteres += list(string.ascii_uppercase)
    if usar_numeros:
        caracteres += list(string.digits)
    if usar_simbolos:
        caracteres += list("!@#$%&*()-_=+")

    if not caracteres:
        raise ValueError("Nenhum conjunto de caracteres foi selecionado.")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def avaliar_forca(senha):
    score = 0
    if any(c.islower() for c in senha): score += 1
    if any(c.isupper() for c in senha): score += 1
    if any(c.isdigit() for c in senha): score += 1
    if any(c in "!@#$%&*()-_=+" for c in senha): score += 1
    if len(senha) >= 12: score += 1

    if score <= 2:
        return "fraca"
    elif score == 3:
        return "média"
    else:
        return "forte"

def main():
    parser = argparse.ArgumentParser(description="Gerador de senhas seguro e personalizável.")
    parser.add_argument('--tamanho', type=int, default=12, help='Tamanho da senha (padrão: 12)')
    parser.add_argument('--maiusculas', action='store_true', help='Incluir letras maiúsculas')
    parser.add_argument('--numeros', action='store_true', help='Incluir números')
    parser.add_argument('--simbolos', action='store_true', help='Incluir símbolos')
    parser.add_argument('--quantidade', type=int, default=1, help='Quantas senhas gerar')
    parser.add_argument('--copiar', action='store_true', help='Copiar a última senha para a área de transferência')
    parser.add_argument('--forca', action='store_true', help='Exibe a força da senha')
    parser.add_argument('--salvar', type=str, help='Salva as senhas em um arquivo .txt')

    args = parser.parse_args()

    senhas = []
    for _ in range(args.quantidade):
        senha = gerar_senha(args.tamanho, args.maiusculas, args.numeros, args.simbolos)
        senhas.append(senha)

    for i, senha in enumerate(senhas):
        print(f"Senha {i+1}: {senha}")
        if args.forca:
            print(f"→ Força: {avaliar_forca(senha)}\n")

    if args.copiar:
        pyperclip.copy(senhas[-1])
        print("Última senha copiada para a área de transferência.")

    if args.salvar:
        with open(args.salvar, 'w') as arquivo:
            for senha in senhas:
                arquivo.write(senha + '\n')
        print(f"Senhas salvas em: {args.salvar}")

if __name__ == '__main__':
    main()
