import tokenize

""" Estou lendo os tokens gerados pelo arquivo 
exemplos_bytecode.py"""

with open('exemplo_bytecode.py', 'rb') as arquivo:
    for token in tokenize.tokenize(arquivo.readline):
        print(token)

"""
O arquivo.py é aberto de forma binaria. Cada texto dentro
do arquivo é tokenizado. E é retornado uma Tupla com as informações
type - Tipo do token
string - texto do token
start/end - Linha e coluna onde começa e termina
line - Trecho do código fonte
"""        