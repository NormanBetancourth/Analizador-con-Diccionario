from parts.tabla import Tabla_de_simbolos


class CondiIterable:
    def __init__(self, type, tabla):
        self.type = type
        self.tabla_de_simbolos = Tabla_de_simbolos()
        self.tabla_de_simbolos.diccionario.update(tabla)


    def __repr__(self):
        return f"{self.type} [ {self.tabla_de_simbolos.diccionario} ]"

    def updateDict(self, diccionario):
        self.tabla_de_simbolos.extenderDiccionario(diccionario)


