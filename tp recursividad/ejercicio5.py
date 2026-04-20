def r(n):
    v = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
    if len(n) == 0:
        return 0
    if len(n) == 1:
        return v[n]
    
    if v[n[0]] < v[n[1]]:
        # Si es menor, se resta
        return -v[n[0]] + r(n[1:])
    else:
        return v[n[0]] + r(n[1:])


n = input("Ingrese el número romano: ").upper()

print("El número es:", r(n))