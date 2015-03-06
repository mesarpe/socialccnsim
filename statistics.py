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
import threading
import numpy

class GeneralStats():
    def __init__(self):
        self.lock = threading.Lock()
        self.lock.acquire()
        self._cache_hit = []
        self._stretch = []
        self._hops_reduction = []
        self.expired_elements = []
        self.diversity = []
        self.acceptance_ratio = []
        self.lock.release()
    def append(self, cache_hit, stretch, hops_reduction, expired_elements, diversity, acceptance_ratio):
        self.lock.acquire()
        self._cache_hit.append(cache_hit)
        self._stretch.append(stretch)
        self._hops_reduction.append(hops_reduction)
        self.expired_elements.append(expired_elements)
        self.diversity.append(diversity)
        self.acceptance_ratio.append(acceptance_ratio)
        self.lock.release()
    def summary(self):
        self.lock.acquire()
        res = "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15}".format(numpy.average(self._cache_hit), numpy.average(self._stretch), numpy.average(self._hops_reduction), numpy.average(self.expired_elements), numpy.average(self.diversity), numpy.average(self.acceptance_ratio), numpy.average(self._w), numpy.average(self._interest), numpy.std(self._cache_hit), numpy.std(self._stretch), numpy.std(self._hops_reduction), numpy.std(self.expired_elements), numpy.std(self.diversity), numpy.std(self.acceptance_ratio), numpy.std(self._w), numpy.std(self._interest))
        #print numpy.std(self._cache_hit), numpy.std(self._stretch), numpy.std(self._hops_reduction)
        self.lock.release()
        return res
            
class Stats():
    def __init__(self):
        self.lock = threading.Lock()
        self.lock.acquire()
        self._miss = 0
        self._hit = 0
        self._increase_messages = 0
        self._interest = 0
        self._publish = 0
        self._distance = 0
        self._hops_walked = 0
        self._hops_hits = 0

        # number of requests issued by end-users satisfied by caches
        self._w = 0

        self.accepted = 0
        self.rejected = 0
        self.lock.release()
    def increase_messages(self):
        self._increase_messages+=1
        return self._increase_messages
    def hit(self):
        self.lock.acquire()
        self._hit+=1
        self.lock.release()
    def miss(self):
        self.lock.acquire()
        self._miss+=1
        self.lock.release()
    def incr_w(self):
        self.lock.acquire()
        self._w += 1
        self.lock.release()
    def incr_interest(self):
        self.lock.acquire()
        self._interest += 1
        self.lock.release()
    def incr_publish(self):
        self.lock.acquire()
        self._publish += 1
        self.lock.release()
    def incr_accepted(self, value):
        self.lock.acquire()
        if value:
            self.accepted +=1
        else:
            self.rejected +=1
        self.lock.release()
    def hops_walked(self, hops_walked, distance):
        #Hop reduction is the ratio
        # between the total number of the hops of cache hits and
        # the total number of the hops of all accesses
        self.lock.acquire()
        self._hops_walked += hops_walked
        if hops_walked < distance:
            self._hops_hits += hops_walked
            self._w += 1
        elif hops_walked == distance:
            self._hops_hist += hops_walked
        elif hops_walked > distance:
            assert hops_walked > distance
        self._distance += distance
        self.lock.release()

    def get_acceptance_ratio(self):
        return self.accepted / (self.accepted + self.rejected)

    def get_expired_elements(self, last_interest, caches): # Get the ratio of expired elements saved into the cache
        list_last_interest = []
        for k, v in last_interest.items():
            list_last_interest.append(str('/friend%s/%s'%(k, v)))

        #print list_last_interest        
        expired_elements = 0
        total_elements = 0
        for cache in caches.values():
            for name in cache:
                if not name in list_last_interest:
                    expired_elements+=1
            total_elements += len(cache)

        
        return expired_elements/float(total_elements)

    def get_diversity(self, caches):
        total_elements = 0
        diff_elements = set()
        for cache in caches.values():
            for content_name in cache:
                diff_elements.add(content_name)
            total_elements+=len(cache)
        return len(diff_elements)/float(total_elements)

    def get_caching_operations(self):
        self.lock.acquire()
        res = self.accepted + self.rejected
        self.lock.release()
        return res
    def get_eviction_operations(self):
        return self.accepted
    def get_cache_hit(self):
        self.lock.acquire()
        res = self._hit/float(self._miss+self._hit)
        self.lock.release()
        return res
    def get_stretch(self):
        self.lock.acquire()
        if self._distance == 0:
            res = 0.0
        else:
            res = self._hops_walked/float(self._distance)
        self.lock.release()
        return res
    def get_hops_reduction(self):
        self.lock.acquire()
        if self._hops_walked == 0:
            res = 0
        else:
            res = self._hops_hits/float(self._hops_walked)
        self.lock.release()
        return res

    def summary(self, caches):
        #print "Hit: %d. Miss: %d. Global Cache Hit: %2f"%(self._hit, self._miss, self._hit/float(self._miss+self._hit))
        #print "Interest: %d. Published Data: %d"%(self._interest, self._publish)
        #Just global hit        
        res = "{0} {1} {2} {3} {4} {5} {6} {7}".format(self.get_cache_hit(), self.get_stretch(), self.get_hops_reduction(), self.get_diversity(caches), self.get_caching_operations(), self.get_eviction_operations(), self._w, self._interest)
        return res

    def comparison_against_ip_summary(self):
        #mathematical approximation
        hops_route_std = 3
        print "%d, %d"%(hops_route_std*self._interest*2, self._miss+self._hit)

