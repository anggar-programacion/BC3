import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from tabulate import tabulate

def extraer_lineas_precios_elementales(archivo):
    lineas_precios_elementales = []
    try:
        with open(archivo, 'rb') as f:
            for linea in f:
                if linea.startswith(b'~C'):  # Verificar si la línea comienza con "~C"
                    campos = linea.decode('iso-8859-1').strip().split('|')
                    if len(campos) >= 4:
                        segundo_campo = campos[1]
                        if segundo_campo.endswith('$'):
                            codigo_precio = segundo_campo.rstrip('$')
                            unidad = campos[2].strip()
                            texto_reducido = campos[3].strip()
                            lineas_precios_elementales.append((codigo_precio, unidad, texto_reducido))
    except FileNotFoundError:
        print(f"Error: Archivo {archivo} no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
    
    return lineas_precios_elementales

def seleccionar_archivo_bc3():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

def main():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    archivo_bc3 = seleccionar_archivo_bc3()
    if archivo_bc3:
        lineas_precios_elementales = extraer_lineas_precios_elementales(archivo_bc3)
        if lineas_precios_elementales:
            print(tabulate(lineas_precios_elementales, headers=["Código de Precio", "Unidad", "Texto Reducido"], tablefmt="pretty", stralign="left"))
        else:
            print("No se encontraron precios elementales en el archivo.")
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
