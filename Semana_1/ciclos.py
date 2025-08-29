#Ejemplos de ciclos for y while
#While

'''
numero = int(input("Ingrese un número: "))

while numero < 100:
    print(numero)
    numero = int(input("Ingrese un número: "))

#while numero < 100 and numero > 50:
#    print(numero)
#    numero = int(input("Ingrese un número: "))

numero = int(input("Ingresar números positivos"))

if numero > 0:
    control = True

while control:
    numero = int(input("Ingresar números positivos"))
    if numero > 0:
        control = True
    else:
        control = False


contador_positivos = 0
contador_negativos = 0
numero = int(input("Ingresar numeros, corta con 0: "))

while numero != 0:
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1

    numero = int(input("Ingresar numeros, corta con 0: "))

total = 0

while True:
    monto = float(input("Ingresar valor de producto: "))
    total += monto
    if monto == 0:
        break

#for

for x in range(3):
    nombre = input("Ingresar nombre de mascota: ")
    tipo = input("Que tipo de animal es? ")
    print(f"Animal {x + 1}.  {nombre} es un {tipo}")

for x in range(0, 5):
    print(x + 1)

for x in range(0, 11, 2):    
    print(x + 1)
'''

