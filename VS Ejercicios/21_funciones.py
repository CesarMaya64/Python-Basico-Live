opc = 1
valor1 = 0
valor2 = 0

def suma(val1, val2):
    return val1 + val2

def resta(val1, val2):
    return val1 - val2

def multiplicacion(val1, val2):
    return val1 * val2

def division(val1, val2):
    return val1 / val2

def operaciones_basicas(val1, val2, operador):
    if operador == "+":
        return val1 + val2
    elif  operador == "-":
        return val1 - val2
    elif  operador == "*":
        return val1 * val2
    elif  operador == "/":
        return val1 / val2

while opc >= 1 and opc <= 5:
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    print("5.- Salir")
    opc  = int(input())
    if opc == 5:
        print("Bye")
        break
    elif opc >= 1 and opc <= 4:
        print("Captura valor1:")
        valor1  = float(input())
        print("Captura valor2:")
        valor2  = float(input())
    if opc == 1:
        #print("Resultado +: " + str(suma(valor1, valor2)))
        print("Resultado +: " + str(operaciones_basicas(valor1, valor2, "+")))
    elif opc == 2:
        #print("Resultado -: " + str(resta(valor1, valor2)))
        print("Resultado +: " + str(operaciones_basicas(valor1, valor2, "-")))
    elif opc == 3:
        #print("Resultado *: " + str(multiplicacion(valor1, valor2)))
        print("Resultado +: " + str(operaciones_basicas(valor1, valor2, "*")))
    elif opc == 4:
        #print("Resultado /: " + str(division(valor1, valor2)))
        print("Resultado +: " + str(operaciones_basicas(valor1, valor2, "/")))
    opc = 1
    
