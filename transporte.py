#puntos de oferta
#puntos de demanda
#matriz de costos

#oferta = demanda

from random import randint

def puntos(cantidadPuntos: int, suma: int) -> list:
    lista = [0] * cantidadPuntos
    while suma > 0:
        for i in range(cantidadPuntos):
            if suma > 10:
                b = randint(1, 10)
                lista[i] += b
                suma -= b
            else:
                b = randint(1, suma)
                lista[i] += b
                suma -= b
            if suma == 0:
                break
    return lista

small = 10
medium = 100
large = 1000

tipo = "aslñdjk"
while tipo not in ("s", "m", "l"):
    tipo = input("¿Cual es el tamaño del problema? (s/m/l)")
    if len(tipo) > 0:
        tipo = tipo.lower()

if tipo == "s":
    cantidadPuntosOferta = randint(10, 99)
    cantidadPuntosDemanda = randint(10, 99)
    matrix = [[randint(1, 9) for x in range(cantidadPuntosDemanda)] for y in range(cantidadPuntosOferta)]
    print("Puntos de oferta: ", cantidadPuntosOferta)
    print("Puntos de demanda: ", cantidadPuntosDemanda)
    demanda = max(cantidadPuntosOferta, cantidadPuntosDemanda) * 1000
    oferta = demanda
    puntosDemanda = puntos(cantidadPuntosDemanda, demanda)
    puntosOferta = puntos(cantidadPuntosOferta, oferta)
    print("Demanda: ", puntosDemanda)
    print("Oferta: ", puntosOferta)

elif tipo == "m":
    cantidadPuntosOferta = randint(100, 999)
    cantidadPuntosDemanda = randint(100, 999)
    matrix = [[randint(1, 9) for x in range(cantidadPuntosDemanda)] for y in range(cantidadPuntosOferta)]
    print("Puntos de oferta: ", cantidadPuntosOferta)
    print("Puntos de demanda: ", cantidadPuntosDemanda)
    demanda = max(cantidadPuntosOferta, cantidadPuntosDemanda) * 1000
    oferta = demanda
    puntosDemanda = puntos(cantidadPuntosDemanda, demanda)
    puntosOferta = puntos(cantidadPuntosOferta, oferta)
    print("Demanda: ", puntosDemanda)
    print("Oferta: ", puntosOferta)

elif tipo == "g":
    cantidadPuntosOferta = randint(1000, 9999)
    cantidadPuntosDemanda = randint(1000, 9999)
    matrix = [[randint(1, 9) for x in range(cantidadPuntosDemanda)] for y in range(cantidadPuntosOferta)]
    print("Puntos de oferta: ", cantidadPuntosOferta)
    print("Puntos de demanda: ", cantidadPuntosDemanda)
    demanda = max(cantidadPuntosOferta, cantidadPuntosDemanda) * 1000
    oferta = demanda
    puntosDemanda = puntos(cantidadPuntosDemanda, demanda)
    puntosOferta = puntos(cantidadPuntosOferta, oferta)
    print("Demanda: ", puntosDemanda)
    print("Oferta: ", puntosOferta)


