import networkx

G = networkx.Graph()

# 0: F
# 1: C
# 2: J
# 3: M
# 4: I
# 5: Th
# 6: A

G.add_edge(0, 1)
G.add_edge(0, 3)
G.add_edge(0, 5)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 5)
G.add_edge(4, 5)
G.add_edge(5, 6)
