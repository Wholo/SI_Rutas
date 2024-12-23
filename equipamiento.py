from logica_borrosa import temporal


def recomendar_equipamiento(temperatura, terreno, desnivel, longitud, temporal):
    """
    Genera recomendaciones de equipamiento basadas en la temperatura y el terreno.
    """
    recomendaciones = []
    #Recomendaciones para cualquier tipo de ruta
    recomendaciones.append("Linterna")
    recomendaciones.append("Ropa cambio")
    recomendaciones.append("Comida")
    recomendaciones.append("Cuchillo")
    recomendaciones.append("Botiquín")
    recomendaciones.append("Mapa")
    # Recomendaciones según la temperatura
    if temperatura < 10:
        recomendaciones.append("Abrigo térmico")
    elif 10 <= temperatura <= 25:
        recomendaciones.append("Ropa cómoda y ligera")
    elif temperatura > 25:
        recomendaciones.append("Protección solar")
        recomendaciones.append("Gorra o sombrero")
        recomendaciones.append("Botas técnicas")
        recomendaciones.append("Gafas de sol")

    # Recomendaciones según el terreno
    if terreno <= 5:
        recomendaciones.append("Botas de senderismo")
    elif 5 < terreno <= 7:
        recomendaciones.append("Botas de montaña")
        recomendaciones.append("Bastones de trekking")
    elif 7 < terreno <= 9:
        recomendaciones.append("Botas técnicas")
        recomendaciones.append("Bastones de trekking")
    else:
        recomendaciones.append("Botas técnicas")
        recomendaciones.append("Bastones de trekking")
        recomendaciones.append("Piolet")
        recomendaciones.append("Crampones")

        # Recomendaciones según el desnivel
    if desnivel > 1000 and longitud <=10:
        recomendaciones.append("Cuerda y arnés")

        # Recomendaciones según la longitud
    if longitud > 20:
        recomendaciones.append("Snacks energéticos")
        recomendaciones.append("Recipientes adicionales para agua")

    #Recomendaciones según el temporal
    if 3 < temporal <= 7:
        recomendaciones.append("Chubasquero")
        recomendaciones.append("Toalla")
    elif temporal < 7:
        recomendaciones.append("Linterna frontal")
        recomendaciones.append("Chubasquero")

    return recomendaciones
