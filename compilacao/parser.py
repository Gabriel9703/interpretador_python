from compilacao.lexer import lex
from compilacao.ast_nodes import Numero, BinaryOP, Print
import tokenize

def parse(codigo_fonte):
    tokens = lex(codigo_fonte)
    pos = 0

    def match(tipo_esperado, valor_esperado=None):
        nonlocal pos
        tipo_token, valor_token = tokens[pos]
        if tipo_token == tipo_esperado and (valor_esperado is None or valor_token == valor_esperado):
            pos += 1
            return valor_token
        raise SyntaxError(f"Esperado {valor_esperado} mas veio {valor_token}")
    
    match(tokenize.NAME, 'Print')
    match(tokenize.OP, '(')

    esquerda = Numero(int(match(tokenize.NUMBER)))
    op = match(tokenize.OP)
    direita = Numero(int(match(tokenize.NUMBER)))

    match(tokenize.OP, ')')

    return(Print(BinaryOP(esquerda, op, direita)))

