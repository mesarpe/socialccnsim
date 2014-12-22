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

class RNDFORWARD8(CacheManager):
    """
    Hash-routing scheme
    """
    def calculate_hash(self, message):
        """
        lose lose algorithm
        """
        _hash = 0
        for c in message:
            _hash = ord(c) + (_hash << 6) + (_hash << 16) - _hash

        return _hash
    def retrieve_from_caches(self, interest, path):
        r = self.calculate_hash(interest) % 8
        
        path = [1,2+r,0]

        for i in range(0, len(path)):
            p = path[i]
            if self.caches[p].lookup(interest):
                self.stats.hit()
                break
            else:
                self.stats.miss()
                self.stats.incr_accepted(self.caches[p].store(interest))

        return i
