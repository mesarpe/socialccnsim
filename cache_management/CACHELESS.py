#
from cache_manager import CacheManager
import networkx

class CACHELESS(CacheManager):
    def _init_strategy(self):
        self.central_betweenness = networkx.algorithms.centrality.betweenness_centrality(self.topology)
    def retrieve_from_caches(self, interest, path):
        content_found_caches = False

        for i in range(0, len(path)):
            p = path[i]
            if self.lookup_cache(p, interest):
                content_found_caches = True
                break
            else:
                pass

        
        #Cache in the node with the biggest central betweenness in the path
        max_v = -1
        node = None
        for i in range(0, len(path)):
            p = path[i]
            if self.central_betweenness[p] > max_v:
                max_v = self.central_betweenness[p]
                node = p
        
        self.store_cache(node, interest)

        return (content_found_caches, i)
