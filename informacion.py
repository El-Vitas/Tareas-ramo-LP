#clase que funciona como un struct
class info:
    lineaActual = 1
    llaves = 0
    posX = 0
    posY = 0
    direccion = 'r'
    rep = []
    nRep = []
    flag = False

#se obtiene cada linea del texto
with open("archivo.txt", 'r') as f:
    texto = f.read().splitlines()

def errores():
    with open("errores.txt",'w') as error:
        error.write(f"{info.lineaActual} {texto[info.lineaActual-1]}")
    quit()




