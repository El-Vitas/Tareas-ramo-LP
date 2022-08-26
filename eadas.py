import re
import matrizRGB
import instrucciones
linea = 0
llaves = 0

def tokenize(code):

    # palab = [
    #     r'Avanzar (?P<numA>[1-9])', 
    #     r'Avanzar',
    #     r'Pintar RGB\((?P<R>\d{1,3}),(?P<G>\d{1,3}),(?P<B>\d{1,3})\)',
    #     r'Pintar (?P<color>Rojo|Verde|Azul|Negro|Blanco)',
    #     r' Repetir (?P<nRep>[0-9]) veces {',
    #     r'[^ \n]+'
    # ]

    # palab = [ #Palabras en lista para apreciar cada busqueda
    #     r'Avanzar (?P<numA>[1-9])', 
    #     r'Avanzar',
    #     r'Pintar RGB\((?P<R>\d{1,3}),(?P<G>\d{1,3}),(?P<B>\d{1,3})\)',
    #     r'Pintar (?P<color>Rojo|Verde|Azul|Negro|Blanco)',
    #     r' Repetir (?P<nRep>[0-9]) veces {',
    #     r'[^ \n]+'
    # ]

    #Compilador que tiene como match las instrucciones que contienen un espacio
    # o cualquier palabra separada por un espacio
    # palabras = re.compile(r"""
    #     Avanzar\ (?P<numA>[1-9])|
    #     Pintar\ RGB\((?P<R>\d{1,3}),(?P<G>\d{1,3}),(?P<B>\d{1,3})\)|
    #     Pintar\ (?P<color>Rojo|Verde|Azul|Negro|Blanco)|
    #     Repetir\ (?P<nRep>[0-9])\ veces {|
    #     [^ \n]+
    #     """,re.X)

    # palabras = re.compile(r"""
    #     (?P<AvanzarN>Avanzar\ (?P<numA>[1-9]))|
    #     (?P<PintarRGB>Pintar\ RGB\((?P<R>\d{1,3}),(?P<G>\d{1,3}),(?P<B>\d{1,3})\))|
    #     Pintar\ (?P<color>Rojo|Verde|Azul|Negro|Blanco)|
    #     Repetir\ (?P<nRep>[0-9])\ veces {|
    #     [^ \n]+
    #     """,re.X)

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

tokenize(statements)
matrizRGB.MatrizAImagen(matrizRGB.Data)