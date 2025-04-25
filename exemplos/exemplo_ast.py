import ast


arvore = ast.dump(ast.parse("print(3 + 4)"), indent=4)

print(arvore)