import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox


def contar_registros_capitulos(archivo):
    
    total_capitulos = 0

    
    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~C'):  # Verificar si la línea comienza con "~C"
                campos = linea.decode('iso-8859-1').strip().split('|')  # Decodificar con ISO-8859-1 y dividir la línea en campos usando '|'

                # Incrementar el contador total de registros
                total_capitulos += 1
    
    return total_capitulos


def seleccionar_archivo_bc3():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

archivo_bc3 = seleccionar_archivo_bc3()



total_capitulos = contar_registros_capitulos(archivo_bc3)

# Imprimir los ámbitos geográficos y el total de registros


print(f"Total de registros de capitulos: {total_capitulos}")

