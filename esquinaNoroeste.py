import sys
import time

def north_west_corner(supply, demand):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    i = 0
    j = 0
    bfs = []
    while len(bfs) < len(supply) + len(demand) - 1:
        s = supply_copy[i]
        d = demand_copy[j]
        v = min(s, d)
        supply_copy[i] -= v
        demand_copy[j] -= v
        bfs.append(((i, j), v))
        if supply_copy[i] == 0 and i < len(supply) - 1:
            i += 1
        elif demand_copy[j] == 0 and j < len(demand) - 1:
            j += 1
    return bfs

try:
    archivo = open("transporte.txt", "r")
except:
    print("El archivo transporte.txt no existe.")
    sys.exit(0)

for linea in archivo:
    cosa, resto = linea.split(":")
    if cosa == "Demanda":
        demanda = list(map(int, resto.split(",")))
    elif cosa == "Oferta":
        oferta = list(map(int, resto.split(",")))
    elif cosa == "MatrizCosto":
        matriz = []
        rows = resto.split("|")
        for row in rows:
            matriz.append(list(map(int, row.split(","))))
    
archivo.close()

print("Esquina Noroeste.")

inicio = time.time()

resultado = north_west_corner(oferta, demanda)

costoTotal = 0

for t, cost in resultado:
    x, y = t
    costoTotal += matriz[y][x] * cost

print("El tiempo de calculo fue de:", time.time() - inicio, "segundos.")
print(costoTotal)