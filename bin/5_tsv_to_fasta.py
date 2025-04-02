with open('/home/majiso/Desktop/LCG_Gen22/LCG_Sem2/Python/comprension_listas-archivos/data/dna_sequences.txt', 'r') as archivo:
    lineas = archivo.readlines()

# Listas vacías
identificadores = []
secuencias = []

# Iterar sobre las líneas
for linea in lineas:
    identificador, secuencia = linea.strip().split('\t')
    identificadores.append(identificador)
    secuencias.append(secuencia.upper().replace('-', '').replace('—', '')) # Convertir todo a mayúsculas y qutar guiones antes de añadir a la lista

# Reacomodar las secuencias y sus identificadores en el formato deseado
secuencias_fasta = [f'> {identificador}\n{secuencia}\n' for identificador, 
                    secuencia in zip(identificadores, secuencias)] # List comprehension con zip para iterar ambas listas

# Guardar las secuencias en un archivo FASTA
with open('/home/majiso/Desktop/LCG_Gen22/LCG_Sem2/Python/comprension_listas-archivos/results/dna_sequences.fa', 'w') as archivo:
    for linea in secuencias_fasta:
        archivo.write(f'{linea}')