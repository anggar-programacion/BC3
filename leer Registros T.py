import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox

def leer_registros_T(archivo_bc3):
    registros_T = []  # Lista para almacenar los registros T

    # Obtener el nombre del archivo bc3 sin la extensión
    bc3_filename_without_ext = os.path.splitext(os.path.basename(archivo_bc3))[0]

    # Obtener la ruta del directorio del archivo bc3
    bc3_dir = os.path.dirname(archivo_bc3)

    with open(archivo_bc3, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~T'):  # Verificar si la línea comienza con "~T"
                try:
                    linea_decodificada = linea.decode('utf-8').strip()  # Decodificar de bytes a str y eliminar espacios en blanco
                except UnicodeDecodeError:
                    linea_decodificada = linea.decode('iso-8859-1').strip()  # Intentar decodificar con ISO-8859-1 si falla con UTF-8
                campos = linea_decodificada.split('|')  # Dividir la línea en campos usando '|'

                # Verificar si hay al menos tres campos (CODIGO_CONCEPTO, TEXTO_DESCRIPTIVO)
                if len(campos) >= 3:
                    # Obtener el CODIGO_CONCEPTO y el TEXTO_DESCRIPTIVO
                    codigo_concepto = campos[1].strip()
                    texto_descriptivo = '|'.join(campos[2:]).strip()  # Unir los campos restantes en caso de que el texto tenga '|'

                    # Almacenar el registro T en un diccionario
                    registro_T = {"CODIGO_CONCEPTO": codigo_concepto, "TEXTO_DESCRIPTIVO": texto_descriptivo}

                    # Crear el directorio con el nombre del archivo bc3 si no existe
                    txt_dir = os.path.join(bc3_dir, bc3_filename_without_ext, "TXT")
                    if not os.path.exists(txt_dir):
                        os.makedirs(txt_dir)

                    # Generar el nombre del archivo txt
                    nombre_archivo = f"{codigo_concepto}.txt"

                    # Guardar el registro T en un archivo individual en el directorio creado
                    nombre_archivo = os.path.join(txt_dir, nombre_archivo)
                    guardar_registro_T(registro_T, nombre_archivo)

def guardar_registro_T(registro_T, nombre_archivo):
    # Crear el archivo si no existe
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        # Escribir el texto del registro en el archivo
        f.write(registro_T["TEXTO_DESCRIPTIVO"])

# Ruta del archivo *.bc3 (especificar aquí)
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/BDCG18C1S.bc3'

def seleccionar_archivo_bc3():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

archivo_bc3 = seleccionar_archivo_bc3()

# Leer los registros T del archivo especificado
leer_registros_T(archivo_bc3)



