import instrucciones
import matrizRGB

allTokens = instrucciones.re.compile(r"""
        (?P<AvanzarN>Avanzar\ (?P<numA>[1-9]))|
        (?P<Avanzar>Avanzar)|
        (?P<PintarRGB>Pintar\ RGB\((?P<R>\d{1,3}),(?P<G>\d{1,3}),(?P<B>\d{1,3})\))|
        (?P<Pintar>Pintar\ (?P<color>Rojo|Verde|Azul|Negro|Blanco))|
        (?P<Repetir>Repetir\ (?P<nRep>\d+)\ veces\ {)|
        (?P<llave>{)|
        (?P<Izquierda>Izquierda)|
        (?P<Derecha>Derecha)|
        (?P<Cierre>})|
        (?P<Error>[^ \n]+) #Cualquier instruccion que no se encuentre aca es un error
        """,instrucciones.re.X)

def analisisSintaxico():
    flagError = False
    listaErrores = []
    linea = ''
    indiceCiclo = -1 #indice que va indicar en que pos se produce el ciclo "mayor"
    for i in range(instrucciones.informacion.info.lineaActual,len(instrucciones.informacion.texto)):
        instrucciones.informacion.info.lineaActual+=1
        for token in instrucciones.re.finditer(allTokens, instrucciones.informacion.texto[i]):
            print((token.start(), token.end(), token.group(0)))
            if token.group('Error') != None:
                # instrucciones.informacion.errores()
                flagError = True
                linea = f"{i} {instrucciones.informacion.texto[i]}"

            elif token.group('Repetir') != None:
                if not instrucciones.informacion.info.flag:
                    instrucciones.informacion.info.flag = True
                    indiceCiclo = len(listaErrores)
                    linea = f"{i} {instrucciones.informacion.texto[i]}"
                instrucciones.informacion.info.llaves +=1
                
            elif token.group('llave') != None: #si hay una llave sola, la añadira como error pero sumara de igual manera como llave
                linea = f"{i} {instrucciones.informacion.texto[i]}"
                instrucciones.informacion.info.llaves +=1

            elif token.group('Cierre') != None:
                instrucciones.informacion.info.llaves -=1
                if instrucciones.informacion.info.llaves < 0:
                    flagError = True
                    linea = f"{i} {instrucciones.informacion.texto[i]}"
                elif instrucciones.informacion.info.llaves == 0 and instrucciones.informacion.info.flag:
                    listaErrores.pop(indiceCiclo) #elimina el ciclo ya que sus llaves son correctas
                    instrucciones.informacion.info.flag = False

            if linea != '' and linea not in listaErrores:
                listaErrores.append(linea)
                linea = ''

    if flagError or instrucciones.informacion.info.llaves > 0: #si existe un error termina el programa
        instrucciones.informacion.errores(listaErrores)
        quit()
    else:
        instrucciones.informacion.info.lineaActual = 3 ..... #arreglar esto


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

def tokenize():

    for i in range(instrucciones.informacion.info.lineaActual,len(instrucciones.informacion.texto)):
        instrucciones.informacion.info.lineaActual+=1
        for token in instrucciones.re.finditer(allTokens, instrucciones.informacion.texto[i]):
            print((token.start(), token.end(), token.group(0)))
            instrucciones.opciones(token,instrucciones.informacion.info.rep)

    # for i in range(instrucciones.informacion.info.lineaActual,len(instrucciones.informacion.texto)):
    #     instrucciones.informacion.info.lineaActual+=1
    #     for token in instrucciones.re.finditer(allTokens, instrucciones.informacion.texto[i]):
    #         print((token.start(), token.end(), token.group(0)))
    #         instrucciones.opciones(token,instrucciones.informacion.info.rep)

  
comienzo()   
analisisSintaxico()
tokenize()
with open("errores.txt",'w') as textError:
    textError.write('No hay errores')
matrizRGB.MatrizAImagen(matrizRGB.data.getMatriz())

