# senha-cli

Um gerador de senhas aleatórias via linha de comando, com opção de cópia automática para a área de transferência.

## Funcionalidades

- Geração de senhas fortes com letras, números e símbolos.
- Cópia automática da senha para a área de transferência.
- Interface simples de linha de comando (CLI).
- Empacotamento como utilitário instalável com `setup.py`.

## Pré-requisitos

- Python 3.8 ou superior
- `pip` instalado

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/password-generator.git
cd password-generator
```

### 2. Crie e ative o ambiente virtual

**No Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**No macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

### 4. Instale o projeto localmente em modo editável

```bash
pip install -e .
```

### 5. Execute o utilitário

```bash
senha-cli
```

A senha gerada será exibida no terminal e automaticamente copiada para a área de transferência.

---

## Estrutura do Projeto

```
password-generator/
├── senha_cli/
│   ├── __init__.py
│   └── gerador_senhas.py
├── requirements.txt
└── setup.py
```

