import networkx

GG = networkx.read_gml('graphs/social_graph_hetrec2011_lastfm2.gml')

G=networkx.Graph()
for n,nbrs in GG.adjacency_iter():
   for nbr,edict in nbrs.items():
       G.add_edge(n,nbr)

