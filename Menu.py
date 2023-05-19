from os import system
import Decimal  
import ValidarDatos as VD
import Binario as B
import Operaciones_Decimal as OD 

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

def nuevoMenu():
    Utiliza = False
    condicion = False
    numeros = [0,0]
    resultado = 0
    operando = 0
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
        print("5.   Salir")
        print("")
        base = (input("Ingrese el numero de base que desea utilizar: "))
        
        if(VD.numero_entero(base) == True): #hacer que lo invoque calculadora
            base=int(base)
            if(base == 1):
                while(condicion==False):#invoca al menu decimal y pasa operando de parametro

                    if(resultado == 0 and Utiliza == False):
               
                        resultado = Menu_Decimal(operando,resultado)
                     #system("cls")
                        sigue = realizar_otra() #pregunta si va a seguir ejecutando
                    
                    if(sigue == True):
                        Utiliza = Utilizar_resultado()
                        if(Utiliza == True):
                            operando = posicion_operando()#pregunta en que posicion lo quiere utilizar
                            resultado = Menu_Decimal(operando,resultado)#vuelve a invocar
                            sigue = realizar_otra()  
                            
                            if(sigue == False):
                                condicion = True 
                        else:
                            nuevoMenu()
                    elif(sigue == False):
                        condicion = True
                
            elif(base == 2):
                Menu_Binario()
            elif(base == 3):
                pass
            elif(base == 4):
                pass
            elif(base == 5):
                condicion = True
            else:
                input("El numero ingresado no es valido ")
                system("cls")
        else:
            input("Eso no es un numero, ingrese un numero para continuar ")
            system("cls")

def Menu_Decimal(operando, resultado):
    numeros=[0,0]
    if(operando == 0):
        numeros[0]=Decimal.ingresar_numero() #retorna los numeros que se utilizan
        operacion = Menu_Tipo_De_Operacion_Decimal() #retorna la operacion a realizar           
        numeros[1]=Decimal.ingresar_numero()
    
    elif(operando == 1):
        numeros[0] = resultado
        operacion = Menu_Tipo_De_Operacion_Decimal() #retorna la operacion a realizar           
        numeros[1]=Decimal.ingresar_numero()
    
    elif(operando == 2):
        numeros[0]=Decimal.ingresar_numero() #retorna los numeros que se utilizan
        operacion = Menu_Tipo_De_Operacion_Decimal() #retorna la operacion a realizar
        numeros[1] = resultado
    
    resultado = Decimal.operacion(numeros, operacion)

    return resultado
            
def Utilizar_resultado():
    condision = False
    while(condision == False):
        print("¿Desea utilizar el resultado para otra operacion?")
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

def posicion_operando():
    condision = False
    while(condision == False):
        print("¿Que operando quiere que sea?")
        print("1 = primer posicion | 2 = segunda posicion ")
        decision = input("")
        
        if(VD.numero_entero(decision) == True):
            decision = int(decision)
            if(decision == 1):
                resultado = 1
                condision = True
            elif(decision  == 2):
                resultado = 2
                condision = True
        else:
            input("el numero ingresada no corresponde a un valor esperado...")
            system("cls")
    
    return resultado

def Menu_Binario():
    
    condicion = True
    
    while(condicion == True):
        system("cls")
        print("             BINARIO")
        print("")
        print("¿Con que tipo de operacion desea realizar?")
        print("")
        print("1.   Conversion")
        print("2.   Suma")
        print("3.   Resta")
        print("")
        operacion = (input("Ingrese el numero de operacion que desea utilizar: "))
        
        if(VD.numero_entero(operacion) == True): 
            operacion=int(operacion)
            
            if(operacion == 1):
                while(condicion==True):

                    binario = B.Ingresar_Binario()
                    resultado = B.Conversion_Binario_a_Decimal(binario)
                    #mostrar resultado
                    condicion = realizar_otra()

    

nuevoMenu()