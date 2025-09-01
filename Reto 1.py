
# Programa para clasificar niveles de hemoglobina

# Se le solicita info al usuario
print("Seleccione su género:")
print("2. Femenino")
print("1. Masculino")
genero = int(input("Ingrese el número de su género: "))
hemoglobina = float(input("Ingrese la cantidad de hemoglobina: "))

# vemos el genero y el nivel de hemoglovina
if genero == 2:  # Femenino
    if hemoglobina < 12.6:
        print("Baja")
    elif hemoglobina <= 15:
        print("Normal")
    else:
        print("Alta")

elif genero == 1:  # Masculino
    if hemoglobina <= 12.2:
        print("Baja")
    elif hemoglobina <= 16.6:
        print("Normal")
    else:
        print("Alta")

else:
    print("No es posible generar alerta")
