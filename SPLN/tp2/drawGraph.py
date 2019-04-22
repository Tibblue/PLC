import networkx as nx
import matplotlib.pyplot as plt

triplos = [('Departamento', 'de', 21), ('Harry', 'Potter', 21), ('Harry', 'Luna', 22), ('Harry', 'Neville', 22), ('Harry', 'Magia', 24), ('Harry', 'Rua', 25), ('da', 'dos', 25), ('Percy', 'Harry', 25), ('das', 'da', 25), ('de', 'da', 25), ('Harry', 'nas', 26), ('Magia', 'de', 28), ('Harry', 'Jorge', 30), ('Harry', 'Ministério', 32), ('Harry', 'Fred', 33), ('Magia', 'Ministério', 33), ('Ministério', 'da', 38), ('Harry', 'de', 38), ('da', 'Magia', 46), ('Fred', 'Jorge', 48), ('Harry', 'Válter', 67), ('dos', 'Harry', 67), ('Harry', 'pela', 72), ('Harry', 'das', 73), ('da', 'Harry', 165)]

def get_nodes(triplos):
    set1 = set([t1 for t1,t2,n in triplos])
    set1.update([t2 for t1,t2,n in triplos])
    # print(set1) # debug
    return set1

def draw(nodes,edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edgesW)

    ### safe
    nx.draw_shell(G,with_labels=True)
    # pos=nx.get_node_attributes(G,'pos')
    # labels = nx.get_edge_attributes(G,'weight')
    # nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G),edge_labels=labels)

    ### experimental
    pos=nx.spring_layout(G)
    nx.draw(G,pos,with_labels=True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G),edge_labels=labels)

nodes = get_nodes(triplos)
edgesW = triplos
draw(nodes,edgesW)