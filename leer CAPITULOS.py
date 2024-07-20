import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from tabulate import tabulate

def extraer_lineas_capitulo(archivo):
    lineas_capitulos = []
    nombre_medicion = None

    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~C'):  # Verificar si la línea comienza con "~C"
                # Decodificar la línea y dividirla en campos usando '||'
                campos = linea.decode('iso-8859-1').strip().split('||')
                
                # Verificar si hay al menos 2 campos después de dividir por '||'
                if len(campos) >= 2:
                    # El primer campo contiene la parte que empieza con '~C' y el código del capítulo
                    primer_campo = campos[0].split('|')
                    
                    # Verificar si el segundo campo del primer_campo termina en '#' o '##'
                    if len(primer_campo) >= 2:
                        if primer_campo[1].endswith('##'):
                            nombre_medicion = primer_campo[1].rstrip('#')
                        elif primer_campo[1].endswith('#'):
                            codigo_capitulo = primer_campo[1].rstrip('#')
                            # El título del capítulo está en el segundo campo, pero quitamos cualquier texto adicional después del primer '|'
                            titulo_codigo = campos[1].split('|')[0].strip()
                            lineas_capitulos.append((codigo_capitulo, titulo_codigo))
    #print (lineas_capitulos)
    return nombre_medicion, lineas_capitulos

def seleccionar_archivo_bc3():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

archivo_bc3 = seleccionar_archivo_bc3()

nombre_medicion, lineas_capitulos = extraer_lineas_capitulo(archivo_bc3)

# Imprimir el nombre de la medición y los códigos de capítulo y sus títulos extraídos en forma tabulada
if nombre_medicion:
    print(f"Nombre de la medición: {nombre_medicion}\n")

print(tabulate(lineas_capitulos, headers=["Código de Capítulo", "Título del Capítulo"], tablefmt="pretty", stralign="left"))
