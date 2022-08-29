import numpy as np # pip install numpy
from PIL import Image # pip install Pllow

#MTRIZ
class MatrizRGB:
    def __init__(self):
        self.__data = []
        self.__ancho = 0

    def crearMatriz(self,num,RGB):
        self.ancho = num
        for i in range(num):
            self.__data.append([(RGB)]*num)

    def editarMatriz(self,RGB,posX,posY):
        self.__data[posX][posY] = RGB

    def getMatriz(self):
        return self.__data

    def getAncho(self):
        return self.__ancho

data = MatrizRGB()

def MatrizAImagen(matriz, filename='pixelart.png', factor=10):
    '''
    Convierte una matriz de valores RGB en una imagen y la guarda como un archivo png.
    Las imagenes son escaladas por un factor ya que con los ejemplos se producirian imagenes muy pequeñas.
        Parametros:
                matriz (lista de lista de tuplas de enteros): Matriz que representa la imagen en rgb.
                filename (str): Nombre del archivo en que se guardara la imagen.
                factor (int): Factor por el cual se escala el tamaño de las imagenes.
    '''
    matriz = np.array(matriz, dtype=np.uint8)
    np.swapaxes(matriz, 0, -1)

    N = np.shape(matriz)[0]

    img = Image.fromarray(matriz, 'RGB')
    img = img.resize((N*10, N*10), Image.Resampling.BOX)
    img.save(filename)