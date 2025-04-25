import tokenize
from io import BytesIO


""" Criando uma lista com tuplas de tokens, capturados pelo
modulo tokenize, ignorando (ENCONDING, NEWLINE e ENDMAKER),
por que a ideia é pegar apenas a string do token"""

def separando_em_tokens(codigo_fonte):
    resultado = []
    tokens = tokenize.tokenize(BytesIO(codigo_fonte.encode('utf-8')).readline)

    for token in tokens:
        if token.type in (tokenize.NEWLINE, tokenize.ENDMARKER, tokenize.ENCODING):
            continue
        else:
            resultado.append((token.type, token.string))
    return resultado        


