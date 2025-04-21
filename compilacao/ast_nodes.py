## Gerar os nós da AST

class Numero:
    def __init__(self, valor):
        self.valor = valor


class BinaryOP:
    def __init__(self, esquerda, op, direita):
        self.esquerda = esquerda   ## Pode ser numero ou outro BinaryOP
        self.op = op               ## '+, '-' , ect
        self.direita = direita

class Print:
    def __init__(self, expressao):
        self.expressao = expressao


"""
Exmplo de uma AST que soma dois valores

Imprimir(
    BinaryOp(
        Numero(10),
        '+',
        Numero(20)
    )
) 
 """       