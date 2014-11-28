#

class CACHELESS(CacheManager):
    def _init_strategy(self):
        self.central_betweenness = networkx.algorithms.centrality.betweenness_centrality(topology)
    def _post_production(self):
        pass
    def retrieve_from_caches(self, interest, path):
        for i in range(0, len(path)):
            p = path[i]
            if self.caches[p].lookup(interest):
                self.stats.hit()
                break
            else:
                self.stats.miss()
                #stats.incr_accepted(self.caches[p].store(interest))
        self.stats.hops_walked(i, len(path)-1)
        
        #Cache in the node with the biggest central betweenness in the path
        max_v = -1
        node = None
        for i in range(0, len(path)):
            p = path[i]
            if self.central_betweenness[p] > max_v:
                max_v = self.central_betweenness[p]
                node = p
        
        self.stats.incr_accepted(self.caches[node].store(interest))
