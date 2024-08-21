print("Captura la cadena uno:")
cadena1 = input()

#Se concatena
print(cadena1 + ". Se le concatena esta cadena")
#Se multiplica
print("Se multiplica: " + (cadena1 * 3) + " Hola")

#Operadores +=
cadena_compuesta = cadena1
cadena_compuesta += " "
cadena_compuesta += " Mundo"
print("Cadena compuesta: " + cadena_compuesta)

#Longitud
print("Longitud de la cadena: " + str(len(cadena_compuesta)))

#Encontar
contiene_mundo = cadena_compuesta.find("Mundo")
if contiene_mundo != (-1):
    print("Si contiene la palabra mundo, en la posición: " + str(contiene_mundo))
else:
    print("No contiene la palabra mundo")

#Minusculas
print("Minusculas: " + cadena_compuesta.lower())

#Mayusculas
print("Mayusculas: " + cadena_compuesta.upper())

#Reemplazar
print("Reemplazar: " + cadena_compuesta.replace("M", "Pizza"))

#Cortar
print("Cortar: " + cadena_compuesta[1:4])

