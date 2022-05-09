"""
Reto 2:
En el parque de diversiones “AVENTURAS EXTREMAS” se requiere implementar una función en la
cual reciba como parámetro un diccionario, el cual va a tener las variables que a continuación se
muestran:

Nombre              Tipo        Descripción
id_cliente          int         Código único que identifica al cliente
nombre              str         Nombre del cliente
edad                int         Edad cliente
primer_ingreso      boolean      Primera vez que el cliente ingresa puede ser: True/False

En la siguiente tabla se muestra la atracción y el valor de la boleta para cada una de ellas, en la cual
los clientes podrán ingresar dependiendo de su edad, posteriormente el parque de atracciones ha
decidido otorgar un descuento al valor de la boleta si cumple con el rango de edad y es la primera
vez que el cliente ingresa.

Atracción   Valor de boleta     Edad            Primer  Ingreso Descuento
                                (años) 
X-Treme     20000               >18 años        True    5% del valor de la boleta
Carros
chocones    5000                >=15 y          True    7% del valor de la boleta
                                <=18 
Sillas
voladoras   10000               >=7 y < 15      True    5% del valor de la boleta

Esta función debe retornar un nuevo diccionario con las llaves nombre, edad, atracción,
primer_ingreso, total_boleta y apto del cliente:

• En donde apto tendrá como valor una variable booleana, será verdadera si su edad cumple con
los rangos exigidos en la tabla anterior, en el caso contrario será falsa.

• En el caso de atraccion y total_boleta, si no se cumple el rango de edades se le asignara un valor
de ‘N/A’ a cada uno.

• Si primer_ingreso es verdadero, el total_boleta será el valor de la boleta menos el descuento de
lo contrario se pagará el valor neto de la boleta. 

"""

informacion = {
"id_cliente" : 1,
"nombre" : "Johana Fernandez",
"edad" : 14,
"primer_ingreso" : True
                    
}

print(informacion["edad"])
def cliente(informacion:dict)-> dict:
    costo_total = 0
    informacion_ingreso = {}
    if( informacion["edad"] > 18 and informacion["primer_ingreso"] == True):
        costo_total = 20000 - (20000*0.05)
        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "Sillas voladoras"
        informacion_ingreso["primer_ingreso"] = True
        print(costo_total)
    elif(informacion["edad"] > 18 and informacion["primer_ingreso"] == False):
        costo_total = 20000 
        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "Sillas voladoras"
        informacion_ingreso["primer_ingreso"] = False
        print(costo_total)
    elif( informacion["edad"] >= 15 and informacion["edad"] <= 18):
        costo_total = 5000 - (5000*0.07)
        print(costo_total)
        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "Carros chocones"
        informacion_ingreso["primer_ingreso"] = "Sillas voladoras"
    elif (informacion["edad"] >= 7 and informacion["edad"] < 15):
        costo_total = 10000 - (10000*0.05)
        print(costo_total)
        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "Sillas voladoras"
        informacion_ingreso["primer_ingreso"] = "Sillas voladoras"
    return informacion_ingreso
    
if __name__ == '__main__':
    
    print(cliente(informacion))