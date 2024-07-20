import tkinter as tk
from tkinter import filedialog
import os

def extraer_registros_D(archivo):
    contador_registros_D = 0
    registros_D = []

    # Obtener el nombre base del archivo sin la extensión
    nombre_base = os.path.splitext(os.path.basename(archivo))[0]

    # Crear el directorio para los registros ~D
    directorio_salida = os.path.join(os.path.dirname(archivo), nombre_base)
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    # Nombre del archivo de salida para los registros ~D
    archivo_salida = os.path.join(directorio_salida, f"{nombre_base}_registros_D.txt")

    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~D'):
                contador_registros_D += 1
                registros_D.append(linea.decode('iso-8859-1').strip())

    # Escribir los registros en el archivo de salida
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        for registro in registros_D:
            f.write(registro + '\n')

    # Imprimir el total de registros ~D encontrados
    print(f"Se encontraron {contador_registros_D} registros que empiezan por ~D.")
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
        extraer_registros_D(archivo_bc3)
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
