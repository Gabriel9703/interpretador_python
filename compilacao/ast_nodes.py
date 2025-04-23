
## Gerar os nós da AST (Arvore Sintática Abstrata)
class Numero:
    """ Classe que representa somente os 
    numeros """
    def __init__(self, valor):
        self.valor = valor


class BinaryOP:
    """ Classe que representa a operacao binária
    """
    def __init__(self, esquerda, op, direita):
        self.esquerda = esquerda   ## Pode ser numero ou outro BinaryOP
        self.op = op               ## '+, '-' , ect
        self.direita = direita

class Print:
    """ Classe que representa a impressão da 
    operação relizada"""
    def __init__(self, expressao):
        self.expressao = expressao


"""
Geraria uma arvore tipo:

Print
    BinaryOP
        Numero(3)
           '+'
        Numero(4)   

"""