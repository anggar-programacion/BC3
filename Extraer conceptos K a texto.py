import tkinter as tk
from tkinter import filedialog
import os

def extraer_registros_K(archivo):
    registros_K = []
    encabezados_primer_bloque = ["DN", "DD", "DS", "DR", "DI", "DP", "DC", "DM", "DIVISA"]
    encabezados_segundo_bloque = ["CI", "GG", "BI", "BAJA", "IVA"]
    encabezados_tercer_bloque = ["DRC", "DC", "DFS", "DRS", "DUO", "DI", "DES", "DN", "DD", "DS", "DSP", "DEC", "DIVISA"]
    
    # Obtener el nombre base del archivo sin la extensión
    nombre_base = os.path.splitext(os.path.basename(archivo))[0]

    # Crear el directorio para los registros ~K
    directorio_salida = os.path.join(os.path.dirname(archivo), nombre_base)
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    # Nombre del archivo de salida para los registros ~K
    archivo_salida = os.path.join(directorio_salida, f"{nombre_base}_registros_K.txt")

    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~K'):
                registros_K.append(linea.decode('iso-8859-1').strip())

    if registros_K:
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            for registro in registros_K:
                # Extraer los bloques de campos del registro ~K
                bloques = registro.split('|')
                
                if len(bloques) < 5:
                    print(f"Registro inválido encontrado: {registro}")
                    continue

                # Procesar el primer bloque
                primer_bloque = bloques[1].split('\\')
                segundo_bloque = bloques[2].split('\\')
                tercer_bloque = bloques[3].split('\\')
                n_bloque = bloques[4].strip()
                
                # Crear un diccionario para los encabezados y sus valores
                valores = {}

                # Asignar valores a los encabezados del primer bloque
                for i, valor in enumerate(primer_bloque):
                    if i < len(encabezados_primer_bloque):
                        valores[encabezados_primer_bloque[i]] = valor.strip()

                # Asignar valores a los encabezados del segundo bloque
                for i, valor in enumerate(segundo_bloque):
                    if i < len(encabezados_segundo_bloque):
                        valores[encabezados_segundo_bloque[i]] = valor.strip()

                # Asignar valores a los encabezados del tercer bloque
                for i, valor in enumerate(tercer_bloque):
                    if i < len(encabezados_tercer_bloque):
                        valores[encabezados_tercer_bloque[i]] = valor.strip()

                # Agregar el valor de n
                valores["n"] = n_bloque

                # Escribir los encabezados y sus valores en el archivo
                for encabezado, valor in valores.items():
                    f.write(f"{encabezado}: {valor}\n")
                f.write('\n')

        print(f"Se encontró {len(registros_K)} registro(s) que empieza(n) por ~K.")
        print(f"El/Los registro(s) se ha(n) guardado en el archivo: {archivo_salida}")
    else:
        print("No se encontraron registros que empiezan por ~K.")

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
        extraer_registros_K(archivo_bc3)
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
