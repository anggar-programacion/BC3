import os
import tkinter as tk
from tkinter import filedialog

def contar_registros_P(archivo):
    # Inicializar el contador para las líneas que empiezan con ~P
    contador_p = 0

    try:
        with open(archivo, 'rb') as f:  # Abrir en modo binario 'rb'
            for linea in f:
                # Verificar si la línea comienza con ~P
                if linea.startswith(b'~P'):
                    contador_p += 1
    except FileNotFoundError:
        print(f"Error: Archivo {archivo} no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
    
    return contador_p

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
        contador_p = contar_registros_P(archivo_bc3)
        print(f"Total de Registros de Parámetros: {contador_p}")
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
