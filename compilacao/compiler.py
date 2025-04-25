from compilacao.bytecode import *
from compilacao.ast_nodes import Numero, BinaryOP, Print



def compilar_ast_em_bytecode(node):
    bytecode = []

    if isinstance(node, Print):
        bytecode += compilar_ast_em_bytecode(node.expressao)
        bytecode.append(Instrucao(PRINT))

    elif isinstance(node, BinaryOP):
        bytecode += compilar_ast_em_bytecode(node.esquerda)    
        bytecode += compilar_ast_em_bytecode(node.direita)    

        if node.op == '+':
            bytecode.append(Instrucao(ADD))

        else:
            raise NotImplementedError(f"Operador {node.op} nao suportado ainda")


    elif isinstance(node, Numero):
        bytecode.append(Instrucao(LOAD_CONST, node.valor))

    return bytecode    