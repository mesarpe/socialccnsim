import networkx

def generate_facebook_graph(filename):
    # We generate the Facebook graph offere at http://snap.stanford.edu/data/egonets-Facebook.html
    # This is the script we used, taking information from .edges and .circles files
    g = networkx.Graph()
    files = ['0.edges', '1684.edges', '3437.edges', '414.edges', '698.edges', '107.edges', '1912.edges', '348.edges', '686.edges', '3980.edges']

    print len(files)

    for f in files:
        node = f.split('.')[0]
        print node
        content = file(f).read()
        lines = content.split('\n')
        for l in lines:
            if l != '':
                d = l.split(' ')
                g.add_edge(int(d[0]), int(d[1]))

                # The edges in the ego network for the node 'nodeId'. Edges are undirected for facebook, and directed (a follows b) for twitter and gplus. The 'ego' node does not appear, but it is assumed that they follow every node id that appears in this file.
                g.add_edge(int(node), int(d[0]))
                g.add_edge(int(node), int(d[1]))


    files = ['0.circles', '1684.circles', '3437.circles', '414.circles', '698.circles', '107.circles', '1912.circles', '348.circles', '686.circles', '3980.circles']

    circles = 0

    for f in files:
        node = f.split('.')[0]
        content = file(f).read()
        lines = content.split('\n')
        for l in lines:
            if l != '':
                nodes = l.split('\t')[1:]
                [g.add_edge(int(node), int(n)) for n in nodes]
                circles+=1

    # This is a simple check for the Diameter (longest shortest path)
    #max_ = -1
    #n = g.nodes()
    #for i in n:
    #    for j in n:
    #        m = networkx.shortest_path(g, i, j)
    #        if m > max_:
    #            max_ = m

    print len(g.nodes()), len(g.edges())
    print "is connected", networkx.is_connected(g)
    print "number of components", len(networkx.connected_components(g))
    print "circles", circles
    #print "diameter ( longest shortest path)", max_

    networkx.write_gml(g, filename)
    
#generate_facebook_graph('facebook.gml')

GG = networkx.read_gml('graphs/facebook.gml')

G=networkx.Graph()
for n,nbrs in GG.adjacency_iter():
   for nbr,edict in nbrs.items():
       G.add_edge(n,nbr)

