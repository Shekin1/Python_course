from functools import reduce

def doble(x):
    return x+x

lista = [1, 3, -1, 15, 9, 2]

# Map aplica una transformación a cada elemento de lista
listaDobles = map(lambda x: x*2, lista)
# La función doble aplica a cada elemento de lista
listaDobles1 = map(doble,lista)

def esPar(x):
    return x % 2 == 0

listaPares = filter(lambda x: x% 2 == 0, lista)
# La función es par tiene que devolver un booleano para cada elemento de lista
listaPares1 = filter(esPar, lista)

# Reduce se aplica sobre todos los elementos de lista y devuelve un único valor
# La x es simempre el acumulado y la y es el siguiente elemento de la lista
sumatorio = reduce(lambda x,y: x+y, lista)

suma100 = reduce(lambda x,y: x+y, range(101))
sumatorioDobles = reduce(lambda x,y: x+y*2, lista)