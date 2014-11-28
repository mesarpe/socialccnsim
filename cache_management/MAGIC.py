#Leave Copy on the Edge Cache Manager
from cache_manager import CacheManager

class MAGIC(CacheManager):
    def _init_strategy(self):
        self.r_m_v = {}
        for node in self.topology.nodes():
            self.r_m_v[node] = {}
            self.r_m_v[node]['sum'] = 0

    def retrieve_from_caches(self, interest, path):
        len_path = len(path)
    
        max_gain = 0
        max_gain_index = -1
        rep_penalty = {}

        for i in range(0, len_path):
            p = path[i]

            if not self.r_m_v[p].has_key(interest):
                self.r_m_v[p][interest] = 0
            self.r_m_v[p][interest] +=1
            self.r_m_v[p]['sum'] +=1

            h_m_v = len_path - i
            # calculate replace penalty in the node p
            min_ = "inf"
            min_index = -1
            if len(self.caches[p]) == self.CACHE_SIZE:
                for e in self.caches[p].keys():
                    local_gain = self.r_m_v[p][e] * h_m_v
                    if local_gain < min_:
                        min_ = local_gain
                        min_index = e
                assert min_ != "inf"
                rep_penalty[p] = min_index
            elif len(self.caches[p]) < self.CACHE_SIZE:
                min_ = 0
                rep_penalty[p] = min_
            else:
                raise Exception("Cache has more than X elements.")

            # calculate place gain
            place_gain = self.r_m_v[p][interest] * h_m_v
            local_gain = place_gain - min_ # place gain - replace penalty

            # then we get the max
            if local_gain > max_gain:
                max_gain = local_gain
                max_gain_index = i

        for i in range(0, len_path):
            p = path[i]
            
            if self.caches[p].lookup(interest):
                self.stats.hit()
                break
            else:
                self.stats.miss()
                # if the cache is not filled or we store 
                if len(self.caches[p]) < self.CACHE_SIZE:
                    self.stats.incr_accepted(self.caches[p].store(interest))
                elif max_gain_index == i:
                    self.caches[p].remove(rep_penalty[p])
                    self.stats.incr_accepted(self.caches[p].store(interest))
        
        
        self.stats.hops_walked(i, len(path)-1)
