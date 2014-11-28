#####################################################################
#SocialCCNSim, a simulator of caches for Content Centric Networking.
#
#Developed by Cesar A. Bernardini Copyright (C) 2014.
#This library is free software; you can redistribute it and/or
#modify it under the terms of the GNU Library General Public
#License as published by the Free Software Foundation; either
#version 2 of the License, or (at your option) any later version.
#
#This library is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#Library General Public License for more details.
#
#You should have received a copy of the GNU Library General Public
#License along with this library; if not, write to the
#Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
#Boston, MA  02110-1301, USA. 
#
#####################################################################
#
from cache_manager import CacheManager
from externmodules.semantic.virtuoso_webservice import SemanticService

class SEMANTIC(CacheManager):
    def _init_strategy(self):
        eq = [
                "0 0 0 0 0 0 0 0 0 0 0", "0 1 1 1 0 0 1 0 0 0 0", "0 0 1 1 0 0 1 0 0 0 0",
                "0 0 1 0 0 0 1 0 0 0 0", "0 0 1 1 0 0 1 1 0 0 0", "0 0 1 1 0 0 1 0 0 0 1",
                "0 0 1 1 0 0 0 0 0 0 0", "0 0 1 0 0 0 0 0 0 0 0", "0 1 1 1 0 0 1 1 0 0 0",
                "0 1 1 1 0 0 1 0 0 0 1", "0 0 1 0 0 0 1 0 0 0 1", "1 0 1 1 0 0 1 0 0 0 0",
                "0 1 1 1 0 0 0 0 0 0 0", "0 0 1 1 0 0 1 1 0 0 1", "1 0 1 1 0 0 1 0 0 0 1",
                "1 1 1 1 0 0 1 0 0 0 0", "0 1 1 1 0 0 1 1 0 0 1", "0 1 1 0 0 0 0 0 0 0 0",
                "0 0 1 0 0 0 1 1 0 0 0", "0 0 1 1 0 1 1 1 0 0 0", "1 1 1 1 0 0 1 0 0 0 1",
                "0 0 0 1 0 0 0 0 0 0 0", "0 1 1 1 0 0 1 0 1 0 0", "0 1 1 1 0 0 1 1 1 1 0",
                "0 0 0 0 0 0 1 0 0 0 0", "0 1 1 0 0 0 1 0 0 0 0", "0 1 0 1 0 0 1 0 0 0 0",
                "0 0 1 1 0 0 1 1 1 1 0", "1 0 1 1 0 0 1 1 0 0 0", "1 0 1 1 0 0 1 1 1 0 0",
                "0 0 0 1 0 0 1 0 0 0 0", "0 1 1 1 0 0 1 1 1 0 0", "0 0 1 1 0 0 0 0 0 0 1",
                "0 0 0 0 0 0 0 0 0 0 1", "0 0 1 0 0 0 0 0 0 0 1", "1 0 1 1 0 0 1 1 0 0 1",
                "0 0 1 1 0 0 1 0 0 1 0", "1 1 0 1 0 0 1 0 0 0 0", "0 1 1 0 0 0 1 0 0 0 1",
                "0 0 1 1 1 0 1 0 0 0 0"
        ]
        self.SEMANTIC_SPLIT=3
        self.eq_g = []
        for r in range(0, self.SEMANTIC_SPLIT):
            self.eq_g.append([eq[i] for i in range(r, len(eq), self.SEMANTIC_SPLIT) ])
        
        #eq_odd = [eq[i] for i in range(0, len(eq), 2) ]

        self.semantic_service = SemanticService([0.5, 20, 100000])
    def retrieve_from_caches(self, interest, path):
        fv = self.semantic_service.get_features_vector(interest)
        for r in range(0, self.SEMANTIC_SPLIT):
            if fv in self.eq_g[r]:
                break
        
        path = [1,2+r,0]

        for i in range(0, len(path)):
            p = path[i]
            if self.caches[p].lookup(interest):
                self.stats.hit()
                break
            else:
                self.stats.miss()
                self.stats.incr_accepted(self.caches[p].store(interest))
        self.stats.hops_walked(i, len(path)-1)
