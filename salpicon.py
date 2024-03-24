
frutas = []

n = int(input("CUANTAS FRUTAS DESEAS AGREGAR ?"))


nombre_fruta_barata = ""
precio_fruta_barata = float('inf')  


costo_total_salpicon = 0

for i in range(n):
    print(f"\nFruta {i+1}:")
    nombre = input("Nombre de la fruta: ")
    precio_unitario = float(input("Precio unitario de la fruta: "))
    cantidad = int(input("Cuantas porciones deseas agregar: "))
    costo_total = precio_unitario * cantidad

    
    costo_total_salpicon += costo_total

   
    if precio_unitario < precio_fruta_barata:
        precio_fruta_barata = precio_unitario
        nombre_fruta_barata = nombre

    
    frutas.append({
        'nombre': nombre,
        'precio_unitario': precio_unitario,
        'cantidad': cantidad,
        'costo_total': costo_total
    })


print(f"\nCosto total del salpicón: {costo_total_salpicon}")

frutas_ordenadas = sorted(frutas, key=lambda x: x['costo_total'], reverse=True)
print("Frutas ordenadas por costo total de mayor a menor:")
for fruta in frutas_ordenadas:
    print(f"{fruta['nombre']}: {fruta['costo_total']}")
print(f"\nLa fruta más barata es: {nombre_fruta_barata} con un precio de {precio_fruta_barata}")
