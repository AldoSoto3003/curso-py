import re

lista_nombres = ['Ana Gomez',
                 'Maria Martin',
                 'Sandra Lopez',
                 'Santiago MArtín']

for nombre in lista_nombres:
    if re.findall('^Sandra',nombre):
        print(nombre)