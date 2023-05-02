from os import system
import Decimal  
import ValidarDatos as VD

def MenuPrincipal():
    condicion = False
    numeros = []
    operacion = 0
    while(condicion == False):
        print("             CALCULADORA")
        print("")
        print("¿Con que tipo de base desea trabajar?")
        print("")
        print("1.   Decimal")
        print("2.   Binario")
        print("3.   Octal")
        print("4.   Hexadecimal")
        print("")
        base = (input("Ingrese el numero de base que desea utilizar: "))
        
        if(VD.numero_entero(base) == True): #hacer que lo invoque calculadora
            base=int(base)
            if(base == 1):
                numeros=Decimal.Operandos_En_Decimal() #retorna los numeros que se utilizan
                operacion = Menu_Tipo_De_Operacion_Decimal() #retorna la operacion a realizar           
                Decimal.operacion(numeros, operacion)
                system("cls")
                sigue = realizar_otra() #pregunta si va a seguir ejecutando
                if(sigue == False):
                    condicion = True
                
            elif(base == 2):
                pass
            elif(base == 3):
                pass
            elif(base == 4):
                pass
            else:
                input("El numero ingresado no es valido ")
                system("cls")
        else:
            input("Eso no es un numero, ingrese un numero para continuar ")
            system("cls")

def Menu_Tipo_De_Operacion_Decimal():
    system("cls")
    condicion = False
    validarDato=0
    while(condicion == False):

        print("¿Que tipo de operacion desea realizar?")
        print("")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Potencia")
        print("5. Division")
        print("6. Division entera")
        print("")

        tipo_operacion = input("Ingrese el numero deseado: ")

        if(VD.Es_numero(tipo_operacion) == True):
            tipo_operacion = int(tipo_operacion)
            validarDato = VD.OperacionDecimal(tipo_operacion)

        if(validarDato != 0):
            condicion = True
    return tipo_operacion

def realizar_otra():
    condision = False
    while(condision == False):
        print("¿Desea realizar otra operacion?")
        print("S = si | N = no")
        decision = input("")
    
        if(decision== "s" or decision == "S"):
            resultado = True
            condision = True
        elif(decision== "n" or decision == "N"):
            resultado = False
            condision = True
        else:
            input("La letra ingresada no corresponde a un valor esperado...")
            system("cls")
    
    return resultado