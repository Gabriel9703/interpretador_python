
class Numero:
    def __init__(self, valor):
        self.valor = valor


class BinaryOP:
    def __init__(self, esquerda, op, direita):
        self.esquerda = esquerda   ## Pode ser numero ou outro BinaryOP
        self.op = op               ## '+, '-' , etc
        self.direita = direita

class Print:
    def __init__(self, expressao):
        self.expressao = expressao


"""
Gerar os nós da AST (Arvore Sintática Abstrata):

Print
    BinaryOP
        Numero(3)
           '+'
        Numero(4)   
"""