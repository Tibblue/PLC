import networkx as nx
import matplotlib.pyplot as plt

def create_edges(lista):
    tam = len(lista)-1
    for i in range(tam):
        if 2*i+1 <= tam:
            G.add_edge(lista[i],lista[2*i+1])
        if 2*i+2 <= tam:
            G.add_edge(lista[i],lista[2*i+2])

lista = range(50)
G = nx.Graph()
G.add_nodes_from(lista)
create_edges(lista)
nx.draw_kamada_kawai(G, node_color='lime', node_size=500, with_labels=True)
plt.savefig("exemplo.png")