
class Usuario():
    def guardar(self):
        print("guardando en BBDD")

class Sesion():
    def guardar(self):
        print("guardando en BBDD")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
sesion  = Sesion()

guardar([sesion,usuario])