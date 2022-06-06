"""
Descripción del problema:
Un contador necesita llevar una bitácora acerca de los registros diarios de una papelería, en consecuencia,
esta información que necesita automatizar es la siguientes:
Entrada:

Número de orden        Código del producto    Cantidad   Precio unitario
int de 4 a 6 dígitos   str de 4 a 6 dígitos   Int        Float

Salida:
Tipo de retorno     Descripción
Str                 Cadena de caracteres de la forma:
                    “La factura <número> tiene un total en pesos de <cantidad>”

Requerimiento. Para el desarrollo de esta implementación, el programador debe permitir introducir un
registro de ordenes desde una lista de tuplas y a través de la función “map”, “reduce” y “lambda”
desarrollar las funciones necesarias para el siguiente calculo:

• Sumar el total de cada tupla de cada lista
• Sumar los totales de todas las tuplas de toda la lista
• Suma el incremento si la compra no llega a un mínima de 600.000 pesos, en este caso, se incrementa 25.000 pesos al total de la compra.

Recuerde, que la salida no debe tener más de dos decimales.

"""

def ordenes(rutinaContable):
    from functools import reduce
    print('------------------------ Inicio Registro diario ---------------------------------')
    for i in range(len(rutinaContable)):
        preciosUnitarios = []
        cantidadProductos = []
        for j in range(len(rutinaContable[i])-1):
            preciosUnitarios.append(rutinaContable[i][j+1][2])
            cantidadProductos.append(rutinaContable[i][j+1][1])
        totalCostoProductos = map(lambda x, y : x * y, preciosUnitarios, cantidadProductos)
        total = reduce(lambda x, y : x + y, totalCostoProductos)
        if total < 600000:
            total = total + 25000
        mensaje = f"La factura {rutinaContable[i][0]} tiene un total en pesos de {total:,.2f}"
        print(mensaje)
    
    print('-------------------------- Fin Registro diario ----------------------------------')
    
lista = [
    
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
    
    ]
lista1 = [
    
    [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)]
    
]
if __name__ == "__main__":
    ordenes(lista)
    ordenes(lista1)