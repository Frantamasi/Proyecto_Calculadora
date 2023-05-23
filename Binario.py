from os import system
import ValidarDatos as VD
import Operaciones_Decimal as Operaciones

def Binario_a_lista(binario):

    lista_binario1 = []

    for i in range(0, len(binario)):
        lista_binario1.append(binario[i])   #almacena cada posicion del string en una lista
        lista_binario1[i] = (binario[i])

    return lista_binario1

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
        lista_binario[i] = int(binario[i]) #los pasa a int para realizar la cuenta
   
    lista_binario = lista_binario[::-1]   #Invierte la lista
    
    for i in range(0, len(lista_binario)):
        suma = lista_binario[i] * (2**i)   #realiza la conversion
        resultado3 = suma + resultado3

    
    return resultado3

def Suma_binario(binario1, binario2): #recibe dos strings e invoca a la operacion suma_B
    lista_binario1 = []
    lista_binario2 = []
    resultado = []

    for i in range(0, len(binario1)):
        lista_binario1.append(binario1[i])   #almacena cada posicion del string en una lista
        lista_binario1[i] = (binario1[i])
    
    for i in range(0, len(binario2)):
        lista_binario2.append(binario2[i])   #almacena cada posicion del string en una lista
        lista_binario2[i] = (binario2[i])

    if(len(lista_binario1) == len(lista_binario2)):
        
        lista_binario1 = lista_binario1[::-1]   #invierte las listas para trabajarlo del ultimo bit al primero
        lista_binario2 = lista_binario2[::-1]
        
        resultado = Operaciones.Operacion_suma_B(lista_binario1, lista_binario2,False)
                
    elif(len(lista_binario1) > len(lista_binario2)):  #el primero es mayor
        
        lista_binario1 = lista_binario1[::-1]
        lista_binario2 = lista_binario2[::-1]
        
        diferencia_bits = len(lista_binario1) - len(lista_binario2)

        for i in range (0, diferencia_bits):
            lista_binario2.append("0")


        resultado= Operaciones.Operacion_suma_B(lista_binario1, lista_binario2,False)

    elif(len(lista_binario1) < len(lista_binario2)):  #si el primero es menor
        
        lista_binario1 = lista_binario1[::-1]
        lista_binario2 = lista_binario2[::-1]
        
        diferencia_bits = len(lista_binario2) - len(lista_binario1)

        for i in range (0, diferencia_bits):
            lista_binario1.append("0")

        resultado= Operaciones.Operacion_suma_B(lista_binario1, lista_binario2,False)
        
    return resultado    #agregarle que lo devuelva como string

def CA2(lista_binario):#recibe una lista
    for i in range(0,len(lista_binario)):
        if (lista_binario[i] == "1"):
            lista_binario[i] = "0"
        elif(lista_binario[i]== "0"):
            lista_binario[i] = "1"
    
    resultado = Suma_binario(lista_binario,"1")
    
    return resultado

def Resta_binario(binario1, binario2):  #recibe 2 strings
    lista_binario1=[]; lista_binario2 = [];resultado=[]
    es_negativo = False

    if(Conversion_Binario_a_Decimal(binario1) < Conversion_Binario_a_Decimal(binario2)): #compara si el numero es menor
        
        binario_temporal=binario1
        binario1 = binario2             
        binario2 = binario_temporal

        es_negativo = True

    for i in range(0, len(binario1)):
        lista_binario1.append(binario1[i])   #almacena cada posicion del string en una lista
        lista_binario1[i] = (binario1[i])
    for i in range(0, len(binario2)):
        lista_binario2.append(binario2[i])   #almacena cada posicion del string en una lista
        lista_binario2[i] = (binario2[i])


    if(len(lista_binario2) < len(lista_binario1)):                   #si tiene menor cantidad de bits, lo va a completar con 0
        diferencia_bits = len(lista_binario1) - len(lista_binario2)
        
        for i in range (0,diferencia_bits):
            lista_binario2.insert(i,"0")

        
    
    lista_binario2 = CA2(lista_binario2) #realiza el complemento a 2

    resultado = Operaciones.Operacion_suma_B(lista_binario1[::-1],lista_binario2[::-1],True)
    
    if(es_negativo == True):
        resultado.insert(0, "-")
    
    resultado = Lista_a_string(resultado)
    return resultado

def Ingresar_Binario(): #retorna un string
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

def Lista_a_string(lista_binario): #recibe una lista y retorna un string
    binario = ""
    for i in range(0,len(lista_binario)):
        binario = binario + lista_binario[i]
    return binario


