# 🧠 Simulação da Pipeline do CPython

Este projeto tem como objetivo aprofundar os estudos sobre o que acontece em **baixo nível** quando um script Python é executado.

A simulação cobre desde o processo de **tokenização** até a **geração de bytecode**, oferecendo uma visão didática da pipeline de execução. Questões mais avançadas, como o funcionamento interno da **stack machine** do Python ou a conversão final para código de máquina, **não são abordadas** neste momento.

> 📌 Código-fonte analisado: `print(3 + 4)`

---

## 🛠️ Ferramentas Utilizadas

- Python 3.12
- Interpretador **CPython**
- Bibliotecas da standard library que expõem a camada de baixo nível:
  - `tokenize`: usada para entender como o Python separa os tokens
  - `dis`: usada para visualizar os bytecodes gerados após a AST

---

## 🗂️ Estrutura do Projeto

### 📁 `/compilacao`

- `lexer.py`: utiliza o módulo `tokenize` para gerar strings de tokens
- `parser.py` + `ast_node.py`: responsáveis pela construção da AST (*Abstract Syntax Tree*).
  - `ast_node.py` define os nós da árvore
  - `parser.py` monta a árvore a partir dos tokens
- `bytecode.py`: contém as instruções compreendidas pela VM simulada
- `compiler.py`: faz a compilação da AST em bytecode

### 📁 `/maquina_virtual`

- `vm.py`: simula uma **máquina virtual Python** que interpreta os bytecodes e executa as operações

### 📁 `/exemplos`

- Scripts de exemplo que mostram como visualizar bytecodes e tokens gerados pelo CPython

---

## 🧩 Conceitos Importantes

- A **recursão** é essencial para a construção da AST. O CPython percorre os tokens recursivamente para gerar os nós da árvore sintática.
- A **PVM** (Python Virtual Machine) funciona como um grande loop `switch/case` que interpreta opcodes, empilha e desempilha valores na stack.

---

## 📝 Observações

Este projeto busca entender melhor como o **CPython** realiza seu trabalho por trás dos panos. Existem outros interpretadores como o **PyPy** (que utiliza JIT), **Jython**, entre outros — que não foram abordados aqui.

Futuramente, pretendo estudar esses outros interpretadores para realizar comparações mais técnicas com o CPython.
