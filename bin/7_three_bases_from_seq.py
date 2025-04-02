cadenas = input('Ingrese una o más secuencias de DNA, separadas por "," (coma): ')
cadenas = cadenas.split(',') # Separar las cadenas por la coma

tres_bases_por_secuencia = [cadena[:3] for cadena in cadenas] # Comprehension list
print(f'Los tres primeros nucleótidos de cada secuencia son: {', '.join(tres_bases_por_secuencia)}') # Mostrar el resultado en una sola línea