import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variables de entrada
desnivel = ctrl.Antecedent(np.arange(0, 2001, 1), 'desnivel')  # Desnivel en metros
longitud = ctrl.Antecedent(np.arange(0, 51, 1), 'longitud')    # Longitud en km
terreno = ctrl.Antecedent(np.arange(0, 11, 1), 'terreno')      # Estabilidad del terreno

# Variable de salida
dificultad = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'dificultad')

# Definir funciones de pertenencia
desnivel['bajo'] = fuzz.trimf(desnivel.universe, [0, 0, 500])
desnivel['medio'] = fuzz.trimf(desnivel.universe, [300, 1000, 1500])
desnivel['alto'] = fuzz.trimf(desnivel.universe, [1000, 2000, 2000])

longitud['corta'] = fuzz.trimf(longitud.universe, [0, 0, 15])
longitud['media'] = fuzz.trimf(longitud.universe, [10, 25, 40])
longitud['larga'] = fuzz.trimf(longitud.universe, [30, 50, 50])

terreno['estable'] = fuzz.trimf(terreno.universe, [0, 0, 5])
terreno['inestable'] = fuzz.trimf(terreno.universe, [5, 10, 10])

dificultad['muy_facil'] = fuzz.trimf(dificultad.universe, [0, 0, 0.3])
dificultad['facil'] = fuzz.trimf(dificultad.universe, [0.2, 0.4, 0.6])
dificultad['dificil'] = fuzz.trimf(dificultad.universe, [0.5, 0.8, 1])
dificultad['muy_dificil'] = fuzz.trimf(dificultad.universe, [0.7, 1, 1])

# Reglas borrosas
rules = [
    ctrl.Rule(desnivel['bajo'] & longitud['corta'] & terreno['estable'], dificultad['muy_facil']),
    ctrl.Rule(desnivel['medio'] & longitud['media'] & terreno['estable'], dificultad['facil']),
    ctrl.Rule(desnivel['alto'] & longitud['larga'] & terreno['inestable'], dificultad['muy_dificil']),
    ctrl.Rule(desnivel['medio'] & longitud['media'] & terreno['inestable'], dificultad['dificil'])
]

# Sistema de control borroso
dificultad_ctrl = ctrl.ControlSystem(rules)
dificultad_sim = ctrl.ControlSystemSimulation(dificultad_ctrl)

def calcular_dificultad(desnivel_val, longitud_val, terreno_val):
    dificultad_sim.input['desnivel'] = desnivel_val
    dificultad_sim.input['longitud'] = longitud_val
    dificultad_sim.input['terreno'] = terreno_val
    dificultad_sim.compute()
    return dificultad_sim.output['dificultad']
