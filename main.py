from compilacao.bytecode import Instrucao, LOAD_CONST, ADD, PRINT, HALT
from maquina_virtual.vm import MaquinaVirtual
from compilacao.parser import parse
from compilacao.codegen import compilar_ast

bytecode = [
    Instrucao(LOAD_CONST, 10),
    Instrucao(LOAD_CONST, 30),
    Instrucao(ADD),
    Instrucao(PRINT),
    Instrucao(HALT)
]


maquina_virtual = MaquinaVirtual(bytecode)
maquina_virtual.executar()

codigo_fonte = "Print(10 + 20)"
ast = parse(codigo_fonte)
bytecode = compilar_ast(ast)
bytecode.append(Instrucao(HALT))


print('Bytecode gerado: \n')
for i, instrucao in enumerate(bytecode):
    print(f"{i}: {instrucao}")



print("Executando na VM:\n")

vm = MaquinaVirtual(bytecode)
vm.executar()