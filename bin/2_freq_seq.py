# Necesitamos contar a frecuencia de cada nucleótido de una secuencia dada, por lo que usaremos la función 'count()'
secuencia = input('Hola. Introduzca una secuencia de nucleótidos:') # Sólo cuenta la frecuencia de las bases A, T, C, G
print(f'Su secuencia es: {secuencia}\n')

bases = 'ATCG'
for base in bases:
    print(f'La base {base} aparece {secuencia.count(base)} veces en la secuencia')