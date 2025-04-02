secuencias_dna = input('Ingrese una o más secuencias de DNA, separadas por "," (coma): ')
secuencias_dna = secuencias_dna.split(',') # Separar las secuencias por cada coma, reutilizando la variable

secuencias_rna = [secuencia.replace('T', 'U') for secuencia in secuencias_dna] # Reemplazar T por U en cada secuencia

# Guardar secuencias en un archivo
with open('/home/majiso/Desktop/LCG_Gen22/LCG_Sem2/Python/comprension_listas-archivos/results/secuencias_arn.txt', 'w') as archivo:
    for secuencia in secuencias_rna:
        archivo.write(f'{secuencia}\n')