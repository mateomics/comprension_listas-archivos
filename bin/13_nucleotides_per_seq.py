secuencias = input('Ingrese una o más secuencias de DNA, separadas por "," (coma): ')
secuencias = secuencias.split(',') # Separar las secuencias por cada coma

# Contar la cantidad de cada uno de los nucleótidos por secuencia dada
NUCLEOTIDOS = 'ACGT' # mayúsculas porque es constante por su uso

for secuencia in secuencias:
    print(f'\nLa secuencia "{secuencia}" contiene:')
    for nucleotido in NUCLEOTIDOS:
        print(f'{secuencia.count(nucleotido)} nucleótidos "{nucleotido}"')
    