from logica_borrosa import calcular_dificultad, temperatura
from rutas import crear_grafo_rutas, dibujar_grafo
from equipamiento import recomendar_equipamiento

if __name__ == "__main__":
    # Crear y dibujar el grafo de rutas
  #  grafo = crear_grafo_rutas()
   # dibujar_grafo(grafo)

    # Ejemplo de parámetros
    desnivel = int(input("Ingrese el desnivel (en metros): "))
    longitud = int(input("Ingrese la longitud de la ruta (en kilómetros): "))
    terreno = int(input("Ingrese la estabilidad del terreno (0-10): "))
    temperatura = int(input("Ingrese la temperatura (en grados Celsius): "))
    temporal = int(input("Ingrese la condición temporal. Despejado(0-3) Lluvia(3-7) Niebla(7-10): "))

    # Convierte el valor numérico de dificultad en una categoría de texto.
    def interpretar_dificultad(valor_dificultad):
        if valor_dificultad <= 0.3:
            return "Muy Fácil"
        elif valor_dificultad <= 0.6:
            return "Fácil"
        elif valor_dificultad <= 0.8:
            return "Difícil"
        else:
            return "Muy Difícil"

    # Calcular la dificultad de la ruta
    dificultad = calcular_dificultad(desnivel, longitud, terreno, temperatura, temporal)
    if dificultad is not None:
        print(f"Nivel de dificultad de la ruta: {dificultad:.2f}")
        texto_dificultad = interpretar_dificultad(dificultad)
        print(f"Nivel de dificultad de la ruta: {texto_dificultad}")
    else:
        print("No se pudo calcular la dificultad de la ruta.")

    # Sugerir equipamiento
    equipo = recomendar_equipamiento(temperatura, terreno, desnivel, longitud)
    print("Recomendaciones de equipamiento:")
    for item in equipo:
        print(f"- {item}")

