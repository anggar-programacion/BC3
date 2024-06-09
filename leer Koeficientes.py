import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox


def leer_registro_K(archivo):
    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~K'):  # Verificar si la línea comienza con "~K"
                linea_decodificada = linea.decode('utf-8').strip()  # Decodificar de bytes a str y eliminar espacios en blanco
                campos = linea_decodificada.split('|')[1].strip().split('\\')[:-1]  # Extraer los campos relevantes

                # Imprimir cada campo con su correspondiente etiqueta
                etiquetas = ["DN", "DD", "DS", "DR", "DI", "DP", "DC", "DM", "DIVISA"]
                for etiqueta, campo in zip(etiquetas, campos):
                    print(f"{etiqueta}: {campo}")


def seleccionar_archivo_bc3():
    """
    Función para abrir un cuadro de diálogo y seleccionar un archivo *.bc3
    """
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

archivo_bc3  = seleccionar_archivo_bc3()

leer_registro_K(archivo_bc3)

