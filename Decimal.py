from os import system
import ValidarDatos as VD
import Operaciones_Decimal as OD

def Operandos_En_Decimal():
    system("cls")
    numeros = []
    condicion = False
    while(condicion == False):

        CantDeOperandos = input("¿Con cuantos numeros vas a operar?") 

        if(VD.numero_entero(CantDeOperandos) == True):
            CantDeOperandos = int(CantDeOperandos) #con este dato define cuantas veces se itera el for
            contador = 0
            
            for i in range (0, CantDeOperandos):
                
                numeros.append(ingresar_numero())#completa la lista de numeros que tenes
                system("cls")

            
            print ("los numeros ingresados son: ")
            for i in range (0, CantDeOperandos):
                print(numeros[contador])
                contador += 1
            
            condicion = True
        else:
            input("el dato ingresado no corresponde a un numero entero ")
        input("")
        system("clear")
        
    return numeros #devuelve la lista de numeros
    #tiene que invocar al funcion Tipo_DE_operacion y pasarle como parametro los numeros que tiene que utilizar 



def ingresar_numero():
    condicion = False
    system("cls")
    while(condicion == False):
        
        a = (input("ingrese un numero: "))
        
        if(VD.Es_numero(a) == True):
            
            b=float(a) #convierte a A en float y se lo asigna a B
            condicion = True 
            
            if(b % 1 == 0): #si el numero da resto 0 significa que es un entero y lo transforma
                b=int(b)        
        else:
            input("el dato ingresado no corresponde a un numero ")
            system("cls")
        
       
    return b

def operacion(numeros, operacion):

    if(operacion == 1):
        OD.suma(numeros)