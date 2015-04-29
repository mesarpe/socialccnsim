import networkx
import random

G = networkx.balanced_tree(2, 3)


# There will be no requests in the first three levels of the tree
#for i in range(7):
#    G.node[i]['wr'] = True

for i in random.sample(G.nodes(), len(G.nodes())/2):
    G.add_node(i, wc=True)
