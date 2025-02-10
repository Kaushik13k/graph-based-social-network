from graph.core.graph import Graph


class SocialNetworkOps:
    def __init__(self):
        self.graph = Graph(directed=True)

    def add_user(self, user_id: str, name: str, username: str, email: str, age: int) -> None:
        if not self.graph.has_node(user_id):
            self.graph.add_node(
                user_id,
                node_type="user",
                name=name,
                username=username,
                email=email,
                age=age,
                posts=[],
                connections=[]
            )
        else:
            print(f"User {user_id} already exists.")

    def add_post(self, user_id: str, post_id: str, title: str, content: str) -> None:
        if self.graph.has_node(user_id):
            user_node = self.graph.nodes[user_id]
            if user_node.node_type == "user":
                user_node.attributes["posts"].append(post_id)
                self.graph.add_node(
                    post_id,
                    node_type="post",
                    title=title,
                    content=content,
                    author=user_id,
                    likes=[]
                )
                self.graph.add_edge(user_id, post_id)
            else:
                print(f"{user_id} is not a valid user.")
        else:
            print(f"User {user_id} does not exist!")

    def add_connection(self, user1: str, user2: str) -> None:
        if self.graph.has_node(user1) and self.graph.has_node(user2):
            node1, node2 = self.graph.nodes[user1], self.graph.nodes[user2]

            if node1.node_type == "user" and node2.node_type == "user":
                if not self.graph.has_edge(user1, user2):
                    self.graph.add_edge(user1, user2)
            else:
                print("Connections can only be made between users.")
        else:
            print(f"One or both users do not exist.")

    def like_post(self, user_id: str, post_id: str) -> None:
        if self.graph.has_node(user_id) and self.graph.has_node(post_id):
            user_node, post_node = self.graph.nodes[user_id], self.graph.nodes[post_id]
            if user_node.node_type == "user" and post_node.node_type == "post":
                if user_id not in post_node.attributes["likes"]:
                    post_node.attributes["likes"].append(user_id)
                    self.graph.add_edge(user_id, post_id, edge_type="like")
            else:
                print("Invalid like operation. Users can only like posts.")
        else:
            print(f"Either User {user_id} or Post {post_id} does not exist.")

    def get_connections(self, user_id: str):
        if self.graph.has_node(user_id):
            return [
                neighbor for neighbor in self.graph.get_neighbors(user_id)
                if self.graph.nodes[neighbor].node_type == "user"
            ]
        return []

    def get_posts(self, user_id: str):
        if self.graph.has_node(user_id):
            return self.graph.nodes[user_id].attributes["posts"]
        return []

    def get_who_liked_post(self, post_id: str):
        if self.graph.has_node(post_id):
            return self.graph.nodes[post_id].attributes["likes"]
        return []

    def get_post_like_count(self, post_id: str):
        if self.graph.has_node(post_id):
            return len(self.graph.nodes[post_id].attributes["likes"])
        return 0

    def get_post_author(self, post_id: str):
        if self.graph.has_node(post_id):
            return self.graph.nodes[post_id].attributes.get("author", None)
        return None
