class Perro:

    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def habla(self):
        print(f"{self.__nombre} Guau!")
    
    @classmethod
    def factory(cls):
        return cls("chanchito feliz",4)
      
perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())