import os
import shutil
import base64
#----------------------------------------------------------------Menu de opciones para la gestion de ficheros ---------------------------------------------------------------------
def Menu():
    Eleccion=True
    while Eleccion==True:
        print('Gestion de Ficheros con Python')
        print('Desarrollado por: Vikolow')
        print('\n')
        print('Menu de opciones:')
        print('\n')
        print('1-Crear un fichero')
        print('2-Escribir dentro de un fichero')
        print('3-Leer el contenido de un archivo')
        print('4-Copiar un fichero')
        print('5-Encriptar un fichero')
        print('6-Desencriptar un fichero')
        print('7-Salir')
        print('\n')
        opcion= input('Elige una opcion: ')
        os.system('cls')
        if opcion.isdigit():
            opcion= int(opcion)
        if opcion==1:
            Mensaje=Crear()
        if opcion==2:
            Mensaje=Escribir()
        if opcion==3:
            Mensaje=Leer()
        if opcion==4:
            Mensaje=Copiar()
        if opcion==5:
            Mensaje=Encriptar()
        if opcion==6:
            Mensaje=Desencriptar()
        if opcion==7:
            print('¡Hasta Pronto!')
            break
        if opcion > 7 or opcion < 0:
            print('El numero no esta en el rango indicado')
            input('Pulsa cualquier tecla para continuar') 
        #Como hago para enviarlo fuera del if isdigit() , si pongo opcion = "string" no funciona bien.
        else:
        #Bucle de castigo para listos
            os.system('cls')
            disculpa=''
            while disculpa=='':
                disculpa=input('Manin esta bastante claro ,introduce un numero valido ,entre 1 y 7.Disculpate con el programa si quieres volver al menu (Escribe "Perdón"):')
                if disculpa == 'Perdón':
                    disculpa='aceptada'
                else:
                    disculpa=''
                    os.system('cls')
                
    
#Funcion para crear un archivo
def Crear():
    try:
        ruta=input('Indica la ruta donde quieres crear el fichero: ')
        nombre=input('Indica el nombre del fichero: ')
        ruta_nombre=ruta + nombre
        archivo= open(ruta_nombre,"w")
        archivo.close()
        print('El archivo se creo correctamente en',ruta)
    except Exception as error:
        if FileExistsError:
            print('El fichero ya existe:',ruta_nombre)
        if FileNotFoundError:
            print('La ruta no existe:',ruta)
        print('Ha ocurrio un error, error: ',error)
    input('Pulsa cualquier tecla para continuar: ')
    

#Funcion para escribir en un archivo
def Escribir():
    try:
        ruta=input('Indica la ruta donde crear el fichero con su nombre: ')
        texto = input('Introduce el texto a escribir: ') 
        with open(ruta,"a") as archivo: 
            archivo.write('\n'+texto) 
        print('El texto se ha escrito correctamente en ',ruta)
        print('\n')
    except Exception as error:
        if FileNotFoundError:
            print('La ruta no existe:',ruta)
        print('Ha ocurrido un error: ', error)
    input('Pulsa cualquier tecla para continuar: ')
        

#Funcion para leer un archivo
def Leer():
    try:
        ruta=input('Indica la ruta donde se encuentra el fichero: ')
        nombre=input('Indica el nombre del fichero: ')
        with open(os.path.join(ruta, nombre), "r") as archivo:
            contenido = archivo.read()
        print('El contenido del fichero es: ')
        print('\n')
        print(contenido)
        print('\n') 
    except Exception as error:
        if FileNotFoundError:
            print('La ruta no existe:',ruta)
        print('Ha ocurrido un error: ', error)
    input('Pulsa cualquier tecla para continuar: ')


#Funcion para copiar un archivo 
def Copiar():
    try:
        ruta_origen = input('Indica la ruta del fichero origen: ')
        ruta_destino = input('Indica la ruta del fichero destino: ')
        if not os.path.exists(ruta_origen):
            print('La ruta de origen no existe:',ruta_origen) 
        elif not os.path.exists(ruta_destino):
            print('La ruta de destino no existe:',ruta_destino)
        shutil.copy(ruta_origen, ruta_destino)
        print('El archivo se ha copiado correctamente.')
    except Exception as error:
        print('Ha ocurrido un error:', error)
    input('Pulsa una tecla para continuar:')
    
#---------------------------------------------------------------- Encriptar y desencriptar archivos con base64. Mejorar ambas con pycrypto en el proximo commit----------------------------------------------------------------    

#Funcion para encriptar un archivo 
def Encriptar():
    try:
        ruta_origen=input('Indica la ruta donde se encuentra el fichero: ')
        nombre_origen=input('Indica el nombre del fichero: ')
        with open(os.path.join(ruta_origen, nombre_origen), "rb") as archivo_origen:
            contenido = archivo_origen.read()
            contenido_base64 = base64.b64encode(contenido)
            ruta_destino = input('Indica la ruta donde quieres guardar el archivo encriptado: ')
            nombre_destino = input('Indica el nombre del archivo encriptado: ')
        with open(os.path.join(ruta_destino, nombre_destino), "wb") as archivo_destino:
            archivo_destino.write(contenido_base64)
        print('El archivo se ha encriptado correctamente.')
    except Exception as error:
        if FileNotFoundError:
            print('Alguna de las rutas no existe:',ruta_origen ,ruta_destino)
        print('Ha ocurrido un error: ', error)
    input('Pulsa cualquier tecla para continuar: ')
    
#Funcion para desencriptar un archivo 
def Desencriptar():
    try:
        ruta_origen = input('Indica la ruta donde se encuentra el fichero encriptado: ')
        nombre_origen = input('Indica el nombre del fichero encriptado: ')
        with open(os.path.join(ruta_origen, nombre_origen), "rb") as archivo_encriptado:
            contenido_base64 = archivo_encriptado.read()
            contenido_bytes = base64.b64decode(contenido_base64)
            ruta_destino = input('Indica la ruta donde quieres guardar el archivo desencriptado: ')
            nombre_destino = input('Indica el nombre del archivo desencriptado: ')
            with open(os.path.join(ruta_destino, nombre_destino), "wb") as archivo_destino:
                archivo_destino.write(contenido_bytes) 
            print('El archivo se ha desencriptado correctamente.')
    except Exception as error:
        if FileNotFoundError:
            print('Alguna de las rutas no existe:',ruta_origen ,ruta_destino)
        print('Ha ocurrido un error: ', error)
    input('Pulsa cualquier tecla para continuar: ')
    
Menu()
    
