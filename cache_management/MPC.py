#
from cache_manager import CacheManager

class MPC(CacheManager):
    def _init_strategy(self):
        self.mpc = {}
        for node in self.topology.nodes():
            self.mpc[node] = {}
    def retrieve_from_caches(self, interest, path):
        for i in range(0, len(path)):
            p = path[i]

            try:
                self.mpc[p][interest]+=1
            except:
                self.mpc[p][interest] = 1

            if self.lookup_cache(p, interest):
                break
            else:
                pass

            if self.mpc[p][interest] >= 2:
                #if i == 0:
                #    self.stats.incr_accepted(self.caches[p].store(interest))
                neighbors = self.topology_manager.topology.neighbors(p)
                for n in neighbors:
                    self.stats.incr_accepted(self.caches[n].store(interest))
                self.mpc[p][interest] = 0
                
        return i
