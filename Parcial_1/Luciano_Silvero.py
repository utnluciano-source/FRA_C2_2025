# ============================================
# CONSTANTES
# ============================================
MAX = 10

# ============================================
# INICIALIZACIÓN DE LISTAS ESTÁTICAS
# ============================================
lista_nombres = [""] * MAX
lista_libros = [0] * MAX
lista_comentarios = [""] * MAX

# ============================================
# FUNCIONES
# ============================================

# ---------- Función de validación de ingreso de textos -----------
def ingresar_texto(mensaje):
    texto = ""
    while texto == "":
        texto = input(mensaje)
        if texto == "":
            print("No puede quedar en blanco...")
    
    return texto

# ------------ Función para validar libros de 1 a 20 ----------
def ingresar_libros(mensaje):
    while True:
        numero_str = input(mensaje)
        
        # Validar que no esté vacío
        if numero_str == "":
            print("No puede quedar en blanco...")
            continue
        
        # Validar que todos sean dígitos (SIN isdigit ni isnumeric)
        es_numero = True
        for caracter in numero_str:
            if caracter < '0' or caracter > '9':
                es_numero = False
                break
        
        if not es_numero:
            print("Debe ingresar un número válido")
            continue
        
        # Ahora sí convertir a entero
        numero = int(numero_str)
        if 1 <= numero <= 20:
            return numero
        else:
            print("Debe ingresar un número entre 1 y 20")

# --------- Función para cargar datos --------------------
def ingresar_datos(lista_nombres, lista_libros, lista_comentarios, cantidad):
    while cantidad < MAX:
        print(f"------ Alumno {cantidad + 1} ------")
        lista_nombres[cantidad] = ingresar_texto("Ingrese nombre completo: ")
        lista_libros[cantidad] = ingresar_libros("Ingrese cantidad de libros leídos (1-20): ")
        lista_comentarios[cantidad] = ingresar_texto("Ingrese comentario: ")
        cantidad += 1
        continuar = input("¿Desea ingresar otro alumno? (s/n): ").lower()
        if continuar != "s":
            break
    return cantidad

# ------------ Función para mostrar datos ---------------
def mostrar_datos(nombres, libros, comentarios, cantidad):
    if cantidad == 0:
        print("No hay datos cargados...")
        return
    suma = 0
    print("\n===== HÁBITOS DE LECTURA =====")
    for i in range(cantidad):
        print(f"\nAlumno {i + 1}:")
        print(f"  Nombre: {nombres[i]}")
        print(f"  Libros leídos: {libros[i]}")
        print(f"  Comentario: {comentarios[i]}")
        suma += libros[i]
    promedio = suma / cantidad
    print(f"\nPromedio de libros leídos: {promedio:.2f}")

# ---------- Función para ordenar con Bubble Sort DESCENDENTE ----------------------
def ordenar_por_libros(nombres, libros, comentarios, cantidad):
    if cantidad == 0:
        print("No hay datos para ordenar...")
        return
    
    # Bubble Sort DESCENDENTE (de mayor a menor)
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if libros[j] < libros[j + 1]:
                # Intercambiar libros
                libros[j], libros[j + 1] = libros[j + 1], libros[j]
                # Intercambiar nombres
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                # Intercambiar comentarios
                comentarios[j], comentarios[j + 1] = comentarios[j + 1], comentarios[j]
    
    print("\n===== ALUMNOS ORDENADOS POR CANTIDAD DE LIBROS (DESCENDENTE) =====")
    for i in range(cantidad):
        print(f"\nPosición {i + 1}:")
        print(f"  Nombre: {nombres[i]}")
        print(f"  Libros leídos: {libros[i]}")
        print(f"  Comentario: {comentarios[i]}")

# ============================================
# PROGRAMA PRINCIPAL 
# ============================================
cantidad = 0

while True:
    print("\n" + "="*50)
    print("REGISTRO DE HÁBITOS DE LECTURA")
    print("="*50)
    print("1. Ingresar datos de los alumnos")
    print("2. Mostrar hábitos de lectura")
    print("3. Ordenar alumnos por cantidad de libros leídos")
    print("4. Salir")
    print("="*50)
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        cantidad = ingresar_datos(lista_nombres, lista_libros, lista_comentarios, cantidad)
        print(f"\nTotal de alumnos registrados: {cantidad}")
    elif opcion == "2":
        mostrar_datos(lista_nombres, lista_libros, lista_comentarios, cantidad)
    elif opcion == "3":
        ordenar_por_libros(lista_nombres, lista_libros, lista_comentarios, cantidad)
    elif opcion == "4":
        print("\n¡Gracias por usar el programa!")
        break
    else:
        print("Opción inválida, intente nuevamente.")
