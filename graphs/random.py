import networkx

G = networkx.gnm_random_graph(100, 100*99/5)
while not networkx.algorithms.components.connected.is_connected(G):
    G = networkx.gnm_random_graph(100, random.randint(300, 100*99/5))
