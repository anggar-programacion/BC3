import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox


def leer_primer_registro_V(archivo):
    # Codificaciones a intentar
    codificaciones = ['utf-8', 'latin-1', 'iso-8859-1']
    
    for codificacion in codificaciones:
        try:
            with open(archivo, 'rb') as f:
                primera_linea = f.readline().decode(codificacion).strip()  # Leer la primera línea y decodificar de bytes a str

                # Dividir la línea en campos usando '|' como delimitador
                campos = primera_linea.split('|')

                # Imprimir cada campo con su correspondiente etiqueta
                etiquetas = ["REGISTRO", "PROPIEDAD_ARCHIVO", "VERSION_FORMATO", "PROGRAMA_EMISION", "CABECERA",
                             "JUEGO_CARACTERES", "COMENTARIO", "TIPO_INFORMACION",
                             "NUMERO_CERTIFICACION", "FECHA_CERTIFICACION", "URL_BASE"]

                for etiqueta, campo in zip(etiquetas, campos):
                    if etiqueta == "TIPO_INFORMACION":
                        tipo_informacion = campo.strip()
                        # Mapeo de números a textos equivalentes
                        mapeo = {
                            '1': 'Base de datos',
                            '2': 'Presupuesto',
                            '3': 'Certificación (a origen)',
                            '4': 'Actualización de base de datos'
                        }
                        tipo_texto = mapeo.get(tipo_informacion, "Tipo no especificado")
                        print(f"{etiqueta}: {tipo_texto}")
                    else:
                        print(f"{etiqueta}: {campo.strip()}")
                    
                # Salir del bucle si se ha podido leer correctamente
                return
        except UnicodeDecodeError:
            continue


    # Si no se puede leer con ninguna codificación, imprimir un mensaje de error
    print("No se pudo decodificar el archivo con ninguna codificación compatible.")

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

leer_primer_registro_V(archivo_bc3)



