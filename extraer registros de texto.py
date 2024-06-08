import os
import tkinter as tk
from tkinter import filedialog

def leer_registros_T(archivo_bc3):
    registros_T = {}  # Diccionario para almacenar los registros T

    # Obtener la ruta absoluta del archivo *.bc3
    archivo_bc3 = os.path.abspath(archivo_bc3)

    # Obtener el nombre del archivo bc3 sin la extensión
    bc3_filename_without_ext = os.path.splitext(os.path.basename(archivo_bc3))[0]

    # Obtener la ruta del directorio del archivo bc3
    bc3_dir = os.path.dirname(archivo_bc3)

    with open(archivo_bc3, 'rb') as f:
        contenido_actual = None
        for linea in f:
            try:
                linea_decodificada = linea.decode('utf-8').strip()  # Decodificar de bytes a str y eliminar espacios en blanco
            except UnicodeDecodeError:
                linea_decodificada = linea.decode('iso-8859-1').strip()  # Intentar decodificar con ISO-8859-1 si falla con UTF-8

            if linea_decodificada.startswith('~T'):  # Verificar si la línea comienza con "~T"
                campos = linea_decodificada.split('|')
                if len(campos) >= 3:
                    # Obtener el CODIGO_CONCEPTO
                    codigo_concepto = campos[1].strip()

                    # Almacenar el registro T en una lista dentro del diccionario
                    if codigo_concepto not in registros_T:
                        registros_T[codigo_concepto] = []
                    contenido_actual = registros_T[codigo_concepto]

            # Añadir la línea al contenido actual si hay un concepto abierto
            if contenido_actual is not None:
                contenido_actual.append(linea_decodificada)

    # Crear el directorio "TXT" si no existe
    txt_dir = os.path.join(bc3_dir, bc3_filename_without_ext, "TXT")
    if not os.path.exists(txt_dir):
        os.makedirs(txt_dir)

    # Contador de archivos creados
    archivos_creados = 0


    # Guardar cada registro T en un archivo individual en el directorio creado
    for codigo_concepto, lineas in registros_T.items():
        nombre_archivo = os.path.join(txt_dir, f"{codigo_concepto}.txt")
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            for linea in lineas:
                f.write(linea + '\n')
    
    # Devolver el número de archivos creados

    return archivos_creados                 

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
        leer_registros_T(archivo_bc3)
        print("Los conceptos se han guardado en el directorio 'TXT'.")
        #print(f"Se han creado {archivos_creados} archivos en el directorio 'TXT'.")
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
