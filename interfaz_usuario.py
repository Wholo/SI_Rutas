import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from umbral_temporal import analizar_cielo

# Ajusta estas importaciones a la ruta real de tus archivos:
from logica_borrosa import calcular_dificultad, interpretar_dificultad
from equipamiento import recomendar_equipamiento
from datos_meteorologicos import obtener_datos_meteorologicos

# Variable global para almacenar la ruta de la imagen cargada
ruta_imagen_cargada = None

def temporal_a_texto(temporal_val):
    """
    Mapea el valor numérico de temporal a un texto descriptivo.
    Ajusta los valores 1, 5, 9 a los que retornas en 'analizar_cielo'.
    """
    if temporal_val == 1:
        return "Despejado"
    elif temporal_val == 5:
        return "Nubes"
    elif temporal_val == 9:
        return "Lluvia"
    else:
        return "Desconocido"

def cargar_imagen():
    global ruta_imagen_cargada
    ruta = filedialog.askopenfilename(
        title="Seleccionar imagen de cielo",
        filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.bmp *.webp")]
    )
    if ruta:
        ruta_imagen_cargada = ruta
        label_imagen.config(text=f"Imagen cargada:\n{ruta}")
    else:
        ruta_imagen_cargada = None
        label_imagen.config(text="No se ha seleccionado ninguna imagen")

def mostrar_dificultad():
    """
    Obtiene los valores de entrada de la interfaz,
    calcula la dificultad y muestra el resultado en un Label.
    """
    try:
        desnivel = int(entry_desnivel.get())
        longitud = int(entry_longitud.get())
        terreno = int(entry_terreno.get())
        temperatura = int(entry_temperatura.get())

        if not ruta_imagen_cargada:
            # No hay imagen -> asumimos cielo despejado
            temporal_val = 1
        else:
            # Analizar la imagen
            temporal_val = analizar_cielo(ruta_imagen_cargada)
            if temporal_val is None:
                # Si hubo fallo, también asumimos despejado
                temporal_val = 1

        # Mostrar la etiqueta textual del cielo en label_temporal
        texto_temporal = temporal_a_texto(temporal_val)
        label_temporal.config(text=f"Resultado del cielo: {texto_temporal}")

        # Calcular la dificultad usando la lógica borrosa
        dificultad = calcular_dificultad(desnivel, longitud, terreno, temperatura, temporal_val)
        texto_dificultad = interpretar_dificultad(dificultad)

        # Mostrar el resultado en la misma ventana (Label 'label_resultado')
        label_resultado.config(
            text=f"Nivel de dificultad: {texto_dificultad}\n(Índice difuso: {dificultad:.2f})"
        )

    except ValueError:
        label_resultado.config(text="Error: Ingresa valores numéricos válidos.")

def mostrar_equipamiento():
    """
    Abre una nueva ventana con el equipamiento sugerido,
    en función de los mismos valores introducidos por el usuario.
    """
    try:
        desnivel = int(entry_desnivel.get())
        longitud = int(entry_longitud.get())
        terreno = int(entry_terreno.get())
        temperatura = int(entry_temperatura.get())

        if not ruta_imagen_cargada:
            temporal_val = 1
        else:
            temporal_val = analizar_cielo(ruta_imagen_cargada)
            if temporal_val is None:
                temporal_val = 1

        # Llamamos a la función que genera la recomendación
        equipo_recomendado = recomendar_equipamiento(
            temperatura, terreno, desnivel, longitud, temporal_val
        )

        # Crear la ventana emergente (Toplevel) donde mostraremos el equipamiento
        equip_window = tk.Toplevel(root)
        equip_window.title("Equipamiento Sugerido")
        equip_window.geometry("400x300")
        equip_window.resizable(False, False)
        tk.Label(equip_window, text="Equipamiento Recomendado:",
                 font=("Arial", 12, "bold")).pack(pady=5)
        for item in equipo_recomendado:
            tk.Label(equip_window, text=f"- {item}").pack(anchor="w")

    except ValueError:
        # Si hay un error de conversión de datos
        equip_window = tk.Toplevel(root)
        equip_window.title("Error")
        tk.Label(equip_window, text="Error: valores numéricos inválidos").pack(pady=10)

def mostrar_datos_meteorologicos():
    ciudad = entry_ciudad.get()
    datos_meteo = obtener_datos_meteorologicos(ciudad)

    if datos_meteo:
        messagebox.showinfo("Datos Meteorológicos",
                            f"Temperatura: {datos_meteo['temperatura']-273}°C\n"
                            f"Clima: {datos_meteo['clima']}")
    else:
        messagebox.showerror("Error", "No se pudieron obtener los datos meteorológicos.")


# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Rutas - Interfaz de Usuario")
root.geometry("800x600")  # Ancho x Alto
root.resizable(False, False)  # Opcional, si no quieres que se cambie el tamaño

# Campo: Desnivel
tk.Label(root, text="Desnivel (m):").pack()
entry_desnivel = tk.Entry(root)
entry_desnivel.pack()

# Campo: Longitud
tk.Label(root, text="Longitud (km):").pack()
entry_longitud = tk.Entry(root)
entry_longitud.pack()

# Campo: Terreno
tk.Label(root, text="Terreno (0-10):").pack()
entry_terreno = tk.Entry(root)
entry_terreno.pack()

# Campo: Temperatura
tk.Label(root, text="Temperatura (°C):").pack()
entry_temperatura = tk.Entry(root)
entry_temperatura.pack()

# Botón para cargar imagen de cielo
btn_cargar_img = tk.Button(root, text="Cargar Imagen de Cielo", command=cargar_imagen)
btn_cargar_img.pack(pady=5)

# Label para mostrar la ruta de la imagen o mensaje
label_imagen = tk.Label(root, text="No se ha seleccionado ninguna imagen", fg="blue", pady=10)
label_imagen.pack()

# Botón para calcular dificultad
tk.Button(root, text="Calcular Dificultad", command=mostrar_dificultad).pack(pady=5)

# Label para mostrar el resultado del cielo (despejado, nubes, lluvia)
label_temporal = tk.Label(root, text="", fg="green", pady=5)
label_temporal.pack()

# Label para mostrar el resultado en la misma ventana
label_resultado = tk.Label(root, text="", fg="blue", pady=10)
label_resultado.pack()

# Botón para sugerir equipamiento
tk.Button(root, text="Sugerir Equipamiento", command=mostrar_equipamiento).pack(pady=5)

#Botón para elegir una ciudad
tk.Label(root, text="Ciudad:").pack()
entry_ciudad = tk.Entry(root)
entry_ciudad.pack()

tk.Button(root, text="Obtener Datos Meteorológicos", command=mostrar_datos_meteorologicos).pack()

# Ejecutar el bucle principal de la interfaz
root.mainloop()


