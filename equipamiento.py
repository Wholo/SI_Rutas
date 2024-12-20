def recomendar_equipamiento(temperatura, terreno, desnivel, longitud):
    """
    Genera recomendaciones de equipamiento basadas en la temperatura y el terreno.
    """
    recomendaciones = []

    # Recomendaciones según la temperatura
    if temperatura < 10:
        recomendaciones.append("Abrigo térmico")
    elif temperatura >= 10 and temperatura <= 25:
        recomendaciones.append("Ropa cómoda y ligera")
    elif temperatura > 25:
        recomendaciones.append("Protección solar")
        recomendaciones.append("Gorra o sombrero")

    # Recomendaciones según el terreno
    if terreno <= 5:
        recomendaciones.append("Botas de senderismo")
    elif terreno > 5 and terreno <= 7:
        recomendaciones.append("Botas de montaña")
        recomendaciones.append("Bastones de trekking")
    else:  # Terreno muy inestable
        recomendaciones.append("Botas técnicas")
        recomendaciones.append("Bastones de trekking")

        # Recomendaciones según el desnivel
    if desnivel > 1000 and longitud <=10:
        recomendaciones.append("Cuerda y arnés")

        # Recomendaciones según la longitud
    if longitud > 20:
        recomendaciones.append("Snacks energéticos")
        recomendaciones.append("Recipientes adicionales para agua")

    return recomendaciones
