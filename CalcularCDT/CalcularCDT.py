from wsgiref.validate import validator


def CDT(usuario: str, capital: int, tiempo: int):
    """CDT
    :Parámetros: usuario (str) : alfanumerico
    que identifica el usuario capital(int):
    MOnto a ingresar tiempo(int): tiempo del CDT
    :
    String: de ka forma "Las ganancias obtenidas para un monto de {}, en un tiempo de {} es {}" 
    para el caso de ganancias, para las "La cantidad de dinero a recibir, según rl monto inicial {}, para un tiempo de {} es:{}" """
    porcentaje_interes = 3/100
    valor_intereses = (capital * porcentaje_interes * tiempo) / 12
    porcentaje_perder = 2 / 100
    
    
    if(tiempo >= 3):
        valor_total = valor_intereses + capital
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"
    else:
        valor_a_perder = capital * porcentaje_perder
        valor_total = capital - valor_a_perder
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"

print(CDT("AB1012", 1000000, 3)) 
print(CDT("ER3366", 650000, 2)) 

