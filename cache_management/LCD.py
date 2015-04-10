#
from cache_manager import CacheManager

class LCD(CacheManager):
    def get_next_node(self, last, path):
        next = last
        while next >= 0 and not self.topology_manager.has_caching_capabilities(path[next]):
            next -= 1
        return next

    def retrieve_from_caches(self, interest, path):
        content_found_caches = False

        for i in range(0, len(path)):
            p = path[i]
            if self.lookup_cache(p, interest):
                # move copy down
                content_found_caches = True
                break
            else:
                pass

        # In case we arrive to the last element of the path, we store the element in the last.
        if content_found_caches:
            next = self.get_next_node(i-1, path)
            if next >= 0:
                self.store_cache(path[next], interest)

        else: # content not found in the cache => We put a copy in the last cache of the path
            
            next = self.get_next_node(i, path)
            if next >= 0:
                self.store_cache(path[next], interest)

        return (content_found_caches, i)
