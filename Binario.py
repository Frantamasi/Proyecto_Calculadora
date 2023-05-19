from os import system
import ValidarDatos as VD
def Conversion_Decimal_a_Binario(decimal): #recibe un int
    resultado = ""
    condicion = False
    resto = 0
    while(condicion == False):
        resto = decimal % 2
        decimal = decimal // 2
        resultado = resultado + str(resto)

        if(decimal == 1):
            resultado = resultado + str(decimal)
            condicion = True
        elif(decimal == 0):
            condicion = True

    return resultado[::-1] #devuelve el string invertido

def Conversion_Binario_a_Decimal(binario):    #recibe un string
    lista_binario = []
    resultado3 = 0
    for i in range(0, len(binario)):
        lista_binario.append(binario[i])   #almacena cada posicion del string en una lista
        lista_binario[i] = int(binario[i])
   
    lista_binario = lista_binario[::-1]   #Invierte la lista
    
    for i in range(0, len(lista_binario)):
        suma = lista_binario[i] * (2**i)   #realiza la conversion
        resultado3 = suma + resultado3

    print(f"{binario} es {resultado3} en decimal")
    input()
    return resultado3

def Suma_binario(binario1, binario2):
    lista_binario1 = []
    lista_binario2 = []
    resultado = []
    acarreo = False 
    es_la_ultima = 0

    for i in range(0, len(binario1)):
        lista_binario1.append(binario1[i])   #almacena cada posicion del string en una lista
        lista_binario1[i] = (binario1[i])
    for i in range(0, len(binario2)):
        lista_binario2.append(binario2[i])   
        lista_binario2[i] = (binario2[i])
    
    if(len(lista_binario1) >= len(lista_binario2)):
        
        lista_binario1 = lista_binario1[::-1]
        lista_binario2 = lista_binario2[::-1]
        
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
            
    print(f"el resultado es {resultado}")
    input()


Suma_binario("11", "11")

def Ingresar_Binario():
    condicion = False
    binario = ""
    while(condicion == False):
        system("cls")
        print("un numero en binario solo puede contener 0 y 1")
        binario = input("ingrese el numero binario: ")
        
        condicion = VD.numero_binario(binario)
        #if para validar que sea un binario
    
    print(binario)    
    input()
    return binario

