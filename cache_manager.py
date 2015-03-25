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
import networkx
import numpy
import random
import re

import externmodules.community

from statistics import Stats, GeneralStats

class CacheManager(object):
    def _init_strategy(self):
        pass
    def __init__(self, cache_policy, cache_size, social_graph, topology, topology_manager, threshold = None):
        self.cache_policy = cache_policy
        res = re.match('((?P<name>[a-zA-Z0-9_]*)(\((?P<params>([0-9]*\.?[0-9]*,? ?)*)\))?)', cache_policy)
        assert res != None
        self.cache_policy = res.group('name')
        try:
            self.cache_policy_params = [float(r) for r in res.group('params').split(',')]
        except AttributeError:
            self.cache_policy_params = []
        
        self.social_graph = social_graph
        self.CACHE_SIZE = cache_size

        self.topology_manager = topology_manager
        self.topology = topology

        self.stats = Stats()

        self.caches = {}
        self.prepare_caches(cache_size)

        ## INItIALIZE PRODUCER POLICY
        self._init_strategy()

    def prepare_caches(self, cache_size):
        ### REPLACEMENT POLICIES ##############################################
        #if cache_policy in ['subset_influentials', 'subset_noninfluentials']:
        #    #recorremos todos los nodos, nos fijamos cuales caen y extramos los amigos del subgrafo social
        #    if cache_policy == 'subset_influentials':
        #        n_ = [n for n in social_graph.nodes() if pagerank[n] > threshold]
        #    elif cache_policy == 'subset_noninfluentials':
        #        n_ = [n for n in social_graph.nodes() if pagerank[n] <= threshold]

        #    nodes_ = {}
        #    for n in n_:
        #        nodes_[str(n)] = n

        #    for node in self.topology.nodes():
        #        self.caches[node] = SubsetCache(cache_size, subset = nodes_)

        #elif cache_policy in ['subset_community2']:
        #    partition = externmodules.community.best_partition(self.social_graph)
            
        #    for node in topology.nodes():
        #        users_in_node = [n for n in social_graph.nodes() if topology_manager[n] == node]
        #        for vecino in networkx.neighbors(topology, node):
        #            users_in_node += [n for n in social_graph.nodes() if topology_manager[n] == vecino]
                
        #        self.caches[node] = CommunitySubsetCache(
        #            cache_size,
        #            users = users_in_node,
        #            node_in_the_topology = node,
        #            partition = partition
        #        )

        #elif cache_policy in ['specialsemantic2']:
        #    for node in topology.nodes():
        #        self.caches[node] = SemanticCache2(cache_size, [0.5, 20, 100000])
        #    self.caches[node] = SemanticCache3(cache_size, [0.5, 20, 100000])
        ### END REPLACEMENT POLICIES ##########################################
        rp = getattr(getattr(__import__('replacement_policies.%s'%self.cache_policy), self.cache_policy), self.cache_policy)
        for node in self.topology.nodes():
            self.caches[node] = rp(cache_size)#, self.cache_policy_params)

    def post_production(self, content_name, social_publisher):
        self._post_production(content_name, social_publisher)

    def _post_production(self, content_name, social_publisher):
        """Function to be overloaded"""
        pass

    def __getitem__(self, key):
        return self.caches[key]
    def values(self):
        return self.caches.values()

    #TODO: change function name
    def retrieve_from_caches(self, interest, path):
        """Function to be overloaded"""
        raise Exception('This function should never be called: retrieve_from_caches')

    def lookup_cache(self, node, interest):
        """Wrapper to lookup in the caches
        """
        res = self.caches[p].lookup(interest):
        if res:
            self.stats.hit()
        else:
            self.stats.miss()
        return res

    #REFACTORING OF THIS!
    def incr_publish(self):
        return self.stats.incr_publish()
    def incr_interest(self):
        return self.stats.incr_interest()
    def stats_summary(self):
        return self.stats.summary(self.caches)

