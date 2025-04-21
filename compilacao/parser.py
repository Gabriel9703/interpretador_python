import re
from compilacao.ast_nodes import Numero, BinaryOP, Print

def parse(codigo_fonte):
    ## Parse print(10 +20)
    m = re.match(r"imprimir\((\d+)\s*([\+\-])\s*(\d+)\)", codigo_fonte)
    if not m:
        raise SyntaxError("Apenas consigo fazer print com soma, por enquanto")

    esquerda = Numero(int(m.group(1)))
    op = m.group(2)
    direita = Numero(int(m.group(3)))

    return Print(BinaryOP(esquerda, op, direita))    