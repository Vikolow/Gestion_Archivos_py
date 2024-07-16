import os
import shutil
from cryptography.fernet import Fernet



#------------------------------ Funciones para obtener ruta y nombre  ------------------------------
def obtener_ruta_nombre():
    """Pide y guarda la ruta y el nombre del archivo."""

    ruta = input('Indica la ruta: ')
    nombre = input('Indica el nombre del fichero: ')
    os.system("cls")
    return os.path.join(ruta, nombre)

def mostrar_mensaje_error(error, mensaje):
    """Muestra un mensaje de error."""
    print(f"{mensaje}: {error}")

#------------------------------ Funciones  de Ficheros ------------------------------
def crear_archivo():
    """Crea un archivo en la ruta especificada."""

    try:
        ruta_nombre = obtener_ruta_nombre()
        with open(ruta_nombre, "w") as archivo:
            pass
        print(f'El archivo se creó correctamente en {ruta_nombre}')
    except FileNotFoundError:
        print(f'No se ha encontrado: {ruta_nombre}')
    except Exception as error:
        mostrar_mensaje_error('Error al crear el archivo',error)
    input('Pulsa cualquier tecla para continuar: ')


def escribir_archivo():
    """Escribe texto en un archivo existente."""
    try:
        ruta_nombre = obtener_ruta_nombre()
        texto = input('Introduce el texto a escribir: ')
        with open(ruta_nombre, "a") as archivo:
            archivo.write('\n' + texto)
        print(f'El texto se ha escrito correctamente en {ruta_nombre}')
    except FileNotFoundError:
        print(f'No se ha encontrado: {ruta_nombre}')    
    except Exception as error:
        mostrar_mensaje_error('Error al escribir en el archivo',error)
    input('Pulsa cualquier tecla para continuar: ')


def leer_archivo():
    """Lee el contenido de un archivo."""
    try:
        ruta_nombre = obtener_ruta_nombre()
        with open(ruta_nombre, "r") as archivo:
            contenido = archivo.read()
        print('El contenido del fichero es:')
        print('\n' + contenido + '\n')
    except FileNotFoundError:
        print(f'No se ha encontrado: {ruta_nombre}')
    except Exception as error:
        mostrar_mensaje_error('Error al leer el archivo',error)
    input('Pulsa cualquier tecla para continuar: ')


def copiar_archivo():
    """Copia un archivo de una ruta a otra."""
    try:
        ruta_origen = input('Indica la ruta del fichero origen: ')
        ruta_destino = input('Indica la ruta del fichero destino: ')
        shutil.copy(ruta_origen, ruta_destino)
        print('El archivo se ha copiado correctamente.')
    except FileNotFoundError:
        print(f'No se ha encontrado: {ruta_origen} o {ruta_destino}')
    except Exception as error:
        mostrar_mensaje_error('Error al copiar el archivo',error)
    input('Pulsa cualquier tecla para continuar: ')


#------------------------------ Funciones de Clave de Encriptación ------------------------------
def generar_clave():
    """Genera una clave y la guarda en un archivo."""
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as clave_archivo:
        clave_archivo.write(clave)

def cargar_clave():
    """Carga la clave desde el archivo."""
    return open("clave.key", "rb").read()

# Generar una clave al iniciar 
if not os.path.exists("clave.key"):
    generar_clave()

# Cargar la clave
clave = cargar_clave()
cipher = Fernet(clave)

#------------------------------ Funciones de Encriptación ------------------------------
def encriptar_archivo():
    """Encripta un archivo y lo guarda en la ubicación especificada."""
    try:
        ruta_origen = obtener_ruta_nombre()
        with open(ruta_origen, "rb") as archivo_origen:
            contenido = archivo_origen.read()
            contenido_encriptado = cipher.encrypt(contenido)
        print("Introduce la ruta donde quieres guardar el fichero encriptado")
        ruta_destino = obtener_ruta_nombre()
        with open(ruta_destino, "wb") as archivo_destino:
            archivo_destino.write(contenido_encriptado)
        print('El archivo se ha encriptado correctamente.')
    except Exception as error:
        mostrar_mensaje_error('Error al encriptar el archivo',error)
    input('Pulsa cualquier tecla para continuar: ')


def desencriptar_archivo():
    """Desencripta un archivo y lo guarda en la ubicación especificada."""
    try:
        ruta_origen = obtener_ruta_nombre()
        with open(ruta_origen, "rb") as archivo_encriptado:
            contenido_encriptado = archivo_encriptado.read()
            contenido_desencriptado = cipher.decrypt(contenido_encriptado)
        print("Introduce la ruta donde quieres guardar el fichero desencriptado")
        ruta_destino = obtener_ruta_nombre()
        with open(ruta_destino, "wb") as archivo_destino:
            archivo_destino.write(contenido_desencriptado)
        print('El archivo se ha desencriptado correctamente.')
    except Exception as error:
        mostrar_mensaje_error('Error al desencriptar el archivo' ,error)
    input('Pulsa cualquier tecla para continuar: ')

#------------------------------ Menú de Opciones ------------------------------
def menu():
    """Muestra el menú de opciones para la gestión de ficheros."""
    while True:
        print('\n***************************')
        print('Gestion de Ficheros-Python')
        print('Desarrollado por: Vikolow')
        print('\n***************************')
        print('\nMenu de opciones:\n')
        print('1-Crear un fichero')
        print('2-Escribir dentro de un fichero')
        print('3-Leer el contenido de un archivo')
        print('4-Copiar un fichero')
        print('5-Encriptar un fichero')
        print('6-Desencriptar un fichero')
        print('7-Salir')
        print('\n')

        opcion = input('Elige una opcion: ')
        os.system('cls')

        if not opcion.isdigit():
            print('Por favor, introduce un número válido.')
            input('Pulsa cualquier tecla para continuar')
            continue
        
        opcion = int(opcion)

        if opcion == 1:
            crear_archivo()
        elif opcion == 2:
            escribir_archivo()
        elif opcion == 3:
            leer_archivo()
        elif opcion == 4:
            copiar_archivo()
        elif opcion == 5:
            encriptar_archivo()
        elif opcion == 6:
            desencriptar_archivo()
        elif opcion == 7:
            print('¡Hasta Pronto!')
            break
        else:
            print('El número no está en el rango indicado.')
            input('Pulsa cualquier tecla para continuar')

# Ejecutar el menú
menu()
