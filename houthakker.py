import sys

def houthakker(supply:list, demand:list, matrix:list) -> int:
    oferta = supply.copy()
    demanda = demand.copy()
    suma = 0
    filasEliminadas = []
    columnasEliminadas = []
    while sum(oferta) > 0 or sum(demanda) > 0:
        for filaIndex in range(len(matrix)):
            if filaIndex not in filasEliminadas:
                fila = matrix[filaIndex]
                minCostIndex = -1
                minCost = -1
                i = 0
                while i < len(fila):
                    if fila[i] > minCost and i not in columnasEliminadas:
                        minCost = fila[i]
                        minCostIndex = i
                    i += 1
                ofertaPunto = oferta[minCostIndex]
                demandaPunto = demanda[filaIndex]
                sacar = min(ofertaPunto, demandaPunto)
                suma += sacar*matrix[filaIndex][minCostIndex]
                oferta[minCostIndex] -= sacar
                demanda[filaIndex] -= sacar
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

print(houthakker(oferta, demanda, matriz))


#[
# [., ., -]
# []
# []
# []
# ]


[1][2]