import cv2
import numpy as np

def analizar_cielo(ruta_imagen):
    """
    Analiza la imagen para determinar:
      - 1 (Despejado) si >= 90% de píxeles son azul cielo
      - 5 (Nubes leves) si < 90% azul y el promedio de brillo (canal V) es alto
      - 9 (Nubes oscuras) si < 90% azul y el promedio de brillo es bajo
    Retorna None si no se pudo cargar la imagen.
    """

    # Cargar la imagen
    img = cv2.imread(ruta_imagen)
    if img is None:
        print("No se pudo cargar la imagen:", ruta_imagen)
        return None

    # Convertir a HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 1) Detectar el porcentaje de píxeles azules (cielo despejado)
    # Rango aproximado para azul cielo en HSV (ajusta si es necesario)
    rango_bajo_azul = np.array([90, 50, 50])    # H=90, S>=50, V>=50
    rango_alto_azul = np.array([130, 255, 255]) # H=130, S<=255, V<=255

    mascara_azul = cv2.inRange(hsv, rango_bajo_azul, rango_alto_azul)

    # Porcentaje de píxeles azules
    alto, ancho = img.shape[:2]
    pixeles_totales = alto * ancho
    pixeles_azules = cv2.countNonZero(mascara_azul)
    porcentaje_azul = (pixeles_azules / pixeles_totales) * 100

    # CRITERIO 1: ¿Cielo despejado (>= 90% azul)?
    umbral_azul = 90.0  # Ajusta al 90% para "despejado"
    if porcentaje_azul >= umbral_azul:
        return 1  # Despejado

    # 2) Si no es >= 90% azul, distinguimos nubes leves u oscuras según brillo
    # Tomar brillo medio (canal V)
    canal_v = hsv[:, :, 2]
    brillo_medio = np.mean(canal_v)  # valor entre 0..255

    # Ajustar el umbral de brillo para separar nubes claras de oscuras
    # Por ejemplo, 120 o 130. Haz pruebas para tu conjunto de imágenes.
    umbral_brillo = 130.0

    if brillo_medio >= umbral_brillo:
        # Nubes claras/blancas => nubes leves
        return 5
    else:
        # Nubes grises/oscuras => nubes oscuras (posible lluvia)
        return 9
