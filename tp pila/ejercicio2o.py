#Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
#cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
#norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
#que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
#partida, retornando por el mismo camino que fue.

def apilar(pila, x):
    pila.append(x)

def desapilar(pila):
    return pila.pop()

def pila_vacia(pila):
    return len(pila) == 0

def opuesta(dir):
    if dir == "norte":
        return "sur"
    elif dir == "sur":
        return "norte"
    elif dir == "este":
        return "oeste"
    elif dir == "oeste":
        return "este"
    elif dir == "noreste":
        return "suroeste"
    elif dir == "noroeste":
        return "sureste"
    elif dir == "sureste":
        return "noroeste"
    elif dir == "suroeste":
        return "noreste"

pila = []

apilar(pila, (5, "norte"))
apilar(pila, (3, "este"))
apilar(pila, (2, "sureste"))
apilar(pila, (4, "sur"))

print("Movimientos realizados:")
print(pila)

print("\nCamino de regreso:")

while not pila_vacia(pila):
    pasos, direccion = desapilar(pila)
    
    dir_opuesta = opuesta(direccion)
    
    print("Mover", pasos, "pasos hacia", dir_opuesta)