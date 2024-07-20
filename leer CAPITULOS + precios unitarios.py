import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from tabulate import tabulate

def extraer_capitulos_y_elementos(archivo):
    capitulos_y_elementos = []
    capitulo_actual = None

    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~C'):  # Verificar si la línea comienza con "~C"
                # Decodificar la línea y dividirla en campos usando '|'
                campos = linea.decode('iso-8859-1').strip().split('|')
                
                if len(campos) >= 3:
                    primer_campo = campos[1]
                    
                    # Verificar si es un capítulo
                    if primer_campo.endswith('##') or primer_campo.endswith('#'):
                        if primer_campo.endswith('##'):
                            nombre_medicion = primer_campo.rstrip('#')
                        elif primer_campo.endswith('#'):
                            capitulo_actual = primer_campo.rstrip('#')
                            titulo_capitulo = campos[2].strip()
                            capitulos_y_elementos.append((capitulo_actual, titulo_capitulo, 'Capítulo'))
                    # Verificar si es un precio descompuesto
                    elif primer_campo.endswith('$'):
                        codigo_precio = primer_campo.rstrip('$')
                        if capitulo_actual and codigo_precio.startswith(capitulo_actual):
                            if len(campos) >= 4:
                                unidad = campos[2].strip()
                                texto_reducido = campos[3].strip()
                                capitulos_y_elementos.append((codigo_precio, unidad, texto_reducido, 'Elemento'))  # Añadir 'Elemento' al final
    
    return capitulos_y_elementos

def seleccionar_archivo_bc3():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

archivo_bc3 = seleccionar_archivo_bc3()

if not archivo_bc3:
    print("No se seleccionó ningún archivo.")
    exit()

capitulos_y_elementos = extraer_capitulos_y_elementos(archivo_bc3)

# Separar capítulos y elementos para su visualización tabulada
capitulos = [(codigo, titulo) for codigo, titulo, tipo in capitulos_y_elementos if tipo == 'Capítulo']
elementos = [(codigo, unidad, texto) for codigo, unidad, texto, tipo in capitulos_y_elementos if tipo == 'Elemento']

# Imprimir capítulos y elementos en forma tabulada
print("Capítulos:")
print(tabulate(capitulos, headers=["Código de Capítulo", "Título del Capítulo"], tablefmt="pretty", stralign="left"))

print("\nElementos:")
print(tabulate(elementos, headers=["Código de Elemento", "Unidad", "Texto Reducido"], tablefmt="pretty", stralign="left"))
