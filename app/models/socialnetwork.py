from graph.core.graph import Graph


class SocialNetworkOps:
    def __init__(self):
        self.graph = Graph(directed=True)

    def add_user(self, user_id: str, username: str, name: str, email: str, age: int, place: str) -> None:
        if not self.graph.has_node(username):
            self.graph.add_node(
                username,
                node_type="user",
                user_id=user_id,
                name=name,
                email=email,
                age=age,
                place=place,
                posts=[],
                connections=[]
            )
        else:
            print(f"User {username} already exists.")

    def add_post(self, username: str, post_id: str, title: str, content: str) -> None:
        if self.graph.has_node(username):
            user_node = self.graph.nodes[username]
            if user_node.node_type == "user":
                user_node.attributes["posts"].append(post_id)
                self.graph.add_node(
                    post_id,
                    node_type="post",
                    title=title,
                    content=content,
                    author=username,
                    likes=[]
                )
                self.graph.add_edge(username, post_id)
            else:
                print(f"{username} is not a valid user.")
        else:
            print(f"User {username} does not exist!")

    def add_connection(self, username1: str, username2: str) -> None:
        if self.graph.has_node(username1) and self.graph.has_node(username2):
            node1, node2 = self.graph.nodes[username1], self.graph.nodes[username2]

            if node1.node_type == "user" and node2.node_type == "user":
                if not self.graph.has_edge(username1, username2):
                    self.graph.add_edge(username1, username2)
            else:
                print("Connections can only be made between users.")
        else:
            print(f"One or both users do not exist.")

    def like_post(self, username: str, post_id: str) -> None:
        if self.graph.has_node(username) and self.graph.has_node(post_id):
            user_node, post_node = self.graph.nodes[username], self.graph.nodes[post_id]
            if user_node.node_type == "user" and post_node.node_type == "post":
                if username not in post_node.attributes["likes"]:
                    post_node.attributes["likes"].append(username)
                    self.graph.add_edge(username, post_id, edge_type="like")
            else:
                print("Invalid like operation. Users can only like posts.")
        else:
            print(f"Either User {username} or Post {post_id} does not exist.")

    def get_connections(self, username: str):
        if self.graph.has_node(username):
            return [
                neighbor for neighbor in self.graph.get_neighbors(username)
                if self.graph.nodes[neighbor].node_type == "user"
            ]
        return []

    def get_posts(self, username: str):
        if self.graph.has_node(username):
            return self.graph.nodes[username].attributes["posts"]
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
