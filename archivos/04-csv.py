import csv

# Escribir en un CSV
with open("../archivos/archivo.csv","w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["twit_id","user_id","text"])
    writer.writerow([1100,1,"Este es un twit"])
    writer.writerow([5345,2,"text","Este es otro twit"])
    
# Leer en un CSV
with open("../archivos/archivo.csv","r") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in reader:
        print(linea)
        
# Actualizar CSV
with open("../archivos/archivo.csv","+r") as r, open("../archivos/archivo_temp.csv","+w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000,1,"texto modificado"])
        else:
            writer.writerow(linea)
    