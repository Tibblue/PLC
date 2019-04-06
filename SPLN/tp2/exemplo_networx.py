import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# add nodes
G.add_node('Batatas')
G.add_nodes_from(range(1,10))

# remove nodes
G.remove_node('Batatas')
G.remove_nodes_from([(1,2),(2,3)])

# add and remove edges
G.add_edge(5,100)
G.remove_edge(5,100)

G.add_weighted_edges_from([(0,1,3.0),(1,4,7.5)])
G.add_path([1,2,3])

nx.draw(G,with_labels=True)
nx.draw(G)
plt.show()