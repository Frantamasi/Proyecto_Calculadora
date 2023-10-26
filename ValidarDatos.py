def Es_numero(dato_ingresado): 
    resultado = False
    parteentera=dato_ingresado.find(".") #asigna la posicion donde se encuentra el punto en el string
    

    if(dato_ingresado.isdigit() == True):
        resultado = True
    
    elif(parteentera != -1): #si entra al estring, quiere decir que es un float
        
        resultado = numero_flotante(dato_ingresado, parteentera)
            
    elif(dato_ingresado.find("-") == 0): #identifica si es un numero negativo
        
        if(dato_ingresado[1:].find("-") != -1): #busca si hay otro "-"
            resultado = False
        else:
            resultado = True
    
    return resultado

def OperacionDecimal(Operacion): #tiene que recibir como parametro los numeros para asi pasarlos a como parametro a la funcion especifica
    resultado = 0

    if(Operacion == 1):
        resultado = 1
    elif(Operacion == 2):
        resultado = 2
    elif(Operacion == 3):
        resultado = 3
    elif(Operacion == 4):
        resultado = 4
    elif(Operacion == 5):
        resultado = 5
    elif(Operacion == 6):
        resultado = 6
    else: 
        resultado = 0
    return resultado #retorna la operacion a realizar


def numero_entero(dato_ingresado): 
    resultado = False
    
    if(dato_ingresado.isdigit() == True):
        resultado = True

    return resultado

def numero_flotante(dato_ingresado, parteentera):
    
    cantidad_entera = (dato_ingresado[:parteentera]) #asigna una subcadena desde el inicio del string hasta donde esta el punto
    cantidad_decimal=(dato_ingresado[parteentera+1:]) #asigna una subcadena desde el punto del string hasta el final
        #numero_en_string = f"{cantidad_entera}"+"."+f"{cantidad_decimal}" #los concatena 
        
    otroPunto = cantidad_decimal.find(".") #vuelve a chequear que no haya otro punto
    
    if(otroPunto != -1): #si hay otro retorna falso
         resultado = False
    else:
        resultado = True
    
    return resultado

def numero_binario(dato):
    error = 0 
    lista_binario = []
    
    for i in range(0, len(dato)):
        lista_binario.append(dato[i])   #almacena cada posicion del string en una lista
        lista_binario[i] = (dato[i])
    
    for i in range (0, len(lista_binario)):

        if(lista_binario[i] == "1" or lista_binario[i] == "0"): #chequear esto
            pass
        else: 
            error = error + 1
    
    if(error != 0):
        es_binario = False
        input(f"tu numero tiene {error} errores")
    else:
        es_binario = True
        
    
    return es_binario


def numero_Octal(dato):
    error = 0 
    lista_octal = []
    lista_num_octal = ["0","1","2","3","4","5","6","7"]
    for i in range(0, len(dato)):
        lista_octal.append(dato[i])   #almacena cada posicion del string en una lista
        lista_octal[i] = (dato[i])
    
    for i in range (0, len(lista_octal)):
        if(lista_octal[i] in lista_num_octal):
            int(lista_octal[i])
        else:
            error = 1
    if(error != 0):
        es_octal = False
        input(f"tu numero tiene {error} errores")
    else:
        es_octal = True
        
    
    return es_octal