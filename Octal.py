from os import system
import ValidarDatos as VD
import Binario as B
def Ingresar_octal():
    condicion = False
    Octal = ""
    while(condicion == False):
        system("cls")
        print("un numero en octal contiene numeros entre 0 y 7")
        Octal = input("ingrese el numero octal: ")
        
        condicion = VD.numero_Octal(Octal)
    
    print(Octal)    
    input()
    return Octal

def Conversion_binario(dato): #recibe un string
    
    resultado=""
    lista = []
    
    for i in range(0, len(dato)):
        lista.append(int(dato[i]))
    
    for i in range(0, len(lista)):
        auxiliar = B.Conversion_Decimal_a_Binario(lista[i])
        
        if(len(auxiliar) == 1):#si tiene menos de 3 digitos le agrega un 0
            
            auxiliar = "0" + "0" + auxiliar
            
        elif(len(auxiliar) == 2):
            
            auxiliar = "0" + auxiliar
            
        resultado = resultado + auxiliar 

    print(f"{dato} es {resultado} en binario")
    input("Enter para continuar: ")
    system("cls")