# SIMULACÃO INTERPRETADOR PYTHON

- Um projeto para fins de estudo, que visa simular os processos que ocorrem,
desde o código-fonte até o código máquina, na linguagem Python.
O interpretador simulado é o Cpython, e os seguintes processos, desde a compilação
código fonte em bytecode, e a interpretação do bytecode pela PVM para código máquina, serão
abordados no simulado.

# 1° Fase (Compilação de Código-Fonte em Bytecode)

- Analise Lexica (Tokenização)
- Parsing(Analise Sintática/Parse)
- AST (montar a árvore sintática abstrata) 

# 2° Fase (Bytecode interpretado pela Python Virtual Machine)
- Gerar arquivo .pyc (Bytecode lido pelo PVM)
- Verificar como a Máquina Virtual, implementa a ideia de pilha para interpretar o bytecode


Obs: Alguns desses processos podem ser verificados por algumas bibliotecas nativas

Tokenização:
python -m tokenize -e nome_arquivo.py

Bytecode:

Import dis
