"""

   
def consultaRegistro(ventas,idProducto):
    newDic = {}#crear un nuevo diccionario
    respuesta=#crear una variable String vacía
    for i in range(len(ventas)) :
        if ventas[i][0][0] == #comparar si el producto existe con el idProducto:
            newDic[i] = #Asignar ventas al nuevo diccionario
          
    if len(newDic) == 0:
        respuesta = #Enviar la respuesta cuando no encuentra el producto
    
    for valoresDic in newDic.values(): 
        for idProducto,dProducto...#escribir cada variable como indica el reto# in #iterablevaloresDic:
            respuesta += (f'Devolver respuesta exactamente como aparece en el reto\n')      
    print(respuesta)

Descripción del problema:

Una venta de autopartes necesita de forma urgente un registro de partes vendidas a diferentes compradores,
motivo por el cual, se hace necesario en el futuro inmediato registrar dichas ventas y que las mismas puedan
ser consultadas por un tipo particular de producto, para ello, la información introducida debe ser la siguiente:

Entradas: Lista de tuplas

Nombre          Abreviación         Tipo        Descripción

IdProducto      N/A                 Int         Identificador único del producto
dProducto       N/A                 Char        Descripción del producto
pnProducto      N/A                 Char        Numero de parte del producto
cvProducto      N/A                 Int         Cantidad vendida del producto
sProducto       N/A                 Int         Stock del producto
nComprador      N/A                 Char        Nombre del comprador
cComprador      N/A                 Int         Documento de identidad del comprador
fVenta          N/A                 Char        Fecha de venta del producto
    
Salida: diccionario con lista de tuplas

Tipo de retorno         Descripción

Str {:}                 Cadena de caracteres de la forma
                        Producto consultado : {idProducto} Descripción {dProducto}
                        #Parte {pnProducto} Cantidad vendida {cvProducto} Stock
                        {sProducto} Comprador {nComprador} Documento
                        {cComprador} Fecha Venta {fVenta}
                        
                        Ó
                        “No hay registro de venta de ese producto”


Requerimiento. Para el desarrollo de esta implementación, el programador debe permitir introducir un
registro de ventas desde una lista de tuplas como parámetro de AutoPartes y convertirlo luego en un
diccionario con lista de tuplas.

Asimismo, se debe permitir desde la función consultaRegistro quien llama a un nuevo registro desde la
función AutoPartes, manejar la entrada de un parámetro tipo idProducto para ubicar información
específica acerca del producto en información general que incluye la fecha de venta.
    
"""

ventas = ([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')])
ventas1=([
 (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
 (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
 (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
 (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')])
ventas2=([
 (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
 (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
 (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
 (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')])

def AutoPartes(ventas:list):
    dict = {} 
    for i in range(len(ventas)):
        dict[i] = ventas[i]
    return dict
def consultaRegistro(ventas,idProducto):
    nuevoDict = {}
    respuesta= ""
    for i in ventas:
        if ventas[i][0][0] == idProducto:
            nuevoDict[i] = ventas[i]      
    if len(nuevoDict) == 0:
        respuesta = "No hay registro de venta de ese producto"
    else:
        for i in nuevoDict:
            respuesta += "Producto consultado : {} Descripción {} #Parte {} Cantidad vendida {} Stock {} Comprador {} Documento {} Fecha Venta {}\n".format(ventas[i][0][0],ventas[i][0][1],ventas[i][0][2],ventas[i][0][3],ventas[i][0][4],ventas[i][0][5],ventas[i][0][6],ventas[i][0][7])      
    return print(respuesta)
               
if __name__ == "__main__":
    ##print(AutoPartes1(ventas))
    
    """print(AutoPartes(ventas),"\n\n")
    
    print(AutoPartes(ventas1),"\n\n")
    print(AutoPartes(ventas2),"\n\n")"""
    consultaRegistro(AutoPartes(ventas),2010)
    ##consultaRegistro(AutoPartes(ventas1),2001)
    ##consultaRegistro(AutoPartes(ventas2),9852)