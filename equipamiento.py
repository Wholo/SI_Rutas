def sugerir_equipamiento(dificultad):
    """
    Sugiere equipamiento en función de la dificultad calculada.
    """
    if dificultad < 0.3:
        return ["Botella de agua", "Zapatillas cómodas"]
    elif dificultad < 0.6:
        return ["Botas de senderismo", "Protección solar"]
    elif dificultad < 0.8:
        return ["Botas de montaña", "Bastones", "Chubasquero"]
    else:
        return ["Botas técnicas", "Cuerda", "Arnés", "Casco"]
