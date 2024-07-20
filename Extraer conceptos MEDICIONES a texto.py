import os
import tkinter as tk
from tkinter import filedialog
import openpyxl
import textwrap
from datetime import datetime



# Función para verificar si un valor es numérico
def es_numero(valor):
    try:
        float(valor)
        return float(valor)
    except ValueError:
        return valor


def es_numero_b(valor):
    try:
        float(valor)
        return float(valor)
    except ValueError:
        return 1.0

    
# Función para verificar si un valor es fecha

def es_fecha(valor):
    try:
        if len(valor) != 6:
            raise ValueError("Longitud de cadena incorrecta. Se esperan 6 caracteres.")
            print(valor)
        
        dia = int(valor[:2])
        mes = int(valor[2:4])
        anno = 2000 + int(valor[4:6])  # Suponiendo que los años están en formato YY

        fecha = datetime(anno, mes, dia)
        fecha_formateada = fecha.strftime("%d/%m/%Y")  # Formatear la fecha como DD/MM/YYYY
        return fecha_formateada

    except ValueError as e:
        print(f"Error al convertir a fecha: {e}")
        return None


def leer_registros_M(archivo):
    lineas_Medicion = []
    num_lineasM=0

    with open(archivo, 'r', encoding='iso-8859-1') as f:
        for linea in f:
            if linea.startswith('~M'):

                #Ejemplo:['', '1#\\01TLL00100', '1\\1\\', '242.23', '\\SOLAR\\1\\242.23\\\\\\', '']
                linea_sin_m = linea[2:].strip()
                campos = linea_sin_m.split('|')
                #print (campos)

                campo1=campos[1].strip()

                # Separar el campo en dos partes usando '\'
                partes = campo1.split('\\')
                
                # Asignar las partes a variables
                cod_capitulo = partes[0]  # '1#'
                #Elimina el caracter indicador de capitulo
                cod_capitulo=cod_capitulo.split("#")
                #Codigo del codigo de la partida
                codigo = partes[1]  # '01TLL00100'
                #campo 2 posicion     1\\1\\       
                posicion = campos[2].strip()
                posicion=posicion.split('\\')
                posi1=es_numero(posicion[0])
                posi2=es_numero(posicion[1])
                posi3=es_numero(posicion[2])
                #print (posi1,posi2,posi3)
                #campo 3 medicion_parcial '242.23'
                medicion_parcial = es_numero(campos[3].strip())
                #campo 4 el resto de cosas de la linea '\\SOLAR\\1\\242.23\\\\\\'
                resto_campos =campos[4].strip()
                #campo5 etiqueta '' casi siempre vacia
                etiqueta=campos[5].strip()

                #print (cod_capitulo,codigo,posicion,medicion_parcial,resto_campos,etiqueta)

                #ahora separamos el resto campos en varios si hay varios.
                subcampos = resto_campos.strip().split('\\')
                #print(subcampos)
                

                # El primer elemento es 'tipo', luego procesamos en bloques de 6 elementos.
                tipo = subcampos[0].strip()
                subcampos = subcampos[1:]  # Eliminar 'tipo' de la lista de subcampos

                # Procesar definiciones múltiples en bloques de 6
                num_elementos_por_bloque = 6

                for i in range(0, len(subcampos), num_elementos_por_bloque):
                    bloque = subcampos[i:i + num_elementos_por_bloque]

                    # Verificar que el bloque tenga exactamente 6 elementos
                    if len(bloque) == num_elementos_por_bloque:
                        comentario = bloque[0].strip()
                        unidades = es_numero_b(bloque[1].strip())
                        longitud = es_numero_b(bloque[2].strip())
                        latitud = es_numero_b(bloque[3].strip())
                        altura = es_numero_b(bloque[4].strip())
                        clave = bloque[5].strip()
                        medicion_calculada = longitud * latitud * altura
                        print(cod_capitulo,posi1,posi2,posi3, medicion_parcial, codigo,comentario, unidades, longitud, latitud, altura, medicion_calculada, clave)
                        lineas_Medicion.append([cod_capitulo,posi1,posi2,posi3, medicion_parcial, codigo,comentario, unidades, longitud, latitud, altura, medicion_calculada, clave])

                    else:
                        print("Error: El bloque no tiene suficientes elementos:", bloque)

            

    return lineas_Medicion
    


    # Aquí podrías imprimir o almacenar los datos procesados de alguna manera
    # Ejemplo de impresión de los datos para fines de depuración
    # print(tabulate(datos, headers=["COD_PADRE", "COD_HIJO", "POSICION", "MEDICION_TOTAL", "TIPO_COMENTARIO", "UNIDADES", "LONGITUD", "LATITUD", "ALTURA", "ETIQUETA"], tablefmt="grid"))


    


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
        leer_registros_M(archivo_bc3)
        
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
