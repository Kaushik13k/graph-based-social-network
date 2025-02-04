from custom_graph.graph import Graph


class SocialNetwork:
    def __init__(self):
        self.graph = Graph()

    def add_user(self, user_id: str) -> None:
        self.graph.add_node(user_id, posts=[], connections=[])

    def add_connection(self, user1: str, user2: str):
        self.graph.add_edge(user1, user2)
        self.graph.nodes[user1]["connections"].append(user2)
        self.graph.nodes[user2]["connections"].append(user1)

    def add_post(self, user_id: str, post_id: str):
        self.graph.nodes[user_id]["posts"].append(post_id)

    def get_connections(self, user_id: str):
        return self.graph.nodes[user_id]["connections"]

    # TODO: Implement get_posts method
    def get_friends(self, user_id: str):
        return list(self.graph.get_neighbors(user_id))
