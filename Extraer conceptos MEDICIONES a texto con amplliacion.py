import os
import tkinter as tk
from tkinter import filedialog
import textwrap
from datetime import datetime
from tabulate import tabulate

# Función para verificar si un valor es numérico
def es_numero(valor, decimales=None):
    try:
        numero = float(valor)
        if decimales is not None:
            numero_redondeado = round(numero, decimales)
            return numero_redondeado
        return numero
    except ValueError:
        return valor

def es_numero_b(valor, decimales=None):
    try:
        numero = float(valor)
        if decimales is not None:
            numero_redondeado = round(numero, decimales)
            return numero_redondeado
        return numero
    except ValueError:
        return 1.0

# Función para verificar si un valor es fecha
def es_fecha(valor):
    try:
        if len(valor) != 6:
            raise ValueError("Longitud de cadena incorrecta. Se esperan 6 caracteres.")
        
        dia = int(valor[:2])
        mes = int(valor[2:4])
        anno = 2000 + int(valor[4:6])  # Suponiendo que los años están en formato YY
        fecha = datetime(anno, mes, dia)
        fecha_formateada = fecha.strftime("%d/%m/%Y")  # Formatear la fecha como DD/MM/YYYY
        return fecha_formateada

    except ValueError as e:
        print(f"Error al convertir a fecha: {e}")
        return None

def leer_registros_C(archivo):
    datos_C = {}
    equivalencias_tipo = {}  # Define este diccionario según tus necesidades

    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~C'):
                campos = linea.decode('iso-8859-1').strip().split('|')
                codigo = campos[1].strip()
                unidad = campos[2].strip()
                resumen = campos[3].strip()
                precio = campos[4].strip()
                fecha = campos[5].strip()
                tipo = equivalencias_tipo.get(campos[6].strip(), "Desconocido")
                datos_C[codigo] = {
                    "unidad": unidad,
                    "resumen": resumen,
                    "precio": precio,
                    "fecha": fecha,
                    "tipo": tipo
                }

    return datos_C

def leer_registros_M(archivo, datos_C):
    lineas_Medicion = []

    with open(archivo, 'r', encoding='iso-8859-1') as f:
        for linea in f:
            if linea.startswith('~M'):
                linea_sin_m = linea[2:].strip()
                campos = linea_sin_m.split('|')
                campo1 = campos[1].strip()
                partes = campo1.split('\\')
                cod_capitulo = partes[0].split("#")[0]
                codigo = partes[1]
                posicion = campos[2].strip().split('\\')
                posi1 = posicion[0]
                posi2 = posicion[1]
                posi3 = posicion[2]
                medicion_parcial = es_numero(campos[3].strip(), 2)
                resto_campos = campos[4].strip()
                etiqueta = campos[5].strip()
                subcampos = resto_campos.strip().split('\\')
                tipo = subcampos[0].strip()
                subcampos = subcampos[1:]

                num_elementos_por_bloque = 6
                for i in range(0, len(subcampos), num_elementos_por_bloque):
                    bloque = subcampos[i:i + num_elementos_por_bloque]
                    if len(bloque) == num_elementos_por_bloque:
                        comentario = bloque[0].strip()
                        unidades = es_numero_b(bloque[1].strip(), 2)
                        longitud = es_numero_b(bloque[2].strip(), 2)
                        latitud = es_numero_b(bloque[3].strip(), 2)
                        altura = es_numero_b(bloque[4].strip(), 2)
                        clave = bloque[5].strip()
                        medicion_calculada = es_numero(longitud * latitud * altura, 2)

                        # Buscar en los datos de ~C
                        datos_c = datos_C.get(codigo, {"unidad": "", "resumen": "", "precio": ""})
                        unidad = datos_c["unidad"]
                        resumen = datos_c["resumen"]
                        precio = es_numero( datos_c["precio"])
                        #Calculamos el precio de la linea
                        parcial_linea=es_numero(medicion_calculada*precio,2)


                        lineas_Medicion.append([
                            cod_capitulo, posi1, posi2, posi3, medicion_parcial, codigo, resumen, precio, unidad, comentario,
                            unidades, longitud, latitud, altura, medicion_calculada,parcial_linea,clave])
                        print(cod_capitulo, posi1, posi2, posi3, medicion_parcial, codigo, resumen, precio, unidad, comentario,unidades, longitud, latitud, altura, medicion_calculada, parcial_linea,clave)

    return lineas_Medicion

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
        datos_C = leer_registros_C(archivo_bc3)
        lineas_Medicion = leer_registros_M(archivo_bc3, datos_C)
        #print(tabulate(lineas_Medicion, headers=["COD_CAPITULO", "POSIC1", "POSIC2", "POSIC3", "MEDICION_CAPITULO", "CODIGO", "RESUMEN", "COMENTARIO","PRECIO" ,"UNIDAD", "UNIDADES", "LARGO", "ANCHO", "ALTO", "MEDICION_LINEA", "ETIQUETA"], tablefmt="grid"))
        #print(cod_capitulo, posi1, posi2, posi3, medicion_parcial, codigo, resumen, precio, unidad, comentario,unidades, longitud, latitud, altura, medicion_calculada, clave)
        #print(lineas_Medicion)
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    main()
