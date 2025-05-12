from setuptools import setup, find_packages

setup(
    name="senha-cli",  # Nome do seu pacote
    version="0.1",  # Versão do seu pacote
    packages=find_packages(),  # Encontra os pacotes do seu projeto automaticamente
    install_requires=[
        'pyperclip',  # Lista as dependências do seu projeto
    ],
    entry_points={
        'console_scripts': [
            'senha-cli = senha_cli.gerador_senhas:main',  # Define o comando 'senha-cli' e a função 'main()' que será chamada quando digitado o comando
        ],
    },
)
