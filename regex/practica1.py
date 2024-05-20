" Practica de REGEX "

import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
texto_a_buscar = "Python"
resultado = re.search(texto_a_buscar,cadena)
resultados = re.findall(texto_a_buscar,cadena)

if resultado is not None:
    print(resultado.start()) #Indice donde inicia el substring buscado
    print(resultado.end())   #Indice donde terminar el substring buscado 
    print(resultado.span())  #Tupla con el inicio y fin del substring buscado
    print(len(resultados))
else:
    print("no he encontrado el texto")
    