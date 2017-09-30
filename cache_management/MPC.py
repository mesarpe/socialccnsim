#
from cache_manager import CacheManager

class MPC(CacheManager):
    MPC_THRESHOLD = 10
    RESET_VALUE = 0
    
    def _init_strategy(self):
        self.mpc = {}
        for node in self.topology.nodes():
            self.mpc[node] = {}
    def retrieve_from_caches(self, interest, path):
        content_found_caches = False

        for i in range(0, len(path)):
            p = path[i]

            try:
                self.mpc[p][interest]+=1
            except:
                self.mpc[p][interest] = 1

            if self.caches[p].lookup(interest):
                content_found_caches = True
                self.stats.hit()
                break
            else:
                self.stats.miss()

        if not content_found_caches:
            self.store_cache(path[len(path)-1], interest)
        if content_found_caches and self.mpc[p][interest] >= self.MPC_THRESHOLD:

            neighbors = self.topology_manager.topology.neighbors(p)
            for n in neighbors:
                if self.topology_manager.has_caching_capabilities(n):
                    self.store_cache(n, interest)
            self.mpc[p][interest] = self.RESET_VALUE
                
        return (content_found_caches, i)
