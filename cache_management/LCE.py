#
from cache_manager import CacheManager

class LCE(CacheManager):
    def __init__(self, cache_policy, cache_size, social_graph, topology, topology_manager, threshold = None):
        super(LCE, self).__init__(cache_policy, cache_size, social_graph, topology, topology_manager, threshold)
    def _init_strategy(self):
        pass
    def retrieve_from_caches(self, interest, path):
        for i in range(0, len(path)):
            p = path[i]
            if self.caches[p].lookup(interest):
                self.stats.hit()
                break
            else:
                self.stats.miss()
                self.stats.incr_accepted(self.caches[p].store(interest))
        self.stats.hops_walked(i, len(path)-1)
