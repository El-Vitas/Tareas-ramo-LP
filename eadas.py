import re
import matrizRGB
import instrucciones

#clase que funciona como un struct
class info:
    lineaActual = 0
    llaves = 0
    posMatriz = (0,0)

#se obtiene cada linea del texto
with open("archivo.txt", 'r') as f:
    texto = f.read().splitlines()


def comienzo():

    inicio = re.compile(r"""
        Ancho\ (?P<ancho>\d+)|
        Color\ de\ fondo\ (?P<color>Rojo|Verde|Azul|Negro|Blanco)|
        (?P<RGB>Color\ de\ fondo\ RGB\((?P<R>\d{1,3}),(?P<G>\d{1,3}),(?P<B>\d{1,3})\))|
        """,re.X)
    
    for i in range(2):
        token = re.search(inicio,texto[i])
        if token != None:
            print(token.group(0))
            if token.group('ancho') != None:
                ancho = int(token.group('ancho'))
            elif token.group('color') != None:
                color = instrucciones.colores(token.group(token.group('color')))
            elif token.group('RGB') != None:
                color = (int(token.group('R')),int(token.group('G')),int(token.group('B')))
        else:
            print("ERROR")
    matrizRGB.crearMatriz(ancho,color)

def tokenize(code):
    
    for i in range(2,len(texto)):
    #Instrucciones validas
    allTokens = re.compile(r"""
        (?P<AvanzarN>Avanzar\ (?P<numA>[1-9]))|
        (?P<Avanzar>Avanzar)|
        (?P<PintarRGB>Pintar\ RGB\((?P<R>\d{1,3}),(?P<G>\d{1,3}),(?P<B>\d{1,3})\))|
        (?P<Pintar>Pintar\ (?P<color>Rojo|Verde|Azul|Negro|Blanco))|
        (?P<Repetir>Repetir\ (?P<nRep>[0-9])\ veces {)|
        (?P<Izquierda>Izquierda)|
        (?P<Derecha>Derecha)|
        (?P<Cierre>})|
        [^ \n]+
        """,re.X)

    for token in re.finditer(allTokens, code):
        print((token.start(), token.end(), token.group(0)))
        opciones(token)

        
def opciones(token):
        if(token.group('AvanzarN') != None):
            print("nice")
        if(token.group('Avanzar') != None):
            print("nice")
        elif(token.group('PintarRGB') != None):
            R = int(token.group('R'))
            G = int(token.group('G'))
            B = int(token.group('B'))
            instrucciones.avanzar(R,G,B)
        elif(token.group('Pintar') != None):
            print("nice")
        elif(token.group('Repetir') != None):
            print("nice")
        elif(token.group('Izquierda') != None):
            print("nice")
        elif(token.group('Derecha') != None):
            print("nice")
        elif(token.group('Cierre') != None):
            print("nice")
        else:
            print("error")


statements = '''

    Pintar Blanco hola Avanzar 8 Pintar azul Pintar Azul Avanzar Avanzar 1 Avanzarr
    Derecha Izquierda Pintar RGB(0,255,255)A Pintar RGB(4,15,1)
    Pintar RbG(0,1,2) Pintar a RGB(0,12,255) Pintar RGB(256,255,255)
    Pintar RGB(0,12,255)




'''

comienzo()
matrizRGB.MatrizAImagen(matrizRGB.Data)