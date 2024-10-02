# Pedir al usuario que ingrese una lista de nombres separados por comas
entrada_nombres = input("Introduce una lista de nombres separados por comas: ")

# Crear una lista de nombres y eliminar los espacios adicionales
nombres = [nombre.strip() for nombre in entrada_nombres.split(",")]

# Ordenar los nombres alfabéticamente
nombres.sort()

# Imprimir los nombres en orden alfabético
print("\nNombres en orden alfabético:")
for nombre in nombres:
    print(nombre)