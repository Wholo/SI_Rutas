import tkinter as tk
from tkinter import messagebox
from logica_borrosa import calcular_dificultad
from logica_borrosa import interpretar_dificultad

def mostrar_dificultad():
    """
    Obtiene los valores de entrada de la interfaz,
    calcula la dificultad y muestra el resultado.
    """
    try:
        desnivel = int(entry_desnivel.get())
        longitud = int(entry_longitud.get())
        terreno = int(entry_terreno.get())
        temperatura = int(entry_temperatura.get())

        # Calcular la dificultad usando la lógica borrosa
        dificultad = calcular_dificultad(desnivel, longitud, terreno, temperatura)
        texto_dificultad = interpretar_dificultad(dificultad)
        messagebox.showinfo("Resultado", f"Nivel de dificultad: {texto_dificultad}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Rutas - Interfaz de Usuario")

# Campos de entrada
tk.Label(root, text="Desnivel (m):").pack()
entry_desnivel = tk.Entry(root)
entry_desnivel.pack()

tk.Label(root, text="Longitud (km):").pack()
entry_longitud = tk.Entry(root)
entry_longitud.pack()

tk.Label(root, text="Terreno (0-10):").pack()
entry_terreno = tk.Entry(root)
entry_terreno.pack()

tk.Label(root, text="Temperatura (°C):").pack()
entry_temperatura = tk.Entry(root)
entry_temperatura.pack()

# Botón para calcular dificultad
tk.Button(root, text="Calcular Dificultad", command=mostrar_dificultad).pack()

# Ejecutar el bucle principal de la interfaz
root.mainloop()
