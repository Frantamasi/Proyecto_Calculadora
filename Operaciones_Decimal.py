
def suma(numeros): #arreglar los parametros 
    resultado = 0  #arreglar para que se pueda pasar mas de un numero como parametro
    for i in range(0, len(numeros)):
        resultado = resultado + numeros[i]
    print(f"{numeros[0]} + {numeros[1]} = {resultado}")    
    input("")
    return resultado


def resta(numeros):
    resultado = 0
    for i in range(0, len(numeros)):
        resultado = numeros[i] - resultado 
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
