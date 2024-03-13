from te import Te

# Solicitar al usuario los datos del pedido
sabor_numero = int(input("Ingrese el número correspondiente al sabor (1. Té negro, 2. Té verde, 3. Agua de hierbas): "))
formato_numero = int(input("Ingrese el número correspondiente al formato (300 o 500 gr): "))

# Crear una instancia de Te con los datos ingresados por el usuario
te_pedido = Te(sabor_numero, formato_numero)

# Obtener el tiempo de preparación y la recomendación
tiempo_preparacion, recomendacion = Te.obtener_tiempo_recomendacion(sabor_numero)

# Obtener el precio
precio = Te.obtener_precio(formato_numero)

# Mostrar detalle del pedido
print("\nDetalle del pedido:")
print("Sabor del té:", "Té negro" if sabor_numero == 1 else "Té verde" if sabor_numero == 2 else "Agua de hierbas")
print("Formato del té:", f"{formato_numero} gr")
print("Precio:", f"${precio}")
print("Tiempo de preparación:", f"{tiempo_preparacion} minutos")
print("Recomendación:", recomendacion)
