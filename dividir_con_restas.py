def dividir_con_resta(N,D,i):
    if N ==0:
        return 0
    while N>= D :
        N = N-D
        i += 1
    return i
def Resisduo(N,D,i):
    if N ==0:
        return 0
    while N>= D :
        N = N-D
        i += 1
    return N

i = 0
N = int(input("Ingrese el dividendo : \n"))
D = int(input("Ingrese el divisor: \n"))
Div = dividir_con_resta(N,D,i)
R = Resisduo(N,D,i)
print(f"El cociente es {Div} \nEl residuo es {R} ") 