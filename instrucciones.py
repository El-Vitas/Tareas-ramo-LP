from informacion import info
from matrizRGB  import data
import informacion
import re

def avanzar(num):
    if info.direccion == 'u':
        info.posX -= num
    elif info.direccion == 'd':
        info.posX += num
    elif info.direccion == 'l':
        info.posY -= num
    elif info.direccion == 'r':
        info.posY += num

def colores(color):
    if color == 'Rojo':
        return (255,0,0)
    elif color == 'Verde':
        return (0,255,0)
    elif color == 'Azul':
        return (0,0,255)
    elif color == 'Negro':
        return (0,0,0)
    else: 
        return (255,255,255) #blanco

def pintarRGB(R,G,B): 
    if(0<=R<=255 and 0<=G<=255 and 0<=B<=255):
        RGB = (R,G,B)
        data.editarMatriz(RGB,info.posX,info.posY)
    else:
        print("Error")

def pintar(color):
    RGB = colores(color)
    data.editarMatriz(RGB,info.posX,info.posY)

def izquierda(): #u = up, d = down, l = left, r = right
    if info.direccion == 'u':
        info.direccion = 'l'
    elif info.direccion == 'd':
        info.direccion = 'r'
    elif info.direccion == 'l':
        info.direccion = 'd'
    elif info.direccion == 'r':
        info.direccion = 'u'

def derecha(): #u = up, d = down, l = left, r = right
    if info.direccion == 'u':
        info.direccion ='r'
    elif info.direccion =='d':
        info.direccion = 'l'
    elif info.direccion == 'l':
        info.direccion = 'u'
    elif info.direccion == 'r':
        info.direccion = 'd'


# def repetir(listaToken):
#     cont = 1 #empieza en 1 para saltarse la instruccion de saltar que esta en el [0]
#     llaves = 0
#     nuevoCiclo = False
#     ciclo = []
#     veces = int(listaToken[0].group('nRep'))
#     for i in range(veces):
#         while cont <= len(listaToken):
#             token = listaToken[cont]
#             if token.group('nRep') != None:
#                 nuevoCiclo = True
#                 llaves+=1
#             elif token.group('Cierre') != None:
#                 llaves-=1

#             if nuevoCiclo:
#                 if llaves == 0:
#                     repetir(ciclo)
#                     nuevoCiclo = False
#                     ciclo.clear()
#                 elif llaves < 0:
#                     print("Error")
#                 else:
#                     ciclo.append(token)
#             else: 
#                 opciones(token)
#             cont+=1



# def cierreRep():
#     info.llaves-=1
#     if info.llaves < 0:
#         print("error")
#     elif info.llaves == 0:
#         info.flag = False
#         repetir(info.rep)
#         info.rep.clear()


def repetir(listaToken):
    # cont = 1 #empieza en 1 para saltarse la instruccion de saltar que esta en el [0]
    ciclo = []
    veces = int(listaToken[0].group('nRep'))
    largoLista = len(listaToken)

    for i in range(veces):
        for j in range(1,largoLista):
            token = listaToken[j]
            opciones(token,ciclo)

            # if token.group('nRep') != None:
            #     nuevoCiclo = True
            #     llaves+=1
            # elif token.group('Cierre') != None:
            #     llaves-=1

            # if nuevoCiclo:
            #     if llaves == 0:
            #         repetir(ciclo)
            #         nuevoCiclo = False
            #         ciclo.clear()
            #     elif llaves < 0:
            #         print("Error")
            #     else:
            #         ciclo.append(token)
            # else: 
            #     opciones(token)
            # cont+=1


def cierreRep(ciclo):
    info.llaves-=1
    if info.llaves < 0:
        print("error")
    elif info.llaves == 0:
        info.flag = False
        ciclo.pop(-1) #elimina el ultimo cierre de llaves
        repetir(ciclo)
        ciclo.clear()


def errores(info,texto):
    with open("errores.txt",'w') as error:
        error.write(f"{info.lineaActual} {texto}")
    quit()

def opciones(token,ciclo):
    if(informacion.info.flag): #flag que indica que todo lo que viene se encuentra dentro de una rep
        ciclo.append(token)
        if(token.group('Repetir') != None):
            informacion.info.llaves+=1
        elif(token.group('Cierre') != None):
            cierreRep(ciclo)
    else:
        if(token.group('AvanzarN') != None):
            avanzar(int(token.group('numA')))
        elif(token.group('Avanzar') != None):
            avanzar(1)
        elif(token.group('PintarRGB') != None):
            R = int(token.group('R'))
            G = int(token.group('G'))
            B = int(token.group('B'))
            pintarRGB(R,G,B)
        elif(token.group('Pintar') != None):
            pintar(token.group('color'))
        elif(token.group('Repetir') != None):
            informacion.info.llaves+=1
            ciclo.append(token)
            informacion.info.flag = True
        elif(token.group('Izquierda') != None):
            izquierda()
        elif(token.group('Derecha') != None):
            derecha()
        elif(token.group('Cierre') != None):
            cierreRep(ciclo)
        else:
            print("error")


