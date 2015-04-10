#Leave Copy on the Edge Cache Manager
from cache_manager import CacheManager

#getattr(getattr(__import__('cache_management.LCEdgeCM'), 'LCEdgeCM'), 'LCEDGE')

class LCEDGE(CacheManager):
    def retrieve_from_caches(self, interest, path):
        content_found_caches = False

        for i in range(0, len(path)):
            p = path[i]
            if self.lookup_cache(p, interest):
                content_found_caches = True
                break
            else:
                pass

        # In anycase, we put a copy in the first cacheable element
        first = 0
        while first < len(path)-1 and not self.topology_manager.has_caching_capabilities(path[first]):
            first += 1
        if first < i: #Only if the element is placed before the original requester
            self.store_cache(path[first], interest)
            

        return (content_found_caches, i)
