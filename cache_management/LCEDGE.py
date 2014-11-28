#Leave Copy on the Edge Cache Manager
from cache_manager import CacheManager

#getattr(getattr(__import__('cache_management.LCEdgeCM'), 'LCEdgeCM'), 'LCEDGE')

class LCEDGE(CacheManager):
    def retrieve_from_caches(self, interest, path):
        for i in range(0, len(path)):
            p = path[i]
            if self.caches[p].lookup(interest):
                self.stats.hit()
                break
            else:
                self.stats.miss()
        # In case, content is found in the first element, we don't cache it again.
        if i != 0:
            self.stats.incr_accepted(self.caches[path[0]].store(interest))
        self.stats.hops_walked(i, len(path)-1)
