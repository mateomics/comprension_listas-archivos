secuencias = input('Ingrese una o más secuencias de DNA, separadas por "," (coma): ')
secuencias = secuencias.split(',') # Separar las secuencias por cada coma

secuencias_invertidas = [secuencia[::-1] for secuencia in secuencias] # Invertir cada secuencia usando slicing
print(f'Secuencias invertidas:\n{'\n'.join(secuencias_invertidas)}') # Mostrar el resultado