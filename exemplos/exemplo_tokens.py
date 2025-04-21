import tokenize
from io import BytesIO
""" 
Exemplo:
Captura apenas os tokens textos, ignorando os espaços
e quebras de linhas
"""

def lex(codigo_fonte):
    resultado = []
    tokens = tokenize.tokenize(BytesIO(codigo_fonte.encode('utf-8')).readline)

    for token in tokens:
        tipo_token = token.type
        texto_token = token.string

        if tipo_token == tokenize.NUMBER:
            resultado.append(('NUMBER', texto_token))
        elif tipo_token == tokenize.NAME:
            resultado.append(('NAME', texto_token))
        elif tipo_token == tokenize.OP:
            resultado.append(('OP', texto_token))
        elif tipo_token == tokenize.NEWLINE or tipo_token == tokenize.ENDMARKER:
            continue

        else:
            resultado.append(("OTHER", texto_token))

    return resultado    

codigo_fonte = "print(37 * 5 + 78 - 9)"
tokens = lex(codigo_fonte)
print(tokens)