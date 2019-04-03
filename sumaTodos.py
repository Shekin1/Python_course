def normal(x):
    return x

# normal = lambda x: x

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(0, limitTo+1):
        resultado += f(i)
    return resultado

if __name__ == "__main__":      #para que solo lo ejecute desde aquí
    print(sumaTodos(5, normal))
else:
    print(__name__)
        