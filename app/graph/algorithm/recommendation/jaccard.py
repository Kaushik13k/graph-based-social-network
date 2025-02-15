from core.graph import Graph
from typing import Any, Dict
from algorithm.recommendation.base import RecommendationStrategy


class JaccardSimilarity(RecommendationStrategy):
    def recommend(self, graph: Graph, user: Any) -> Dict[Any, float]:
        if user not in graph.nodes:
            raise ValueError(f"User {user} not found in the graph.")

        recommendations = {}

        user_friends = set(graph.get_neighbors(user))
        for other_user in graph.nodes:
            if other_user != user:
                other_friends = set(graph.get_neighbors(other_user))

                intersection = len(user_friends.intersection(other_friends))
                union = len(user_friends.union(other_friends))

                similarity_score = intersection / union if union != 0 else 0.0
                recommendations[other_user] = similarity_score

        return dict(sorted(recommendations.items(), key=lambda x: x[1], reverse=True))
