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
 sumatoria = lambda x, y : x + y
 print(sumatoria)
 calculo_multi = lambda x, y : x * y
 print(calculo_multi)
 print('----------------- Inicio Registro diario --------------------------')
 for j in range(len(rutinaContable)):
    s_adicion = []
    valores = []
    for i in range[rutinaContable[j]-1]:
        s_adicion.append(rutinaContable[j][i+1][2])
        valores.append(rutinaContable[j][i+1][1])
    valores = map(calculo_multi, s_adicion, valores)
    total = reduce(sumatoria, valores)
    if total < 600000:
        total = total + 25000
    mensaje = f"La factura {rutinaContable[j][0]} tiene un total en pesos de {total:,.2f}"
    
    print(mensaje)
 
 print('----------------- Fin Registro diario -----------------------------')
if __name__ == "__main__":
    pass