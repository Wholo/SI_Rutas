import tkinter as tk
from tkinter import ttk, messagebox

# Ajusta estas importaciones a la ruta real de tus archivos:
from logica_borrosa import calcular_dificultad, interpretar_dificultad
from equipamiento import recomendar_equipamiento
from datos_meteorologicos import obtener_datos_meteorologicos

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

        # Convertir la opción temporal seleccionada a un valor numérico
        opcion_seleccionada = combo_temporal.get()  # 'Despejado', 'Lluvia', 'Niebla'
        if opcion_seleccionada == "Despejado":
            temporal_val = 1
        elif opcion_seleccionada == "Lluvia":
            temporal_val = 5
        elif opcion_seleccionada == "Niebla":
            temporal_val = 9
        else:
            temporal_val = 1  # Por defecto, si no se elige nada

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

        # Convertir la opción temporal seleccionada a un valor numérico
        opcion_seleccionada = combo_temporal.get()
        if opcion_seleccionada == "Despejado":
            temporal_val = 1
        elif opcion_seleccionada == "Lluvia":
            temporal_val = 5
        elif opcion_seleccionada == "Niebla":
            temporal_val = 9
        else:
            temporal_val = 1  # por defecto

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

# Combobox para la condición temporal
tk.Label(root, text="Condición Temporal:").pack()
combo_temporal = ttk.Combobox(root,
                              values=["Despejado", "Lluvia", "Niebla"],
                              state="readonly")
combo_temporal.current(0)  # Seleccionamos "Despejado" por defecto
combo_temporal.pack()

# Botón para calcular dificultad
tk.Button(root, text="Calcular Dificultad", command=mostrar_dificultad).pack(pady=5)

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


