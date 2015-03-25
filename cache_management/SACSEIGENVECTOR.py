#
from cache_management.LCE import LCE
import networkx.algorithms.centrality

class SACSEIGENVECTOR(LCE):
    def _init_strategy(self):
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
                [self.stats.incr_accepted(self.caches[p].store(content_name)) for p in path]

