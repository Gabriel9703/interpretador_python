## Conjunto de instruções que minha VM vai entender
class Instrucao:
    def __init__(self, opcode, agr=None):
        self.opcode = opcode
        self.arg = agr

    def __repr__(self):
        return f"{self.opcode} {self.arg if self.arg is not None else ''}".strip()


LOAD_CONST = "LOAD_CONST"
ADD = "ADD"
PRINT = "PRINT"
HALT = "HALT"      