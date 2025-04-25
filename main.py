from compilacao.bytecode import Instrucao, HALT
from maquina_virtual.vm import MaquinaVirtual
from compilacao.parser import parse
from compilacao.compiler import compilar_ast_em_bytecode


codigo_fonte = "Print(3 + 4)"
ast = parse(codigo_fonte)
bytecode = compilar_ast_em_bytecode(ast)
bytecode.append(Instrucao(HALT))


print('Bytecode gerado: \n')
for i, instrucao in enumerate(bytecode):
    print(f"{i}: {instrucao}")


print("Executando na VM:\n")
vm = MaquinaVirtual(bytecode)
vm.executar()