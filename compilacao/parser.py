from compilacao.lexer import lex
from compilacao.ast_nodes import Numero, BinaryOP, Print

def parse(codigo_fonte):
    tokens = lex(codigo_fonte)
    pos = 0

    def correspondencia(tipo_esperado, valor_esperado=None):
        nonlocal pos 
        tipo_token, valor_token = tokens[pos]
        if tipo_token == tipo_esperado and (valor_esperado is None or valor_token == valor_esperado):
            pos += 1
            return valor_token
        raise SyntaxError(f"Esperado {tipo_esperado} {valor_esperado} mas veio {tipo_token} {valor_token}")

    nome = correspondencia("NAME")
    if nome != 'Print':
        raise SyntaxError("Era esperado print")

    correspondencia('OP', '(')    
    esquerda = Numero(int(correspondencia("NUMBER")))
    op = correspondencia("OP")
    direita = Numero(int(correspondencia("NUMBER")))
    correspondencia('OP', ')')

    return Print(BinaryOP(esquerda, op, direita))
"""
Essa funcao parse simples retorna a seguinte arvore:

 Imprimir(
    BinaryOp(
        Numero(10),
        '+',
        Numero(20)
    )
) 

 """   