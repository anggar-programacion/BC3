import os
import tkinter as tk
from tkinter import filedialog, simpledialog
from tabulate import tabulate
import textwrap

def leer_registros_C(archivo):
    # Diccionario de equivalencias de tipo
    equivalencias_tipo = {
        "0": "Sin clasificar",
        "1": "Mano de obra",
        "2": "Maquinaria y medios auxiliares",
        "3": "Materiales",
        "4": "Componentes adicionales de residuo",
        "5": "Clasificación de residuo"
    }

    contador_registros_C = 0
    datos = []

    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~C'):  # Verificar si la línea comienza con "~C"
                contador_registros_C += 1
                campos = linea.decode('iso-8859-1').strip().split('|')  # Decodificar con ISO-8859-1 y dividir la línea en campos usando '|'

                # Obtener los valores de los campos
                codigo = campos[1].strip()
                unidad = campos[2].strip()
                resumen = campos[3].strip()
                precio = campos[4].strip()
                fecha = campos[5].strip()
                tipo = equivalencias_tipo.get(campos[6].strip(), "Desconocido")

                # Tratar los conceptos que terminan en "##" o "#" como capítulos
                if codigo.endswith('##') or codigo.endswith('#'):
                    capitulo = textwrap.shorten(resumen, width=25, placeholder="...")
                    resumen = ''
                else:
                    capitulo = ''

                # Dividir el resumen en líneas de 50 caracteres
                resumen_lines = textwrap.fill(resumen, width=50)

                # Añadir la fila de datos a la lista
                datos.append([capitulo, codigo, unidad, resumen_lines, precio, fecha, tipo])

    # Imprimir los datos en formato de tabla en la consola
    print(tabulate(datos, headers=["CAPITULOS", "CODIGO", "UNIDAD", "RESUMEN", "PRECIO", "FECHA", "TIPO"], tablefmt="grid"))

    # Crear el directorio "Conceptos" en un subdirectorio con el nombre del archivo BC3
    nombre_archivo = os.path.splitext(os.path.basename(archivo))[0]
    conceptos_dir = os.path.join(os.path.dirname(archivo), nombre_archivo, "Conceptos")
    if not os.path.exists(conceptos_dir):
        os.makedirs(conceptos_dir)

    # Escribir los datos en el archivo de texto con el mismo formato que en la consola
    with open(os.path.join(conceptos_dir, f"{nombre_archivo}_CONCEPTOS.TXT"), 'w', encoding='utf-8') as file:
        file.write(tabulate(datos, headers=["CAPITULOS", "CODIGO", "UNIDAD", "RESUMEN", "PRECIO", "FECHA", "TIPO"], tablefmt="grid"))

    # Imprimir el total de registros de tipo ~C
    print(f"\nTotal de registros de tipo ~C: {contador_registros_C}")

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
        leer_registros_C(archivo_bc3)
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()

