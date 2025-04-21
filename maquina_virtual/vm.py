
from compilacao.bytecode import *

### MAQUINA VIRTUAL QUE EXECUTA BYTECODE
class MaquinaVirtual:
    def __init__(self, bytecode):
        self.byetcode = bytecode 
        self.stack = []
        self.pc = 0 # programa contador

    def executar(self):
        while self.pc < len(self.byetcode):
            instrucao = self.byetcode[self.pc]
            self.pc += 1    


            if instrucao.opcode == LOAD_CONST:
                self.stack.append(instrucao.arg)

            elif instrucao.opcode == ADD:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append( a + b)   

            elif instrucao.opcode == PRINT:
                print(self.stack.pop())

            elif instrucao.opcode == HALT:
                break

            else:
                raise Exception( f" Nao conheco o opcode {instrucao.opcode}")        


