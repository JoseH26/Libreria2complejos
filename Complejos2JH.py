import LibreriaComplejosJH as lc


def adVectorComplejo(a,b):
    n = len(a)
    d = []
    for i in range(n):
        d += [lc.sumacomplejos(a[i],b[i])]
    return d

def inversoVector(a):
    n = len(a)
    b = []
    for i in range(n):
        b += [lc.multiplicacioncomplejos((-1, 0), a[i])]
    return b

def MultiplicacionEscalarVector(a,b):
    n = len(b)
    c = []
    for i in range(n):
        c += [lc.multiplicacioncomplejos(a, b[i])]
    return c

def AdMatricesComplejas(a,b):
    c = len(b)
    d = len(a[0])
    fila = []
    e = c * [fila]
    for i in range(c):
        fila = []
        e[i] = fila
        for j in range(d):
            e += [lc.cplxsum(a[i][j], b[i][j])]
    return e

def invAditivaMatriz(a):
    b = len(a)
    c = len(a[0])
    d = b * [c]
    for i in range(b):
        fila = []
        d[i] = fila
        for j in range(n):
            d[j] += [lc.multiplicacioncomplejos((-1,0), a[i][j])]
    return d

def MultiplicacionEscalarMatriz(a, b):
    m = len(b)
    n = len(b[0])
    d = [n] * m
    for i in range(n):
        fila = []
        d[i] = fila
        for j in range(m):
            d[j] += [lc.multiplicacioncomplejos(a, b[i][j])]
    return d

def TranspuestaMatriz(a):
    m = len(a)
    n = len(a[0])
    x = [n] * m
    for i in range(n):
        fila = []
        x[i] = fila
        for j in range(m):
            x[j] += [a[j][i]]
    return x

def ConjugadaMatriz(a):
    m = len(a)
    n = len(a[0])
    p = [n] * m
    for i in range(n):
        fila = []
        p[i] = fila
        for j in range(m):
            p[i] += [lc.conjugadocomplejos((-1,0), a[i][j])]
    return p

def AdjuntaMatriz(a):
    n = len(a)
    m = len(a[0])
    d = [n] * m
    for i in range(n):
        fila = [] * n
        d[i] = fila
        for j in range(m):
            d[i] += [lc.conjugadocomplejos((-1,0), a[j][i])]
    return d

def ProductoMatrices(a,b):
    m = len(a)
    n = len(a[0])
    fila = [(0, 0)] * n
    f = [fila] * m
    for i in range(m):
        fila = [(0, 0)] * n
        f[i] = fila
        for j in range(n):
            r[i][j] = lc.multiplicacioncomplejos(a[i][j], b[i][j])
    return f

def AccionMatrizVector(a,b):
    m = len(a)
    n = len(a[0])
    fila = [(0, 0)] * n
    d = [fila] * m
    for i in range(m):
        fila = [(0, 0)] * n
        d[i] = fila
        for j in range(n):
            r[i][j] = lc.multiplicacioncomplejos(a[i][j],b[i][j])
    return d

def ProductoInternoVectores(a):
    m = int(lc.modulocomplejos(a) ** 2)
    return m

def NormaVector(a):
    r = int(lc.modulocomplejos(a))
    return r

def distanciaVectores(a,b):
    g = 0
    s = 0
    for i in range(len(a)):
        g = a[i]-v[i]
        g = g**2
        s += g
    n = s ** (1/2)
    return n

def MatrizUnitaria(a):
    b = []
    for i in range(len(a)):
        fila = []
        for j in range(len(a[0])):
            fila = fila + [lc.conjugadocomplejos(a[i][j])]
        b = b + [fila]
    m = [[0 for i in range(n)]for i in range(h)]
    for i in range(n):
        for j in range(h):
            m[j][i] = b[i][j]
    unitaria = []
    for i in range(n):
        fila = []
        for j in range(h):
            suma = (0,0)
            for k in range(n):
                suma = lc.sumacomplejos(suma,lc.multiplicacioncomplejos(a[i][j], b[j][k]))
            n += [suma]
        unitaria += [n]
    return "La matriz es unitaria"

def MatrizHermitiana(a):
    if AdjuntaMatriz(a) == v:
        return True

def ProductoTensor(a,b):
    c = len(a)
    d = len(b)
    t = d * c
    w = [(0, 0)] * t
    cont = 0
    for i in range(c):
        for j in range(d):
            w[cont] = MultiplicacionEscalarVector(a[i],b[j])
            cont = cont + 1
    return w

if __name__ == '__main__':

    print(adVectorComplejo(a,b))
    print(inversoVector(a))
    print(MultiplicacionEscalarVector(a,b))
    print(AdMatricesComplejas(a,b))
    print(invAditivaMatriz(a))
    print(MultiplicacionEscalarMatriz(a, b))
    print(TranspuestaMatriz(a))
    print(ConjugadaMatriz(a))
    print(AdjuntaMatriz(a))
    print(ProductoMatrices(a,b))
    print(AccionMatrizVector(a,b))
    print(ProductoInternoVectores(a))
    print(NormaVector(a))
    print(distanciaVectores(a,b))
    print(MatrizUnitaria(a))
    print(MatrizHermitiana(a))
    print(ProductoTensor(a,b))
