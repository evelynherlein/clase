#Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
#obtener la siguiente información sin perder los datos:
#a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
#b. calcular el promedio de temperatura (o media) del total de valores;
#c. determinar la cantidad de valores por encima y por debajo de la media.
# Definición de funciones básicas de pila

def apilar(pila, x):
    pila.append(x)

def desapilar(pila):
    return pila.pop()

def pila_vacia(pila):
    return len(pila) == 0

pila = [10, 20, 30, 40, 50, 60]  
aux = []

# a) 
minimo = 9999
maximo = -9999
suma = 0
cant = 0

while not pila_vacia(pila):
    x = desapilar(pila)
    
    suma += x
    cant += 1
    
    if x < minimo:
        minimo = x
    if x > maximo:
        maximo = x
    
    apilar(aux, x)
# b)
promedio = suma / cant

while not pila_vacia(aux):
    apilar(pila, desapilar(aux))


# c)
arriba = 0
abajo = 0

while not pila_vacia(pila):
    x = desapilar(pila)
    
    if x > promedio:
        arriba += 1
    elif x < promedio:
        abajo += 1
    
    apilar(aux, x)

while not pila_vacia(aux):
    apilar(pila, desapilar(aux))

print("Minimo:", minimo)
print("Maximo:", maximo)
print("Rango:", maximo - minimo)
print("Promedio:", promedio)
print("Arriba de la media:", arriba)
print("Abajo de la media:", abajo)