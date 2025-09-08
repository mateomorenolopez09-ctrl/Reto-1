from collections import Counter

def contar_caracteres_repetidos(cadena: str) -> int:
 
  frecuencias = Counter(cadena)
  # Suma 1 por cada conteo que sea mayor que 1.
  return sum(1 for conteo in frecuencias.values() if conteo > 1)

# --- Ejemplo de uso ---
print(f"\nUsando la versión compacta:")
print(f"'programacion' -> {contar_caracteres_repetidos('programacion')}") # Salida esperada: 3 (p, r, o, a, c, i, n) -> 'r', 'o', 'a' se repiten