from algorithm.ranking.pagerank import PageRank
from algorithm.ranking.hits import HITS


class RankingFactory:
    """ Factory to create ranking algorithm instances dynamically """

    @staticmethod
    def get_ranking_algorithm(algorithm_type: str, **kwargs):
        """ Returns the appropriate ranking algorithm instance """
        if algorithm_type.lower() == "pagerank":
            return PageRank(**kwargs)
        elif algorithm_type.lower() == "hits":
            return HITS(**kwargs)
        else:
            raise ValueError(f"Unknown ranking algorithm: {algorithm_type}")
