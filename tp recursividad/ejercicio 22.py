def usar_fuerza(m, i=0):
    if i >= len(m):
        return False, i
    
    if m[i] == "sable de luz":
        return True, i + 1
    
    return usar_fuerza(m, i + 1)


m = ["comida", "armamento", "espada", "sable de luz"]

e, c = usar_fuerza(m)

if e:
    print("Encontró el sable de luz")
    print("Objetos revisados:", c)
else:
    print("No encontró el sable")
