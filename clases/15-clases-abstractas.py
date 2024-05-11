from abc import ABC, abstractmethod

class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass
            
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")
    
    @classmethod
    def buscar_por_id(self,_id):
        print(f"Buscando por id: {_id} en la tabla {self.tabla}")
        
class Usuario(Model):
    tabla = "Usuario"

instance = Usuario()
Usuario.buscar_por_id(123)
