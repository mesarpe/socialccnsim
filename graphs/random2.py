import networkx

G = networkx.gnm_random_graph(3000, 1000*99/5)
while not networkx.algorithms.components.connected.is_connected(G):
    G = networkx.gnm_random_graph(3000, random.randint(300, 1000*99/5))
