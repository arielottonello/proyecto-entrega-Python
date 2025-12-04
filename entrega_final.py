from datetime import datetime

def mostrar_menu():
    print("\n" + "="*40) # ======================================
    print("hoy:" + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print( "Sistema de Gestion de Productos") # Sistema de Gestion de Productos
    print("="*40) # ==========================================
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("="*40) 

def validar_texto(mensaje):
    valor = ""
    while valor == "":
        valor = input(mensaje).strip()
        if valor == "":
            print("error: no puede estar vacio.")
    return valor
def validar_numero(mensaje):
    valor = ""
    while not valor.isdigit():
        valor = input (mensaje).strip()  # 2345678  -> ajhsdkasld
        if not valor.isdigit():
            print("error: debe ingresar numeros valido.")
    return int(valor)

# funciones del sistema
def agregar_producto(productos):
    print( "\n --- Agregar Producto ---")
    nombre = validar_texto("Ingresa el nombre del producto: ")
    categoria = validar_texto("Ingresa la categoria del producto: ")
    precio = validar_numero("Ingra el precio del producto: ")
    
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    producto = {"nombre": nombre,"categoria": categoria, "precio": precio, "fecha_creado": fecha}
    productos.append(producto)
    print(f"\n Producto {nombre} agregado correctamente.")

def mostrar_productos(productos):
    """Muestra la lista de productos registrados."""
    print("\n--- Productos Registrados ---")

    if len(productos) == 0:
        print ("No hay productos registrados en el sistema.")
    else:
        print(f"\nTotal de productos: {len(productos)}\n")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto['nombre']}")
            print(f"   Categoría: {producto['categoria']}")
            print(f"   Precio: ${producto['precio']}")
            print(f"   Fecha: {producto['fecha_creado']}")
            print("-" * 30)

def buscar_producto(productos):
    """Busca productos por nombre."""
    print( "\n--- Buscar Producto ---")

    if len(productos) == 0:
        print( "No hay productos registrados en el sistema.")
    else:
        busqueda = input( "Ingrese el nombre del producto a buscar: ").strip().lower()

        if busqueda == "":
            print( " Error: debe ingresar un nombre para buscar.")
        else:
            encontrados = []
            for i, producto in enumerate(productos, start=1):
                if busqueda in producto['nombre'].lower():
                    encontrados.append((i, producto))

            if len(encontrados) > 0:
                print(f"\nSe encontraron {len(encontrados)} coincidencia(s):\n")
                for pos, p in encontrados:
                    print(f"{pos}. Nombre: {p['nombre']}")
                    print(f"   Categoría: {p['categoria']}")
                    print(f"   Precio: ${p['precio']}")
                    print(f"   Fecha: ${p['fecha_creado']}")
                    print("-" * 30)
            else:
                print(f"\nNo se encontraron productos que coincidan con '{busqueda}'.")
                
def eliminar_producto(productos):
    """Elimina un producto por número."""
    print("\n--- Eliminar Producto ---")
    if len(productos) == 0:
        print("No hay productos registrados en el sistema.")
    else:
        mostrar_productos(productos)
        posicion = validar_numero("\nIngrese el número del producto a eliminar: ")

        if 1 <= posicion <= len(productos):
            producto = productos[posicion - 1]
            confirmacion = input(
                f"¿Está seguro que desea eliminar '{producto['nombre']}'? (s/n): "
            ).strip().lower()
            if confirmacion == "s":
                productos.pop(posicion - 1)
                print(f"\n Producto '{producto['nombre']}' eliminado exitosamente.")
            else:
                print("\nEliminación cancelada.")
        else:
            print(f"Error: debe ingresar un número entre 1 y {len(productos)}.")
            
def sistema_gestion():
    print("¡ Bienvenido/a al sistema de pruductos !")
    productos = []

    while True:
        mostrar_menu()
        opcion = input("\n Seleccione una opcion entre (1-5): ").strip()
        
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("\n Error: opción inválida. Por favor seleccione una opción del 1 al 5.")
        input("\nPresione Enter para continuar...")

sistema_gestion()