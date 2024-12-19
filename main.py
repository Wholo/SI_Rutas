from logica_borrosa import calcular_dificultad, temperatura
from rutas import crear_grafo_rutas, dibujar_grafo
from equipamiento import sugerir_equipamiento

if __name__ == "__main__":
    # Crear y dibujar el grafo de rutas
  #  grafo = crear_grafo_rutas()
   # dibujar_grafo(grafo)

    # Ejemplo de parámetros
    desnivel = 800
    longitud = 20
    terreno = 7
    temperatura = 35

    # Calcular dificultad
    dificultad = calcular_dificultad(desnivel, longitud, terreno,temperatura)
    print(f"Nivel de dificultad de la ruta: {dificultad:.2f}")

    # Sugerir equipamiento
    equipo = sugerir_equipamiento(dificultad)
    print(f"Equipo recomendado para esta ruta: {', '.join(equipo)}")
