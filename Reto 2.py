# Programa para clasificar hemoglobina de varias personas

# Inicializar contadores
hombres_baja = 0
hombres_normal = 0
hombres_alta = 0
mujeres_baja = 0
mujeres_normal = 0
mujeres_alta = 0


# Pedir número de personas
N = int(input(" "))

# Ciclo para cada persona
for i in range(1, N + 1):
    print(f"\nPersona {i}:")
    
    # Validar género (1 = masculino, 2 = femenino)
    while True:
        print("Seleccione su género:")
        print("1. Masculino")
        print("2. Femenino")
        genero = int(input(" "))
        if genero == 1 or genero == 2:
            break
        else:
            print("Opción no válida, intente de nuevo.")

    # Leer hemoglobina
    print ("hemoglobina")
    hemoglobina = float(input(" "))

    # Clasificación según género
    if genero == 1:  # Masculino
        if hemoglobina < 12.2:
            hombres_baja += 1
        elif hemoglobina > 16.6:
            hombres_alta += 1
        else:
            hombres_normal += 1
    else:  # Femenino
        if hemoglobina < 12.6:
            mujeres_baja += 1
        elif hemoglobina > 15:
            mujeres_alta += 1
        else:
            mujeres_normal += 1

# Resultados finales
print("Resultados ")
print("Hombres:")
print("  Baja   :", hombres_baja)
print("  Normal :", hombres_normal)
print("  Alta   :", hombres_alta)

print("Mujeres:")
print("  Baja   :", mujeres_baja)
print("  Normal :", mujeres_normal)
print("  Alta   :", mujeres_alta)
