import networkx

GG = networkx.read_gml('graphs/inet_test3037.gml')
G=networkx.Graph()
for n,nbrs in GG.adjacency_iter():
   for nbr,edict in nbrs.items():
       G.add_edge(n,nbr)
