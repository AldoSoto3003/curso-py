def no_space(texto):
    cadena = ""
    for char in texto:
        if char != " ":
            cadena += char
    return cadena        

def reverse_string(texto):
    pivote = 0
    cadena = ""
    for i in range(len(texto)):
        pivote -= 1
        cadena += texto[pivote]
    return cadena
    
def es_palindromo(texto):
    """
    Un palindromo es una palabra que es exactamente igual escrita al reves
    """
    texto = no_space(texto=texto)
    texto_reverse = reverse_string(texto=texto)
    return texto_reverse.lower() == texto.lower()

VAR = "Amo la paloma"
print(f"{VAR} es palindromo: {es_palindromo(VAR)}")