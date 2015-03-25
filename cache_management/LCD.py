#
from cache_manager import CacheManager

class LCD(CacheManager):
    def retrieve_from_caches(self, interest, path):
        for i in range(0, len(path)):
            p = path[i]
            if self.lookup_cache(p, interest):
                # move copy down
                if i>0:
                    self.stats.incr_accepted(self.caches[path[i-1]].store(interest))
                break
            else:
                pass
        if i + 1 == len(path):
            self.stats.incr_accepted(self.caches[p].store(interest))

        return i
