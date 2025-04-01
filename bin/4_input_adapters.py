# Leer archivo
with open('/home/majiso/Desktop/LCG_Gen22/LCG_Sem2/Python/comprension_listas-archivos/data/4_input_adapters.txt', 'r') as archivo: # modo de lectura
    lineas = archivo.readlines() # Para cerrar el archivo

# Hacer nuevas líneas
nuevas_lineas = [linea.strip()[14:] for linea in lineas] # List comprehension

# Guardar las líneas sin adaptadores en un nuevo archivo
with open('/home/majiso/Desktop/LCG_Gen22/LCG_Sem2/Python/comprension_listas-archivos/results/4_input_no_adapters.txt', 'w') as archivo:
    for linea in nuevas_lineas:
        archivo.write(f'{linea}\n')