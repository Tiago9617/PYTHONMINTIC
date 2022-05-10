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

Atracción   Valor de boleta     Edad            Primer  Ingreso     Descuento
                                (años) 
X-Treme     20000               >18 años        True                5% del valor de la boleta
Carros
chocones    5000                >=15 y          True                7% del valor de la boleta
                                <=18 
Sillas
voladoras   10000               >=7 y < 15      True                5% del valor de la boleta

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
"edad" : 20,
"primer_ingreso" : True

}
informacion1 = {

"id_cliente" : 1,
"nombre" : "Johana Fernandez",
"edad" : 20,
"primer_ingreso" : False

}

informacion2 = {
    
"id_cliente" : 2,
"nombre" : "Gloria Suarez",
"edad" : 6,
"primer_ingreso" : True

}

informacion3 = {

"id_cliente" : 3,
"nombre" : "Tatiana Suarez",
"edad" : 17,
"primer_ingreso" : True

}

informacion4 = {

"id_cliente" : 3,
"nombre" : "Tatiana Suarez",
"edad" : 17,
"primer_ingreso" : False

}

informacion5 = {
    
"id_cliente" : 4,
"nombre" : "Tatiana Suarez",
"edad" : 8,
"primer_ingreso" : True

}

informacion6 = {

"id_cliente" : 4,
"nombre" : "Tatiana Suarez",
"edad" : 8,
"primer_ingreso" : False
                    
}


def cliente(informacion:dict):
    informacion_ingreso = {}
    
    if( informacion["edad"] > 18 and informacion["primer_ingreso"] == True):

        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "X-Treme"
        informacion_ingreso["apto"] = True
        informacion_ingreso["primer_ingreso"] = informacion["primer_ingreso"]
        informacion_ingreso["total_boleta"] = 20000 - (20000*0.05)
        
        
    elif(informacion["edad"] > 18 and informacion["primer_ingreso"] == False):
 
        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "X-Treme"
        informacion_ingreso["apto"] = True
        informacion_ingreso["primer_ingreso"] = informacion["primer_ingreso"]
        informacion_ingreso["total_boleta"] = 20000
        
        
    elif( informacion["edad"] >= 15 and informacion["edad"] <= 18 and informacion["primer_ingreso"] == True) :

        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "Carros chocones"
        informacion_ingreso["apto"] = True
        informacion_ingreso["primer_ingreso"] = informacion["primer_ingreso"]
        informacion_ingreso["total_boleta"] = 5000 - (5000*0.07)
        
    elif( informacion["edad"] >= 15 and informacion["edad"] <= 18 and informacion["primer_ingreso"] == False) :

        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "Carros chocones"
        informacion_ingreso["apto"] = True
        informacion_ingreso["primer_ingreso"] = informacion["primer_ingreso"]
        informacion_ingreso["total_boleta"] = 5000
    
    elif (informacion["edad"] >= 7 and informacion["edad"] < 15 and informacion["primer_ingreso"] == True):

        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "Sillas voladoras"
        informacion_ingreso["apto"] = True
        informacion_ingreso["primer_ingreso"] = informacion["primer_ingreso"]
        informacion_ingreso["total_boleta"] = 10000 - (10000*0.05)
    
    elif (informacion["edad"] >= 7 and informacion["edad"] < 15 and informacion["primer_ingreso"] == False):

        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "Sillas voladoras"
        informacion_ingreso["apto"] = True
        informacion_ingreso["primer_ingreso"] = informacion["primer_ingreso"]
        informacion_ingreso["total_boleta"] = 10000
        
    elif (informacion["edad"] < 7):
        informacion_ingreso["nombre"] = informacion["nombre"]
        informacion_ingreso["edad"] = informacion["edad"]
        informacion_ingreso["atraccion"] = "N/A"
        informacion_ingreso["apto"] = False
        informacion_ingreso["primer_ingreso"] = informacion["primer_ingreso"]
        informacion_ingreso["total_boleta"] = "N/A"
    
    
    return informacion_ingreso
    
if __name__ == '__main__':
    
    print(str(cliente(informacion)) + "\n\n")
    print(str(cliente(informacion1)) + "\n\n")
    print(str(cliente(informacion2)) + "\n\n")
    print(str(cliente(informacion3)) + "\n\n")
    print(str(cliente(informacion4)) + "\n\n")
    print(str(cliente(informacion5)) + "\n\n")
    print(str(cliente(informacion6)) + "\n\n")