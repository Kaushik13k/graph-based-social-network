from algorithm.recommendation.jaccard import JaccardSimilarity


class RecommendationFactory:

    @staticmethod
    def get_recommendation_algorithm(algorithm_type: str):
        if algorithm_type.lower() == "jaccard":
            return JaccardSimilarity()
        else:
            raise ValueError(f"Unknown recommendation algorithm: {
                             algorithm_type}")
