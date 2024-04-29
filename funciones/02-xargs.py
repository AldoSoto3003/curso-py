""" Uso de los multiples argumentos XARGS """

def suma(*args):
    
    suma = 0
    for numero in args:
        suma += numero    
    print(suma)
    
suma(5,5)
suma(5,5,45)
suma(5,5,45,87)
