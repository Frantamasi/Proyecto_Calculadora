
def suma(numeros): #arreglar los parametros 
    resultado = 0  #arreglar para que se pueda pasar mas de un numero como parametro
    for i in range(0, len(numeros)):
        resultado = resultado + numeros[i]
    print(f"El resultado es {resultado}")    
    input("")

def resta(a, b):
    resultado = a - b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado

def division(a, b):
    resultado = a / b
    return resultado

def devisionEntera(a, b):
    resultado = a // b
    return resultado

def potencia(a, b):
    resultado = a ** b
    return resultado




         
