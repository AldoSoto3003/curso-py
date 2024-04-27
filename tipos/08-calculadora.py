"""Calculadora"""

n1 = float(input("Ingresa primer numero: "))
n2 = float(input("Ingresa segundo numero: "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

MENSAJE = f"""
para los numeros {n1} y {n2},
el resulado de la suma es {suma},
el resulado de la resta es {resta},
el resulado de la multi es {multi},
el resulado de la div es {div},
"""
print(MENSAJE)
