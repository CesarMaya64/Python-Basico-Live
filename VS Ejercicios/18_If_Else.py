print("Captura valor 1:")
valor1 = int(input())

print("Captura valor2:")
valor2 = int(input())

if valor1 == valor2:
    print("Las variables son iguales")
elif valor1 > valor2:
    print("El primer valor ("+str(valor1)+") es mayor")
else:
    print("El segundo valor ("+str(valor2)+") es mayor")
