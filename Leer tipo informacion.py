import os
import tkinter as tk
from tkinter import filedialog

def leer_Tipo_Informacion(archivo_bc3):
    Tipo_Informacion = None  # Variable para almacenar el tipo de información

    try:
        with open(archivo_bc3, 'rb') as f:
            for linea in f:
                if linea.startswith(b'~V'):  # Verificar si la línea comienza con "~V"
                    
                    campos = linea.decode('iso-8859-1').strip().split('|')
                    if len(campos) > 8:  # Asegurarse de que haya al menos 10 campos
                        tipo_info = campos[7]
                        if tipo_info == '1':
                            Tipo_Informacion = 'Base de datos'
                        elif tipo_info == '2':
                            Tipo_Informacion = 'Presupuesto'
                        elif tipo_info == '3':
                            Tipo_Informacion = 'Certificación (a origen)'
                        elif tipo_info == '4':
                            Tipo_Informacion = 'Actualización de base de datos'
                        else:
                            Tipo_Informacion = 'Tipo no estándar'

                    break  # Romper el bucle después de encontrar la línea ~V
    except FileNotFoundError:
        print(f"Error: Archivo {archivo_bc3} no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo {archivo_bc3}: {e}")
    
    return Tipo_Informacion

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
        Tipo_Informacion = leer_Tipo_Informacion(archivo_bc3)
        if Tipo_Informacion:
            print("La información de este archivo es de tipo:", Tipo_Informacion)
        else:
            print("No se encontró información de tipo en el archivo.")
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
