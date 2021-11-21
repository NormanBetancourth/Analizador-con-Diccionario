class Variable:
    def __init__(self, key,value, type):
        self.value = value
        self.key = key
        self.type = type

    def __repr__(self):
        return f"{self.type}  {self.key} = {self.value}"