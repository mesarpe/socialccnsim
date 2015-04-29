#
from cache_manager import CacheManager

from replacement_policies.Cache import Cache

class TWOLRU(CacheManager):
    def __init__(self, cache_policy, cache_size, social_graph, topology, topology_manager, threshold = None):
        super(TWOLRU, self).__init__(cache_policy, cache_size, social_graph, topology, topology_manager, threshold)

        self.second_cache = {}
        for node in self.topology.nodes():
            self.second_cache[node] = Cache(cache_size)

    def _init_strategy(self):
        pass
    def retrieve_from_caches(self, interest, path):
        
        content_found_caches = False

        for i in range(0, len(path)):
            p = path[i]
            if self.lookup_cache(p, interest):
                content_found_caches = True
                break
            else:
                if self.second_cache[p].lookup(interest):
                    self.store_cache(p, interest)
                else:
                    self.second_cache[p].store(interest)

        return (content_found_caches, i)
