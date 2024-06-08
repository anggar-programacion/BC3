import os
import tkinter as tk
from tkinter import filedialog

def leer_Programa(archivo_bc3):
    Version = None  # Variable para almacenar la versión del archivo

    try:
        with open(archivo_bc3, 'rb') as f:
            for linea in f:
                if linea.startswith(b'~V'):  # Verificar si la línea comienza con "~V"
                    campos = linea.decode('iso-8859-1').strip().split('|')
                    if len(campos) > 4:  # Asegurarse de que haya al menos 3 campos
                        Programa = campos[3]
                    break  # Romper el bucle después de encontrar la línea ~V
    except FileNotFoundError:
        print(f"Error: Archivo {archivo_bc3} no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo {archivo_bc3}: {e}")
    
    return Programa

def seleccionar_archivo_bc3():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

def main():
    archivo_bc3 = seleccionar_archivo_bc3()
    if archivo_bc3:
        Programa = leer_Programa(archivo_bc3)
        if Programa:
            print("El programa que creó este archivo es:", Programa)
        else:
            print("No se encontró información de la versión BC3 en el archivo.")
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()

