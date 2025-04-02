secuencias = input('Ingrese una o más secuencias de DNA, separadas por "," (coma): ')
secuencias = secuencias.split(',') # Separar las secuencias por cada coma

# Filtrar secuencias que contengan alguno de los codones de paro
secuencias_stop_codon = [secuencia for secuencia in secuencias if 'TAA' in secuencia or 'TAG' in secuencia or 'TGA' in secuencia]

print(f'Secuencias que contienen codones de paro:\n{"\n".join(secuencias_stop_codon)}') # Mostrar el resultado