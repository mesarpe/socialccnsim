#
from cache_manager import CacheManager
import logging

logging.basicConfig(filename='example.log',
    level=logging.DEBUG,
    format='%(asctime)-15s %(message)s'
)

class LCE(CacheManager):
    def __init__(self, cache_policy, cache_size, social_graph, topology, topology_manager, threshold = None):
        super(LCE, self).__init__(cache_policy, cache_size, social_graph, topology, topology_manager, threshold)
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
                self.store_cache(p, interest)

        return (content_found_caches, i)
