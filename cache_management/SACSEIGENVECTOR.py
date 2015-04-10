#
from cache_management.LCE import LCE
import networkx.algorithms.centrality
import numpy

class SACSEIGENVECTOR(LCE):
    def __init__(self, cache_policy, cache_size, social_graph, topology, topology_manager, threshold = None):
        super(SACSEIGENVECTOR, self).__init__(cache_policy, cache_size, social_graph, topology, topology_manager, threshold)
        self.eigenvector = networkx.algorithms.centrality.eigenvector_centrality(social_graph)
        self.threshold = numpy.average(self.eigenvector.values())
    def _post_production(self, content_name, social_publisher):
        if self.eigenvector[social_publisher] > self.threshold:
            # In all the cache path
            for social_neighbour in self.social_graph.neighbors(social_publisher):
                path = self.topology_manager.get_path(
                            social_publisher,
                            social_neighbour
                )
                [self.store_cache(p, content_name) for p in path]

