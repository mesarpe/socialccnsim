#
from cache_manager import CacheManager
from cache_management.LCE import LCE

class SACSPAGERANK(LCE):
    def _init_strategy(self):
        self.pagerank = networkx.algorithms.link_analysis.pagerank_alg.pagerank(social_graph)
        self.threshold = numpy.average(self.pagerank.values())

    def _post_production(self, content_name, social_publisher, paths):
        if self.pagerank[social_publisher] > self.threshold:
            # In all the cache path
            for social_neighbour in self.social_graph.neighbors(social_publisher):
                path = self.topology_manager.get_path(
                            social_publisher,
                            social_neighbour
                )
                [self.stats.incr_accepted(self.caches[p].store(content_name)) for p in path]

