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

#print(Conversion_Decimal_a_Binario(58))
#print(Conversion_Binario_a_Decimal("111010"))
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

