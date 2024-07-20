import tkinter as tk
from tkinter import filedialog
import os

def extraer_registros_N(archivo):
    contador_registros_N = 0
    registros_N = []

    # Obtener el nombre base del archivo sin la extensión
    nombre_base = os.path.splitext(os.path.basename(archivo))[0]

    # Crear el directorio para los registros ~N
    directorio_salida = os.path.join(os.path.dirname(archivo), nombre_base)
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    # Nombre del archivo de salida para los registros ~n
    archivo_salida = os.path.join(directorio_salida, f"{nombre_base}_registros_N.txt")

    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~N'):
                contador_registros_N += 1
                registros_N.append(linea.decode('iso-8859-1').strip())

    # Escribir los registros en el archivo de salida
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        for registro in registros_N:
            f.write(registro + '\n')

    # Imprimir el total de registros ~D encontrados
    print(f"Se encontraron {contador_registros_N} registros que empiezan por ~N.")
    print(f"Los registros se han guardado en el archivo: {archivo_salida}")

def seleccionar_archivo_bc3():
    root = tk.Tk()
    root.withdraw()
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

def main():
    archivo_bc3 = seleccionar_archivo_bc3()
    if archivo_bc3:
        extraer_registros_N(archivo_bc3)
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
