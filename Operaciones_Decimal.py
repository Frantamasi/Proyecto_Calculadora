#decimal

def suma(numeros):  
    resultado = 0  #arreglar para que se pueda pasar mas de un numero como parametro
    for i in range(0, len(numeros)):
        resultado = resultado + numeros[i]
    print(f"{numeros[0]} + {numeros[1]} = {resultado}")    
    input("")
    return resultado

def resta(numeros):
    resultado = 0
    
    resultado = numeros[0] - numeros[1]
    print(f"{numeros[0]} - {numeros[1]} = {resultado}")    
    input("")
    return resultado

def multiplicacion(numeros):
    resultado = numeros[0] * numeros[1]
    print(f"{numeros[0]} x {numeros[1]} = {resultado}")    
    input("")
    return resultado

def division(numeros):
    resultado = numeros[0] / numeros[1]
    print(f"{numeros[0]} / {numeros[1]} = {resultado}")    
    input("")
    return resultado

def devisionEntera(numeros):
    resultado = numeros[0] / numeros[1]
    print(f"{numeros[0]} // {numeros[1]} = {resultado}")    
    input("")
    return resultado

def potencia(numeros):
    resultado = numeros[0] ** numeros[1]
    print(f"{numeros[0]} ** {numeros[1]} = {resultado}")    
    input("")
    return resultado


#binario

def Operacion_suma_B(lista_binario1, lista_binario2):
    
    resultado = []
    acarreo = False
    es_la_ultima = 0
    for i in range(0, len(lista_binario1)):
            
        es_la_ultima = es_la_ultima + 1

        if(lista_binario1[i] == "1" and lista_binario2[i] == "1"):

            resultado.append("0")
            acarreo = True

        elif(lista_binario1[i] == "0" and lista_binario2[i] == "1"):

            resultado.append("1")
            
        elif(lista_binario1[i] == "1" and lista_binario2[i] == "0"):

            resultado.append("1")
            
        elif(lista_binario1[i] == "0" and lista_binario2[i] == "0"):

            resultado.append("0")

        if(acarreo == True and es_la_ultima == len(lista_binario1)):
                
            resultado.append("1")

        elif(acarreo == True):

            if(lista_binario1[i+1] == "0"):
                lista_binario1[i+1] = "1"
                acarreo = False

            elif(lista_binario1[i+1] == "1"):
                lista_binario1[i+1] = "0"
                    #acarreo sigue siendo verdadero
    resultado = resultado[::-1]
    
    return resultado