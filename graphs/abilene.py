import networkx
#Baseline scenarios: telematics.poliba.it/icn-baseline-scenarios
G = networkx.Graph()

G.add_edge(0, 1)
G.add_edge(0, 10)
G.add_edge(1, 10)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(2, 8)
G.add_edge(3, 4)
G.add_edge(3, 7)
G.add_edge(4, 5)
G.add_edge(5, 6)
G.add_edge(6, 7)
G.add_edge(7, 8)
G.add_edge(8, 9)
G.add_edge(9, 10)

