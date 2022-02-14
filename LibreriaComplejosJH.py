import math

def sumacomplejos(a,b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return(real,img)

def multiplicacioncomplejos(a,b):
    real = (a[0] * a[1] - b[0] * b[1])
    img = (a[0] * b[1] + a[1] * b[0])
    return(real,img)

def restacomplejos(a,b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    return(real,img)

def divisioncomplejos(a,b):
    real = ((a[0] * a[1]) + (b[0] * b[1])) / (a[1]**2 + b[1]**2)
    img = ((a[1] * b[0]) - (a[0] * b[1])) / (a[1]**2 + b[1]**2)
    return (real,img)

def modulocomplejos(a):
    return ((a[0] ** 2) + (a[1] ** 2)) ** 1/2


def conjugadocomplejos(a):
    return (a[0], -a[1])


def conversioncomplejos(a,P,alpha):

    p = math.sqrt((((a[0]) ** 2) + (a[1] ** 2)))
    alpha = math.atan((a[1] / a[0]))

    c = (P * math.cos(alpha))
    d = (P * math.sin(alpha))

    return f'Polares {p, alpha}', f'Cartesianas {c,d}'

def fasecomplejos(a):
    alpha = math.atan((a[1] / a[0]))
    return alpha


if __name__ == '__main__':

    print ("Suma",sumacomplejos((4 , 3 ),(6 , 33 )))
    print ("Producto" , multiplicacioncomplejos((-10 , 5 ), (2 , 7)))
    print ("Resta " , restacomplejos((-6 , -3), (2,19)))
    print ("Division" , divisioncomplejos((35,34),(3,2)))
    print ("Conjugado" , conjugadocomplejos ((7, 26)))
    print ("Conversion" , conversioncomplejos((18,-3), (math.sqrt(30)),(4)))
    print ("Modulo" , modulocomplejos((-29,8)))
    print ("Fase" , fasecomplejos((-21,3)))

