from compilacao.bytecode import Instrucao, LOAD_CONST, ADD, PRINT, HALT
from compilacao.ast_nodes import Numero, BinaryOP, Print


def compilar_ast(node):
    bytecode = []

    if isinstance(node, Print):
        bytecode += compilar_ast(node.expressao)
        bytecode.append(Instrucao(PRINT))

    elif isinstance(node, BinaryOP):
        bytecode += compilar_ast(node.esquerda)    
        bytecode += compilar_ast(node.direita)    

        if node.op == '+':
            bytecode.append(Instrucao(ADD))

        else:
            raise NotImplementedError(f"Operador {node.op} nao suportado ainda")


    elif isinstance(node, Numero):
        bytecode.append(Instrucao(LOAD_CONST, node.valor))

    return bytecode    