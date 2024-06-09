import os
import tkinter as tk
from tkinter import filedialog, simpledialog

def leer_registros_P(archivo_bc3, codigo_especifico):
    registros_P = {}

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

            if linea_decodificada.startswith('~P'):  # Verificar si la línea comienza con "~P"
                campos = linea_decodificada.split('|')
                if len(campos) >= 1:
                    # Obtener el CODIGO_PARAMETRO
                    codigo_parametro = campos[1].strip().rstrip('$')

                    # Verificar si el código parámetro coincide con el código específico
                    if codigo_parametro == codigo_especifico:
                        if codigo_parametro not in registros_P:
                            registros_P[codigo_parametro] = []
                        contenido_actual = registros_P[codigo_parametro]
                    else:
                        contenido_actual = None

            # Añadir la línea al contenido actual si hay un parámetro abierto
            if contenido_actual is not None:
                contenido_actual.append(linea_decodificada)

    # Crear el directorio "Parametros" si no existe
    parametros_dir = os.path.join(bc3_dir, bc3_filename_without_ext, "Parametros")
    if not os.path.exists(parametros_dir):
        os.makedirs(parametros_dir)

    # Guardar el registro P en un archivo individual en el directorio creado
    for codigo_parametro, lineas in registros_P.items():
        nombre_archivo = os.path.join(parametros_dir, f"{codigo_parametro}.txt")
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            for linea in lineas:
                f.write(linea + '\n')

def seleccionar_archivo_bc3():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

def obtener_codigo_parametro():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    codigo_parametro = simpledialog.askstring("Código Parámetro", "Ingrese el código del parámetro:")
    return codigo_parametro

def main():
    archivo_bc3 = seleccionar_archivo_bc3()
    if archivo_bc3:
        codigo_parametro = obtener_codigo_parametro()
        if codigo_parametro:
            leer_registros_P(archivo_bc3, codigo_parametro)
            print(f"El parámetro '{codigo_parametro}' se ha guardado en el directorio 'Parametros'.")
        else:
            print("No se ingresó ningún código de parámetro.")
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()

