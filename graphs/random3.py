import networkx
import random as rnd

G = networkx.gnm_random_graph(10000, 10000*999/5)
while not networkx.algorithms.components.connected.is_connected(G):
    G = networkx.gnm_random_graph(10000, rnd.randint(3000, 10000*999/5))
