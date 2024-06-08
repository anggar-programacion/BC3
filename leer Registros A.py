def desgranar_registro_A(archivo):
    with open(archivo, 'rb') as f:
        for linea in f:
            if linea.startswith(b'~A'):  # Verificar si la línea comienza con "~A"
                campos = linea.decode('iso-8859-1').strip().split('|')  # Decodificar con ISO-8859-1 y dividir la línea en campos usando '|'

                # Imprimir la línea completa con etiquetas
                etiquetas = ["CODIGO_CONCEPTO", "CLAVE_TESAURO"]
                for etiqueta, campo in zip(etiquetas, campos[1:]):  # Empezar desde el segundo campo
                    if etiqueta == "CLAVE_TESAURO":
                        # Eliminar caracteres especiales de inicio y fin
                        campo = campo.lstrip('<').rstrip('>')
                        # Eliminar espacios en blanco
                        campo = campo.replace(' ', '_')
                        # Separar las claves de tesauro
                        claves = campo.split('\\')
                        for clave in claves:
                            print(f"{etiqueta}: {clave.strip()}")
                    else:
                        print(f"{etiqueta}: {campo.strip()}")

                print()  # Imprimir una línea en blanco para separar las entradas

# Ejemplo de uso
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/5VIVIENDAS.bc3'
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/31-045R_FASE 1v2.bc3'
#archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/JUNTA  ANDALUCIA 2023 JUL.bc3'
archivo_bc3 = 'C:/Users/ANGEL/Desktop/FIEBDC/BC3/BDCG18C1S.bc3'

desgranar_registro_A(archivo_bc3)


