#
from cache_manager import CacheManager
import random

class PROBCACHE(CacheManager):

    def retrieve_from_caches(self, interest, path):
        for i in range(0, len(path)):
            p = path[i]
            if self.caches[p].lookup(interest):
                self.stats.hit()
                break
            else:
                self.stats.miss()
                # Cache with a probability inversily proportional to the distance from the requester.
                if random.randint(0, i) == 0:
                    self.stats.incr_accepted(self.caches[p].store(interest))
        self.stats.hops_walked(i, len(path)-1)
