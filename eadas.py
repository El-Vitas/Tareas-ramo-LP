import instrucciones
import matrizRGB
def comienzo():
    inicio = instrucciones.re.compile(r"""
        Ancho\ (?P<ancho>\d+)| #Ancho de la matriz
        Color\ de\ fondo\ (?P<color>Rojo|Verde|Azul|Negro|Blanco)| #color de fondo de la matriz
        (?P<RGB>Color\ de\ fondo\ RGB\((?P<R>\d{1,3}),(?P<G>\d{1,3}),(?P<B>\d{1,3})\)) #fondo rgb
        """,instrucciones.re.X)
    
    for i in range(2):
        token = instrucciones.re.search(inicio,instrucciones.informacion.texto[i])
        if token != None:
            if token.group('ancho') != None:
                ancho = int(token.group('ancho'))
            elif token.group('color') != None:
                color = instrucciones.colores(token.group('color'))
            elif token.group('RGB') != None:
                color = (int(token.group('R')),int(token.group('G')),int(token.group('B')))
        else:
            instrucciones.informacion.errores(i)
        instrucciones.informacion.info.lineaActual +=1
    matrizRGB.data.crearMatriz(ancho,color)

    if(instrucciones.re.search(r'\S',instrucciones.informacion.texto[2])):
        instrucciones.informacion.errores()
    else:
        instrucciones.informacion.info.lineaActual+=1

def tokenize():
    #Instrucciones validas
    allTokens = instrucciones.re.compile(r"""
        (?P<AvanzarN>Avanzar\ (?P<numA>[1-9]))|
        (?P<Avanzar>Avanzar)|
        (?P<PintarRGB>Pintar\ RGB\((?P<R>\d{1,3}),(?P<G>\d{1,3}),(?P<B>\d{1,3})\))|
        (?P<Pintar>Pintar\ (?P<color>Rojo|Verde|Azul|Negro|Blanco))|
        (?P<Repetir>Repetir\ (?P<nRep>\d*)\ veces\ {)|
        (?P<Izquierda>Izquierda)|
        (?P<Derecha>Derecha)|
        (?P<Cierre>})|
        [^ \n]+
        """,instrucciones.re.X)

    for i in range(instrucciones.informacion.info.lineaActual-1,len(instrucciones.informacion.texto)):
        for token in instrucciones.re.finditer(allTokens, instrucciones.informacion.texto[i]):
            print((token.start(), token.end(), token.group(0)))
            instrucciones.opciones(token,instrucciones.informacion.info.rep)

# def opciones(token,ciclo):
#     if(informacion.info.flag): #flag que indica que todo lo que viene se encuentra dentro de una rep
#         if(token.group('Repetir') != None):
#             informacion.info.llaves+=1
#         elif(token.group('Cierre') != None):
#             instrucciones.cierreRep()
#         informacion.info.rep.append(token)
#     else:
#         if(token.group('AvanzarN') != None):
#             instrucciones.avanzar(int(token.group('numA')))
#         elif(token.group('Avanzar') != None):
#             instrucciones.avanzar(1)
#         elif(token.group('PintarRGB') != None):
#             R = int(token.group('R'))
#             G = int(token.group('G'))
#             B = int(token.group('B'))
#             instrucciones.pintarRGB(R,G,B)
#         elif(token.group('Pintar') != None):
#             instrucciones.pintar(token.group('color'))
#         elif(token.group('Repetir') != None):
#             informacion.info.llaves+=1
#             informacion.info.rep.append(token)
#             informacion.info.flag = True
#         elif(token.group('Izquierda') != None):
#             instrucciones.izquierda()
#         elif(token.group('Derecha') != None):
#             instrucciones.derecha()
#         elif(token.group('Cierre') != None):
#             instrucciones.cierreRep()
#         else:
#             print("error")


comienzo()
tokenize()
matrizRGB.MatrizAImagen(matrizRGB.data.getMatriz())

