def leer_registro_K(archivo):
    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~K'):  # Verificar si la línea comienza con "~K"
                linea_decodificada = linea.decode('utf-8').strip()  # Decodificar de bytes a str y eliminar espacios en blanco
                campos = linea_decodificada.split('|')[1].strip().split('\\')[:-1]  # Extraer los campos relevantes

                # Imprimir cada campo con su correspondiente etiqueta
                etiquetas = ["DN", "DD", "DS", "DR", "DI", "DP", "DC", "DM", "DIVISA"]
                for etiqueta, campo in zip(etiquetas, campos):
                    print(f"{etiqueta}: {campo}")

# Ejemplo de uso
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/5VIVIENDAS.bc3'
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/31-045R_FASE 1v2.bc3'
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/JUNTA  ANDALUCIA 2023 JUL.bc3'
archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/BDCG18C1S.bc3'
leer_registro_K(archivo_bc3)

