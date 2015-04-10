#
import networkx
import numpy
from cache_manager import CacheManager
from cache_management.LCE import LCE

class SACSPAGERANK(LCE):
    def __init__(self, cache_policy, cache_size, social_graph, topology, topology_manager, threshold = None):
        super(SACSPAGERANK, self).__init__(cache_policy, cache_size, social_graph, topology, topology_manager, threshold)
        self.pagerank = networkx.algorithms.link_analysis.pagerank_alg.pagerank(social_graph)
        self.threshold = numpy.average(self.pagerank.values())

    def _post_production(self, content_name, social_publisher):
        if self.pagerank[social_publisher] > self.threshold:
            # In all the cache path
            for social_neighbour in self.social_graph.neighbors(social_publisher):
                path = self.topology_manager.get_path(
                            social_publisher,
                            social_neighbour
                )
                [self.store_cache(p, content_name) for p in path]

