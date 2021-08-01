import sys

def houthakker(supply:list, demand:list, matrix:list) -> int:
    oferta = supply.copy()
    demanda = demand.copy()
    suma = 0
    filasEliminadas = [] # [1]
    columnasEliminadas = []
    while sum(oferta) > 0 and sum(demanda) > 0:
        for filaIndex in range(len(matrix)):
            if filaIndex not in filasEliminadas: # 0
                fila = matrix[filaIndex]
                minCostIndex = -1
                minCost = float('inf')
                i = 0
                while i < len(fila):
                    if fila[i] < minCost and i not in columnasEliminadas:
                        minCost = fila[i]
                        minCostIndex = i # 1
                    i += 1
                ofertaPunto = oferta[minCostIndex] # 4000
                demandaPunto = demanda[filaIndex] # 5000
                sacar = min(ofertaPunto, demandaPunto)
                suma += sacar*matrix[filaIndex][minCostIndex]
                oferta[minCostIndex] -= sacar
                if oferta[minCostIndex] == 0:
                    columnasEliminadas.append(minCostIndex)
                demanda[filaIndex] -= sacar
                if demanda[filaIndex] == 0:
                    filasEliminadas.append(filaIndex)
    return suma


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

oferta = [6000, 4000, 2000, 1500]
demanda = [5000, 6000, 2500]
matriz = [[3, 2, 7, 6], [7, 5, 2, 3], [2, 5, 4, 5]]


print(houthakker(oferta, demanda, matriz))