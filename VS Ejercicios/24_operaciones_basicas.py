from operaciones_basicas import suma
from operaciones_basicas import resta
from operaciones_basicas import multiplicacion
from operaciones_basicas import division

opc = 1
valor1 = 0
valor2 = 0

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
        print("Resultado +: " + str(suma(valor1, valor2)))
    elif opc == 2:
        print("Resultado -: " + str(resta(valor1, valor2)))
    elif opc == 3:
        print("Resultado *: " + str(multiplicacion(valor1, valor2)))
    elif opc == 4:
        print("Resultado /: " + str(division(valor1, valor2)))
    opc = 1
    
