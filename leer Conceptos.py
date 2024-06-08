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
    
    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~C'):  # Verificar si la línea comienza con "~C"
                contador_registros_C += 1
                campos = linea.decode('iso-8859-1').strip().split('|')  # Decodificar con ISO-8859-1 y dividir la línea en campos usando '|'

                # Imprimir la línea completa con etiquetas
                etiquetas = ["CODIGO", "UNIDAD", "RESUMEN", "PRECIO", "FECHA", "TIPO"]
                for etiqueta, campo in zip(etiquetas, campos[1:]):  # Empezar desde el segundo campo
                    if etiqueta == "TIPO":
                        tipo_equivalente = equivalencias_tipo.get(campo.strip(), "Desconocido")
                        print(f"{etiqueta}: {tipo_equivalente}")
                    else:
                        print(f"{etiqueta}: {campo.strip()}")

                print()  # Imprimir una línea en blanco para separar las entradas

    print(f"Total de registros de tipo ~C: {contador_registros_C}")


# Ejemplo de uso
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/5VIVIENDAS.bc3'
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/31-045R_FASE 1v2.bc3'
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/JUNTA  ANDALUCIA 2023 JUL.bc3'
archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/BDCG18C1S.bc3'



leer_registros_C(archivo_bc3)
