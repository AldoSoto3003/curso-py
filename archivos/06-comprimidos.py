from pathlib import Path
from zipfile import ZipFile

with ZipFile("archivos/comprimidos.zip","w") as zip:
    for path in Path().rglob("*.py"):
        
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)
            # pass

with ZipFile("archivos/comprimidos.zip","r") as zip:
    # print(zip.namelist())
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )
    
    zip.extractall("archivos/descomprimidos")