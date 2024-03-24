import random

productos = []  
ids_usados = []  
conteo_por_tienda= {'A': 0, 'B': 0, 'C': 0, 'D': 0} 


continuar = True

while continuar:
    print("********Menú de opciones*********")
    print("1. Registrar un producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar y mostrar un producto específico por nombre")
    print("4. Modificar el número de unidades de un producto por ID")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        nombre = input("Nombre del producto: ")
        precio_unitario = float(input("Precio unitario del producto: "))
        ubicacion = input("Ubicación en la tienda (A,B,C,D): ").upper()

        
        if ubicacion not in conteo_por_tienda:
            print("Ubicación no válida. Por favor, elija entre A, B, C, D.")
            continue

        num_unidades = int(input("Número de unidades compradas del producto: "))
        
        # Verificar que no  pase de 50 productos
        if conteo_por_tienda[ubicacion] + num_unidades > 50:
            print(f"No se pueden agregar {num_unidades} unidades en la zona {ubicacion} porque supera el límite permitido.")
            continue

        
        conteo_por_tienda[ubicacion] += num_unidades
        
        descripcion = input("Descripción del producto: ")
        casa = input("Casa a la que pertenece el producto (Marvel, DC, etc): ")
        referencia = input("Referencia (código alfanumérico): ")
        pais_origen = input("País de origen del producto: ")
        garantia_extendida = input("Producto con garantía extendida (S/N): ").lower() == 's'

        
        id_producto = random.randint(1, 100)
        while id_producto in ids_usados:
            id_producto = random.randint(1, 100)
        ids_usados.append(id_producto)
        
        producto = {
            "Id": id_producto,
            "Nombre": nombre,
            "Precio unitario": precio_unitario,
            "Ubicación": ubicacion,
            "Descripción": descripcion,
            "Casa": casa,
            "Referencia": referencia,
            "País de origen": pais_origen,
            "Número de unidades": num_unidades,
            "Garantía extendida": garantia_extendida
        }
        
        productos.append(producto)
        print("Producto registrado exitosamente.")
    
    elif opcion == '2':
        if not productos:
            print("No hay productos registrados.")
        else:
            for producto in productos:
                print(f"Id: {producto['Id']}, Nombre: {producto['Nombre']}, Ubicación: {producto['Ubicación']}, Número de unidades: {producto['Número de unidades']}")
                print("-" * 20)  
    
    elif opcion == '3':
        nombre_buscado = input("Ingrese el nombre del producto a buscar: ").lower()
        encontrado = False
        for producto in productos:
            if producto['Nombre'].lower() == nombre_buscado:
                print(f"Id: {producto['Id']}, Nombre: {producto['Nombre']}, Precio unitario: {producto['Precio unitario']}, Descripción: {producto['Descripción']}")
                encontrado = True
                break  
        if not encontrado:
            print("Producto no encontrado.")
    
    elif opcion == '4':
        id_producto = int(input("Ingrese el ID del producto a modificar: "))
        nuevas_unidades = int(input("Nuevo número de unidades compradas del producto: "))
        encontrado = False
        for producto in productos:
            if producto['Id'] == id_producto:
                if nuevas_unidades <= producto['Número de unidades']:
                    diferencia_unidades = producto['Número de unidades'] - nuevas_unidades
                    producto['Número de unidades'] = nuevas_unidades
                    conteo_por_tienda[producto['Ubicación']] -= diferencia_unidades
                    print("Número de unidades actualizado correctamente.")
                    encontrado = True
                    break 
        if not encontrado:
            print("Producto no encontrado.")
    
    elif opcion == '5':
        print("Saliendo del programa...")
        continuar = False
    
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
