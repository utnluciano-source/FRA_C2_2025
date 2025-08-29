def main():
    print("🎢 ¡Bienvenido al Parque de Diversiones PythonLand! 🎠")
    print("=" * 50)
    
    # 1. Ingreso de datos secuenciales
    nombre = input("Ingrese el nombre del visitante: ").strip()
    
    while True:
        try:
            edad = int(input("Ingrese la edad del visitante: "))
            if edad < 0:
                print("La edad no puede ser negativa. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")
    
    # Información de las atracciones
    atracciones = {
        "Montaña Rusa": {"precio": 1500, "edad_minima": 12},
        "Casa del Terror": {"precio": 1200, "edad_minima": 6},
        "Carrusel": {"precio": 800, "edad_minima": 0}
    }
    
    print(f"\nEl parque tiene {len(atracciones)} atracciones disponibles:")
    for i, atraccion in enumerate(atracciones.keys(), 1):
        precio = atracciones[atraccion]["precio"]
        print(f"{i}. {atraccion} - ${precio}")
    
    while True:
        try:
            num_atracciones = int(input(f"\n¿Cuántas atracciones quiere usar {nombre}? (máximo 3): "))
            if 1 <= num_atracciones <= 3:
                break
            else:
                print("Debe elegir entre 1 y 3 atracciones.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # 2. y 3. Uso de condicionales y ciclos
    atracciones_elegidas = []
    atracciones_permitidas = []
    costo_total = 0
    
    print(f"\n{nombre}, por favor elija sus atracciones:")
    
    for i in range(num_atracciones):
        print(f"\nAtracción {i + 1}:")
        print("1. Montaña Rusa")
        print("2. Casa del Terror") 
        print("3. Carrusel")
        
        while True:
            try:
                opcion = int(input("Seleccione una opción (1-3): "))
                if 1 <= opcion <= 3:
                    break
                else:
                    print("Por favor, seleccione una opción válida (1-3).")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        # Mapear opción a nombre de atracción
        nombres_atracciones = ["Montaña Rusa", "Casa del Terror", "Carrusel"]
        atraccion_elegida = nombres_atracciones[opcion - 1]
        
        # Evitar duplicados
        if atraccion_elegida in atracciones_elegidas:
            print(f"Ya seleccionó {atraccion_elegida}. Elija otra atracción.")
            i -= 1  # Repetir esta iteración
            continue
            
        atracciones_elegidas.append(atraccion_elegida)
        
        # Verificar si puede subir según la edad
        puede_subir = verificar_acceso(edad, atraccion_elegida, atracciones)
        
        if puede_subir:
            atracciones_permitidas.append(atraccion_elegida)
            costo_total += atracciones[atraccion_elegida]["precio"]
            print(f"✅ ¡{nombre} puede subir a {atraccion_elegida}!")
        else:
            print(f"❌ {nombre} no puede subir a {atraccion_elegida}")
            mostrar_razon_restriccion(edad, atraccion_elegida)
    
    # 4. Salida de resultados
    mostrar_resumen(nombre, edad, atracciones_elegidas, atracciones_permitidas, costo_total)

def verificar_acceso(edad, atraccion, atracciones_info):
    """
    Determina si un visitante puede acceder a una atracción según su edad
    """
    # Restricciones especiales por edad
    if edad < 6:
        # Menores de 6 años solo pueden usar el Carrusel
        return atraccion == "Carrusel"
    elif edad < 12:
        # Entre 6 y 11 años no pueden usar la Montaña Rusa
        return atraccion != "Montaña Rusa"
    else:
        # 12 años o más pueden usar todas las atracciones
        return True

def mostrar_razon_restriccion(edad, atraccion):
    """
    Muestra la razón por la cual no puede acceder a una atracción
    """
    if edad < 6 and atraccion != "Carrusel":
        print(f"   Razón: Los menores de 6 años solo pueden usar el Carrusel por seguridad.")
    elif edad < 12 and atraccion == "Montaña Rusa":
        print(f"   Razón: Debe tener al menos 12 años para subir a la Montaña Rusa.")

def mostrar_resumen(nombre, edad, elegidas, permitidas, costo):
    """
    Muestra el resumen final de la visita
    """
    print("\n" + "=" * 60)
    print("📋 RESUMEN DE LA VISITA")
    print("=" * 60)
    print(f"👤 Visitante: {nombre}")
    print(f"🎂 Edad: {edad} años")
    
    print(f"\n🎯 Atracciones elegidas ({len(elegidas)}):")
    for i, atraccion in enumerate(elegidas, 1):
        print(f"   {i}. {atraccion}")
    
    print(f"\n✅ Atracciones permitidas ({len(permitidas)}):")
    if permitidas:
        for i, atraccion in enumerate(permitidas, 1):
            print(f"   {i}. {atraccion}")
    else:
        print("   Ninguna atracción disponible para esta edad.")
    
    if len(elegidas) != len(permitidas):
        print(f"\n❌ Atracciones no permitidas ({len(elegidas) - len(permitidas)}):")
        no_permitidas = [a for a in elegidas if a not in permitidas]
        for i, atraccion in enumerate(no_permitidas, 1):
            print(f"   {i}. {atraccion}")
    
    print(f"\n💰 Costo total a pagar: ${costo:,}")
    
    if costo > 0:
        print(f"\n🎉 ¡Disfrute su visita a PythonLand, {nombre}!")
    else:
        print(f"\n😔 Lo sentimos {nombre}, por su edad no puede acceder a ninguna de las atracciones elegidas.")
        print("   Le recomendamos el Carrusel, ¡es muy divertido!")

# Ejecutar el programa
if __name__ == "__main__":
    main()