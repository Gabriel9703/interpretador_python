
## Conjunto de instruções que minha VM vai entender
class Instrucao:
    def __init__(self, opcode, agr=None):
        self.opcode = opcode
        self.arg = agr

    def __repr__(self):
        return f"{self.opcode} {self.arg if self.arg is not None else ''}".strip()


## Nossas instruções, que a VM vai entender
LOAD_CONST = "LOAD_CONST"
LOAD_NAME = "LOAD_NAME"
STORE_NAME = "STORE_NAME"
ADD = "ADD"
GT = "GT"  
PRINT = "PRINT"
JUMP_IF_FALSE = "JUMP_IF_FALSE"
JUMP = "JUMP"
HALT = "HALT"      