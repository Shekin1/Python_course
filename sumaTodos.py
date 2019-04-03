def normal(x):
    return x

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(0, limitTo+1):
        resultado += f(i)
    return resultado

print(sumaTodos(5, normal))