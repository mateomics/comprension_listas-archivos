# Este código verifica si una secuencia dada comienza con el codón de inicio 'ATG'/'AUG'
secuencia = input('Introduzca una secuencia de DNA o RNA para comprobar si comienza con un codón de inicio: ')

comienza = 'no'
if secuencia.startswith('ATG') or secuencia.startswith('AUG'):
    comienza = 'sí'

print(f'La secuencia {comienza} comienza con un codón de inicio')