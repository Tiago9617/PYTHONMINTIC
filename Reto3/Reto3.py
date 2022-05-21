"""
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
def AutoPartes(ventas: list):
    pass
def consultaRegistro(ventas, idProducto):
    pass    
if __name__ == "__main__":
    pass