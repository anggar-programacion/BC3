import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox


def contar_registros_ambito_geografico(archivo):
    ambitos_geograficos = {}
    total_registros = 0

    # Diccionario de abreviaturas y nombres completos de ámbitos geográficos
    abreviaturas = {
        'E': 'España',
        'AND': 'Comunidad Autónoma de Andalucía',
        'AL': 'Almería',
        'CO': 'Córdoba',
        'H': 'Huelva',
        'CA': 'Cádiz',
        'GR': 'Granada',
        'J': 'Jaén',
        'MA': 'Málaga',
        'SE': 'Sevilla',
        'ARA': 'Comunidad Autónoma de Aragón',
        'TE': 'Teruel',
        'HU': 'Huesca',
        'Z': 'Zaragoza',
        'AST': 'Comunidad Autónoma del Principado de Asturias',
        'O': 'Asturias',
        'BAL': 'Comunidad Autónoma de las Islas Baleares',
        'PM': 'Baleares',
        'CAN': 'Comunidad Autónoma de Canarias',
        'GC': 'Las Palmas',
        'TF': 'Tenerife',
        'CBR': 'Comunidad Autónoma de Cantabria',
        'S': 'Cantabria',
        'CLM': 'Comunidad Autónoma de Castilla-La Mancha',
        'AB': 'Albacete',
        'CR': 'Ciudad Real',
        'CU': 'Cuenca',
        'GU': 'Guadalajara',
        'TO': 'Toledo',
        'CAL': 'Comunidad Autónoma de Castilla y León',
        'AV': 'Ávila',
        'SG': 'Segovia',
        'SO': 'Soria',
        'VA': 'Valladolid',
        'BU': 'Burgos',
        'LE': 'León',
        'P': 'Palencia',
        'SA': 'Salamanca',
        'ZA': 'Zamora',
        'CAT': 'Comunidad Autónoma de Cataluña',
        'B': 'Barcelona',
        'GI': 'Girona',
        'T': 'Tarragona',
        'L': 'Lleida',
        'EXT': 'Comunidad Autónoma de Extremadura',
        'BA': 'Badajoz',
        'CC': 'Cáceres',
        'GAL': 'Comunidad Autónoma de Galicia',
        'LU': 'Lugo',
        'OR': 'Ourense',
        'PO': 'Pontevedra',
        'C': 'A Coruña',
        'MAD': 'Comunidad de Madrid',
        'M': 'Madrid',
        'MUR': 'Comunidad Autónoma de la Región de Murcia',
        'MU': 'Murcia',
        'NAV': 'Comunidad Foral de Navarra',
        'NA': 'Navarra',
        'PVA': 'Comunidad Autónoma del País Vasco',
        'VI': 'Álava',
        'BI': 'Bizkaia',
        'SS': 'Guipuzkoa',
        'RIO': 'Comunidad Autónoma de La Rioja',
        'LO': 'La Rioja',
        'VAL': 'Comunidad Valenciana',
        'V': 'Valencia',
        'A': 'Alicante',
        'CS': 'Castellón'
    }

    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~W'):  # Verificar si la línea comienza con "~W"
                campos = linea.decode('iso-8859-1').strip().split('|')  # Decodificar con ISO-8859-1 y dividir la línea en campos usando '|'

                # Extraer el ámbito geográfico de la línea
                abrev_ambito = campos[1].lstrip('<').split('\\')[0].strip()
                ambito_completo = campos[1].lstrip('<').split('\\')[1].strip()

                # Asociar la abreviatura con el nombre completo del ámbito geográfico
                ambitos_geograficos[abrev_ambito] = abreviaturas.get(abrev_ambito, ambito_completo)

                # Incrementar el contador total de registros
                total_registros += 1
    
    return ambitos_geograficos, total_registros

def seleccionar_archivo_bc3():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo BC3",
        filetypes=[("Archivos BC3", "*.bc3")],
    )
    return ruta_archivo

archivo_bc3 = seleccionar_archivo_bc3()



ambitos, total_registros = contar_registros_ambito_geografico(archivo_bc3)

# Imprimir los ámbitos geográficos y el total de registros
for abrev_ambito, ambito_completo in ambitos.items():
    print(f"Abreviatura: {abrev_ambito}, Ámbito: {ambito_completo}")

print(f"Total de registros de ámbito geográfico: {total_registros}")

