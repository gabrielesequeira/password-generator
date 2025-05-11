# setup.py

from setuptools import setup, find_packages

setup(
    name="senha-cli",  # Nome do seu projeto
    version="1.0.0",  # Versão do seu projeto
    description="Gerador de senhas seguro e personalizável",  # Descrição breve
    author="Seu Nome",  # Seu nome ou nome da sua organização
    author_email="seuemail@exemplo.com",  # Seu e-mail
    packages=find_packages(),  # Automaticamente encontra todos os pacotes
    install_requires=[
        "pyperclip",  # Dependências do seu projeto
    ],
    entry_points={
        "console_scripts": [
            "senha-cli = senha_cli.gerador:main",  # Define a entrada do CLI
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",  # Versões de Python suportadas
        "License :: OSI Approved :: MIT License",
    ],
)
