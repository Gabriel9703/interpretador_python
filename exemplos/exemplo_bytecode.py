import dis

def soma (a , b):
    return a + b


animal = "Elefante"

lista_animais = ["cao", "gato"]

def verificar_animal(animal, lista_animais):
    for a in lista_animais:
        if a == animal:
            print("Aqui")
        else:
            print("Não esta")    

dis.dis(verificar_animal)

print('\n\n')

dis.dis(soma)
