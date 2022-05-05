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

if __name__ == "__main__":

  while(True):

        try:
            opcion = int(input("""Hola este es un aplicativo que te permite calcular la cantidad de intereses ganados 
            Informacion adicional:
            Si el usuario decide retirar su dinero en menos de dos meses se le aplica una penalidad del 2%

            1) Calcular usuarios con ganancia mayores a 3 meses
            2) calcular usuarios con ganancias menores a 2 meses
            3) listar usuarios con ganancia mayores a 3 meses
            4) listar usuarios con ganancias menores a 2 meses
            5) listar todos los usuarios
            6) Salir del programa
            
            Digite una opcion numerica: """))
            if opcion == 1:
                print(CDT("AB1012", 1000000, 3))
            elif opcion == 2:
                print(CDT("ER3366", 650000, 2)) 
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                break
            else:
                print("digite una opcion valida del menu \n\n")
        except ValueError:
            print("Por favor digite una opcion numerica \n\n")

