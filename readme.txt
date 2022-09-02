Nombre: Jonathan Nicolás Olivares Salinas
Rol: 202073096-2

Informacion: 
    El programa cuenta de 4 archivos .py:
        instrucciones.py: Funciones ligadas a las instrucciones del programa.
        informacion.py: Informacion extra necesaria para el programa.
        matrizRGB.py: Matriz del programa, funciones relacionadas a matrices y a convertir matrices a imagen
        pixelart.py: Modulo principal del programa, el cual se tiene que ejecutar para el funcionamiento de este.

    Cuenta con 2 archivos de texto:
        archivo.txt: Archivo donde se encontrarán todas las instrucciones del programa.
        errores.txt: Archivo donde se mostrarán los errores de sintaxis del programa. (este archivo se crea automaticamente despues de la ejecucion del programa.)
        
    Cuenta con un archivo .png:
        pixelart.png: Imagen creada en caso de que la sintaxis del programa sea correcta (este archivo se crea automaticamente despues de la ejecucion del programa.).
        

Respecto a los errores de sintaxis y de ejecución:
    1) El programa considerará error de sintaxis cada conjunto de caracteres o simbolos que no pertenezca las instrucciones validas entregadas en el respectivo pdf de la tarea.  
    2) El programa considerará como error un repetir que abre pero no cierra. El error se marcará en la linea que empezó el repetir.
    Si se encuentran más repetir dentro, el error lo seguirá marcando en el primer repetir que se encuentra fuera de los otros repetir.
    3) El programa leera todo el texto buscando un error de sintaxis, en caso de que exista algun error, el programa al terminar el analisis de la sintaxis
    escribirá en el texto error.txt todos los errores y terminará el programa.
    4) Errores como: Salirse de una posicion permitida dentro de la matriz , o rango de numeros RGB incorrectos. Se considerarán errores de ejecución y el programa
    imprimira los errores por consola y luego finalizará.

Sobre instrucción repetir:
	La instrucción repetir funciona recursivamente entre 3 funciones. opciones, cierreRep, repetir.
	
Ejecución del programa:
	Para ejecutar el programa se deben tener todos los archivos tanto .py como .txt dentro de la misma carpeta, de no ser así se necesitaría modificar el codigo.
	Luego con los archivos dentro de la misma carpeta se necesita ejecutar pixelart.py
	
	Al realizar todo lo anterior si las instrucciones entregadas son correctas, aparecerá un archivo llamado pixelart.png el cuál corresponde a la imagen creada 
	mediante las instrucciones. De no ser así se le marcará un error por consola, o en el archivo errores.txt (este archivo se crea automaticamente despues de la ejecucion del programa.).
    