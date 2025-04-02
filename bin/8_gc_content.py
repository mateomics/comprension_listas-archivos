secuencia = input('Ingrese una secuencia de DNA: ')
# Uso de comprehension y de 'in' en lugar de '.count()', según lo estipulado en las instrucciones
contenido_gc = sum([1 for base in secuencia if base.upper() in 'GC']) / len(secuencia) * 100 # Cantidad de G y C entre el total de bases por cien, para porcentaje

print(f'El contenido de GC en la secuencia es de {contenido_gc}%')