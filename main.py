from logica_borrosa import calcular_dificultad
from rutas import crear_grafo_rutas

if __name__ == "__main__":
    # Crear el grafo de rutas
    grafo = crear_grafo_rutas()

    # Ejemplo de parámetros
    desnivel = 800  # metros
    longitud = 20   # km
    terreno = 7     # inestabilidad

    # Calcular dificultad
    dificultad = calcular_dificultad(desnivel, longitud, terreno)
    print(f"Nivel de dificultad de la ruta: {dificultad:.2f}")
