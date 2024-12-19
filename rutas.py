import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo_rutas():
    # Crear un grafo vacío
    grafo = nx.Graph()

    # Agregar nodos (representando puntos clave)
    grafo.add_node("Inicio", pos=(0, 0))
    grafo.add_node("Punto_A", pos=(2, 2))
    grafo.add_node("Punto_B", pos=(4, 1))
    grafo.add_node("Destino", pos=(6, 3))

    # Agregar aristas con pesos
    grafo.add_edge("Inicio", "Punto_A", peso=1, etiqueta="Fácil")
    grafo.add_edge("Punto_A", "Punto_B", peso=3, etiqueta="Difícil")
    grafo.add_edge("Punto_B", "Destino", peso=2, etiqueta="Moderada")
    grafo.add_edge("Inicio", "Punto_B", peso=4, etiqueta="Difícil")

    return grafo

def dibujar_grafo(grafo):
    pos = nx.get_node_attributes(grafo, 'pos')  # Recuperar posiciones de los nodos
    labels = nx.get_edge_attributes(grafo, 'etiqueta')  # Recuperar etiquetas de aristas

    # Dibujar nodos y aristas
    nx.draw(grafo, pos, with_labels=True, node_size=2000, node_color="lightblue")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)

    plt.title("Grafo de Rutas")
    plt.show()
