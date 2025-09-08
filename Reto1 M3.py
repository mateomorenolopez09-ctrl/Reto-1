def sucesion_fibonacci(cantidad_numeros: int) -> str:
    # Casos base
    if cantidad_numeros <= 0:
        return ""
    elif cantidad_numeros == 1:
        return "0"

    # Lista para guardar la sucesión
    fib = [0, 1]

    # Usamos for para generar los demás números
    for i in range(2, cantidad_numeros):
        fib.append(fib[i-1] + fib[i-2])

    # Unimos los números en una cadena separada por comas
    return ",".join(map(str, fib)) 