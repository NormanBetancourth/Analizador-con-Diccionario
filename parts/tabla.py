from parts.Variable import Variable


class Tabla_de_simbolos:
    def __init__(self):
        self.diccionario = {}

    def add(self, key, value, type):
        a = Variable(key, value, type)
        self.diccionario[key]= a

    def extenderDiccionario(self, diccionario):
        self.diccionario.update(diccionario)

    def __str__(self):
        return f"{print(self.diccionario)}"

    def agregar(self, i):
        a = Variable(i.key, i.value, i.type)
        self.diccionario[i.key] = a

    def agregarFuncion(self, funcion):
        self.diccionario[funcion.key] = funcion


