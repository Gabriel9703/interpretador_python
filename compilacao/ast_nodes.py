# Etapa 1
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
Exmplo de uma AST que soma dois valores

Imprimir(
    BinaryOp(
        Numero(10),
        '+',
        Numero(20)
    )
) 
 """       

class Variavel:
    def __init__(self, nome):
        self.nome = nome


class Atribuicao:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class If:
    def __init__(self, condition, then_body, else_body=None):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body
        