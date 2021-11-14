from Variable import Variable


class Tabla_de_simbolos:
    def __init__(self):
        self.diccionario = {}

    def add(self, key, value, type):
        a = Variable(key, value, type)
        self.diccionario[key]= a


    def __str__(self):
        return f"{print(self.diccionario)}"

