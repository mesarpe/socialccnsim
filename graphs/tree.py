import networkx

G = networkx.balanced_tree(2, 3)


# There will be no requests in the first three levels of the tree
for i in range(7):
    G.node[i]['wr'] = True
