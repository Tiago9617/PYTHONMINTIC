informacion = {
"id_cliente" : 1,
"nombre" : "Johana Fernandez",
"edad" : 17,
"primer_ingreso" : True
                    
}

print(informacion["edad"])
def cliente(informacion:dict)-> dict:
    costo_total = 0
    if( informacion["edad"] > 18 ):
        costo_total = 20000 - (20000*0.05)
        print(costo_total)
    elif( informacion["edad"] >= 15 and 18<= informacion["edad"]):
        costo_total = 5000 - (5000*0.07)
        print(costo_total)
    elif (informacion["edad"] >= 7 and 15< informacion["edad"]):
        costo_total = 10000 - (10000*0.05)
        print(costo_total)
    return informacion
    
if __name__ == '__main__':
    
    print(cliente(informacion))