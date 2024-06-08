import os
import tkinter as tk
from tkinter import filedialog

def contar_registros_por_tipo(archivo):
    # Inicializar un diccionario para almacenar el conteo de cada tipo de registro
    tipos_validos = "VKCDYRTPLQJWGEOMNIABF"
    contador_registros = {tipo: 0 for tipo in tipos_validos}
    total_registros = 0

    try:
        with open(archivo, 'rb') as f:  # Abrir en modo binario 'rb'
            for linea in f:
                # Verificar si la línea comienza con '~' seguido de uno de los caracteres válidos
                if len(linea) >= 2 and linea[0:1] == b'~':
                    tipo_registro = chr(linea[1])
                    if tipo_registro in tipos_validos:
                        contador_registros[tipo_registro] += 1
                        total_registros += 1
    except FileNotFoundError:
        print(f"Error: Archivo {archivo} no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
    
    return contador_registros, total_registros

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
        contador_por_tipo, total_registros = contar_registros_por_tipo(archivo_bc3)
        # Imprimir el conteo de registros por tipo
        for tipo, contador in contador_por_tipo.items():
            print(f"Tipo {tipo}: {contador} registros")
        # Imprimir el total de registros
        print(f"Total de registros: {total_registros}")
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()



