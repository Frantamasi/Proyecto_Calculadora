def Es_numero(dato_ingresado): #hacer que acepte numeros float
    resultado = False
    parteentera=dato_ingresado.find(".") #asigna la posicion donde se encuentra el punto en el string
    

    if(dato_ingresado.isdigit() == True):
        resultado = True
    
    elif(parteentera != -1): #si entra al estring, quiere decir que es un float
        
        cantidad_entera = (dato_ingresado[:parteentera]) #asigna una subcadena desde el inicio del string hasta donde esta el punto
        cantidad_decimal=(dato_ingresado[parteentera+1:]) #asigna una subcadena desde el punto del string hasta el final
        #numero_en_string = f"{cantidad_entera}"+"."+f"{cantidad_decimal}" #los concatena 
        
        otroPunto = cantidad_decimal.find(".") #vuelve a chequear que no haya otro punto
        if(otroPunto != -1): #si hay otro retorna falso
            resultado = False
        else:
            resultado = True
            
    elif(dato_ingresado.find("-") != -1): #identifica si es un numero negativo
        resultado = True
    
    return resultado

def OperacionDecimal(Operacion): #tiene que recibir como parametro los numeros para asi pasarlos a como parametro a la funcion especifica
    resultado = 0

    if(Operacion == 1):
        resultado = 1
        pass
    elif(Operacion == 2):
        pass
    elif(Operacion == 3):
        pass
    elif(Operacion == 4):
        pass
    elif(Operacion == 5):
        pass
    elif(Operacion == 6):
        pass
    else: 
        resultado = 0
    return resultado #retorna la operacion a realizar


def numero_entero(dato_ingresado): #hacer que acepte numeros float
    resultado = False
    
    if(dato_ingresado.isdigit() == True):
        resultado = True

    return resultado

def numero_flotante(dato):
    pass