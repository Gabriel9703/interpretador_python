from compilacao.lexer import lex
from compilacao.ast_nodes import Numero, BinaryOP, Print, Variavel, If, Atribuicao

def parse(codigo_fonte):
    tokens = lex(codigo_fonte)
    pos = 0
    ast = []

    def correspondencia(tipo_esperado, valor_esperado=None):
        nonlocal pos 
        tipo_token, valor_token = tokens[pos]
        if tipo_token == tipo_esperado and (valor_esperado is None or valor_token == valor_esperado):
            pos += 1
            return valor_token
        raise SyntaxError(f"Esperado {tipo_esperado} {valor_esperado} mas veio {tipo_token} {valor_token}")

    def parse_expression():
        nonlocal pos
        node = parse_atom()

        while pos < len(tokens) and tokens[pos][1] in ('+', '>'):
            op = correspondencia('OP')
            direita = parse_atom()
            node = BinaryOP(node, op, direita)
        return node

    def parse_atom():
        nonlocal pos
        tipo_token, valor_token = tokens[pos]
        if tipo_token == 'NUMBER':
            pos += 1
            return Numero(int(valor_token))
        elif tipo_token == 'NAME':
            pos += 1
            return Variavel(valor_token)

        else:
            raise SyntaxError("Expressao invalida")
    
    while pos < len(tokens):
        if tokens[pos][0] == 'NAME':
            if tokens[pos][1] == 'print':
                correspondencia('NAME', 'print')
                correspondencia('OP', '(')
                expr = parse_expression()
                correspondencia('OP', ')')
                ast.append(Print(expr))
            elif tokens[pos][1] == 'if':
                correspondencia('NAME', 'if')
                cond = parse_expression()
                correspondencia('OP', ':')
                if tokens[pos][1] == 'print':
                    correspondencia('NAME', 'print')
                    correspondencia('OP', '(')
                    body_expr = parse_expression()
                    correspondencia('OP', ')')
                    ast.append(If(cond, [Print(body_expr)]))
            else:
                nome = correspondencia('NAME')
                correspondencia('OP', '=')
                expr = parse_expression()
                ast.append(Atribuicao(nome, expr))
        else:
            pos += 1
    return ast

    