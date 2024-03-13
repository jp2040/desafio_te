from te import Te

# Crear dos instancias
te_instancia1 = Te(1, 300)
te_instancia2 = Te(2, 500)

# Almacenar el tipo de dato de cada instancia
tipo_dato_instancia1 = type(te_instancia1)
tipo_dato_instancia2 = type(te_instancia2)

# Mostrar por pantalla el valor de cada tipo de dato almacenado
print("Tipo de dato de la instancia 1:", tipo_dato_instancia1)
print("Tipo de dato de la instancia 2:", tipo_dato_instancia2)

# Verificar si ambos tipos almacenados son iguales
if tipo_dato_instancia1 == tipo_dato_instancia2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
