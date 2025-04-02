with open('/home/majiso/Desktop/LCG_Gen22/LCG_Sem2/Python/comprension_listas-archivos/data/secuencias.fasta.txt', 'r') as archivo:
    lineas = archivo.readlines()

numero_secuencias = [] # Lista vacía (hubiera usado un contador y ya pero el ejercicio pide el uso de len)

numero_secuencias = [linea for linea in lineas if linea.startswith('>')] # Sólo líneas de IDs (que empiecen con >)

print(f'Número de secuencias: {len(numero_secuencias)}')