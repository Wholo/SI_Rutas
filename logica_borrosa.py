import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variables de entrada
desnivel = ctrl.Antecedent(np.arange(0, 2001, 1), 'desnivel')  # Desnivel en metros
longitud = ctrl.Antecedent(np.arange(0, 51, 1), 'longitud')    # Longitud en km
terreno = ctrl.Antecedent(np.arange(0, 11, 1), 'terreno')      # Estabilidad del terreno
temperatura = ctrl.Antecedent(np.arange(-10, 41, 1), 'temperatura')
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

temperatura['frio'] = fuzz.trimf(temperatura.universe, [-10, 0, 15])
temperatura['templado'] = fuzz.trimf(temperatura.universe, [10, 20, 30])
temperatura['calor'] = fuzz.trimf(temperatura.universe, [25, 40, 40])

dificultad['muy_facil'] = fuzz.trimf(dificultad.universe, [0, 0, 0.3])
dificultad['facil'] = fuzz.trimf(dificultad.universe, [0.2, 0.4, 0.6])
dificultad['dificil'] = fuzz.trimf(dificultad.universe, [0.5, 0.8, 1])
dificultad['muy_dificil'] = fuzz.trimf(dificultad.universe, [0.7, 1, 1])

# Definición de categorías para las variables
categorias = {
    'desnivel': ['bajo', 'medio', 'alto'],
    'longitud': ['corta', 'media', 'larga'],
    'terreno': ['estable', 'inestable'],
    'temperatura': ['frio', 'templado', 'calor']
}

from itertools import product

rules = []

# Generar reglas dinámicamente para todas las combinaciones
for desn, longi, terr, temp in product(categorias['desnivel'], categorias['longitud'], categorias['terreno'], categorias['temperatura']):
    # Define un criterio general para el nivel de dificultad
    if desn == 'alto' and longi == 'larga' and terr == 'inestable' and temp == 'calor':
        diff = 'muy_dificil'
    elif desn == 'bajo' and longi == 'corta' and terr == 'estable' and temp == 'templado':
        diff = 'muy_facil'
    elif terr == 'inestable' or temp == 'calor':
        diff = 'dificil'
    else:
        diff = 'facil'  # Default para combinaciones no específicas

    # Crea la regla y añádela a la lista
    rules.append(ctrl.Rule(
        desnivel[desn] & longitud[longi] & terreno[terr] & temperatura[temp],
        dificultad[diff]
    ))



# Sistema de control borroso
dificultad_ctrl = ctrl.ControlSystem(rules)
dificultad_sim = ctrl.ControlSystemSimulation(dificultad_ctrl)

# Función para calcular la dificultad
def calcular_dificultad(desnivel_val, longitud_val, terreno_val, temperatura_val):
    dificultad_sim.input['desnivel'] = desnivel_val
    dificultad_sim.input['longitud'] = longitud_val
    dificultad_sim.input['terreno'] = terreno_val
    dificultad_sim.input['temperatura'] = temperatura_val
    dificultad_sim.compute()
    return dificultad_sim.output['dificultad']

