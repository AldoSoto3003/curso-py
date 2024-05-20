
def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por 0")
    return 5/n

try:
    print(division())
except ZeroDivisionError as e:
    print(e)