from os import system
import ValidarDatos as VD
import Operaciones_Decimal as OD



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
    resultado=0
    
    if(operacion == 1):
        resultado = OD.suma(numeros)
    elif(operacion == 2):
        resultado = OD.resta(numeros)
    elif(operacion == 3):
        resultado = OD.multiplicacion(numeros)
    elif(operacion == 4):
        resultado = OD.potencia(numeros)    
    elif(operacion == 5):
        resultado = OD.division(numeros)
    elif(operacion == 6):
        resultado = OD.devisionEntera(numeros)
   
    return resultado