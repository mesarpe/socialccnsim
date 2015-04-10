# Works only with CCN network
from cache_manager import CacheManager
import random

class PROBCACHE(CacheManager):

    def retrieve_from_caches(self, interest, path):
        content_found_caches = False

        for i in range(0, len(path)):
            p = path[i]
            if self.lookup_cache(p, interest):
                content_found_caches = True
                break
            else:
                # Cache with a probability inversily proportional to the distance from the requester.
                if random.randint(0, i) == 0:
                    self.store_cache(p, interest)

        return (content_found_caches, i)
