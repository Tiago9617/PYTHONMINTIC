"""

def AutoPartes(ventas:list):
    dic = {} #crear el diccionario vacío
    for i in range(len(ventas)):
        dic[i] = #asignar ventas al diccionario
    return #diccionario
   
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
def AutoPartes(ventas: list):
    dict = {
        "idProducto": (ventas[0][0], ventas[1][0], ventas[2][0], ventas[3][0], ventas[4][0]),
        "dProducto":  (ventas[0][1], ventas[1][1], ventas[2][1], ventas[3][1], ventas[4][1]),
        "pnProducto": (ventas[0][2], ventas[1][2], ventas[2][2], ventas[3][2], ventas[4][2]),
        "cvProducto": (ventas[0][3], ventas[1][3], ventas[2][3], ventas[3][3], ventas[4][3]),
        "sproducto":  (ventas[0][4], ventas[1][4], ventas[2][4], ventas[3][4], ventas[4][4]),
        "nComprador": (ventas[0][5], ventas[1][5], ventas[2][5], ventas[3][5], ventas[4][5]),
        "cComprador": (ventas[0][6], ventas[1][6], ventas[2][6], ventas[3][6], ventas[4][6]),
        "fventa":     (ventas[0][7], ventas[1][7], ventas[2][7], ventas[3][7], ventas[4][7]),
    
    }
    return dict
    
def consultaRegistro(ventas: dict, idProducto):
    mensaje = ""
    bandera = False
    for clave, valor in ventas.items():
        for numero in range(0, 5):

            if valor[0][numero] == idProducto: 
                mensaje = mensaje + f"Producto consultado : {idProducto} Descripción bujía #Parte MS9512 Cantidad vendida 4 Stock 15 Comprador Carlos Rondon Documento 1256 Fecha Venta 12/06/2020"
                break
        if(bandera == True):
            bandera = False
            break
            
         
if __name__ == "__main__":
    while(True):
        consultaRegistro(AutoPartes(ventas), 2010)