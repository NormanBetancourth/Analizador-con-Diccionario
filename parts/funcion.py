from parts.tabla import Tabla_de_simbolos


class Funcion:
    def __init__(self, type, key, tabla):
        self.key = key
        self.type = type
        self.tabla_de_simbolos = Tabla_de_simbolos()
        self.tabla_de_simbolos.diccionario.update(tabla)

    def __repr__(self):
        return f"{self.type}  {self.key} [ {self.tabla_de_simbolos.diccionario} ]"
