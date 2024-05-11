class Animal:
    def comer(self):
        print("comiendo")
        
    def pasear(self):
        print("paseando al animal")
    
class Perro:
    def pasear(self):
        print("paseando al perro")
            
class Chanchito(Animal,Perro):
    def programar(self):
        print("programando")
        
perro = Perro()
perro.pasear()