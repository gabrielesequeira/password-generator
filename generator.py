import random
import string

def generator( length=12, use_digits = True, use_specials = True):
    characters = string.ascii_letters # letras maúisculas e minúsculas

    if use_digits:
        characters += string.digits #add números (0-9)

    if use_specials:
        characters += string.punctuation #add characteres especiais (!@#$%)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print("🔐 Gerador de Senhas Aleatórias 🔐")

    try:
        length = int(input("Digite o tamanho da senha (padrão: 12): ") or 12)
        use_digits = input("Incluir números? (s/n) ").strip().lower() == 's'
        use_specials = input("Incluir caracteres especiais? (s/n) ").strip().lower() == 's'

        password = generator(length, use_digits, use_specials)
        print (f"\n Senha gerada: {password}")

    except ValueError:
        print("Entrada inválida")