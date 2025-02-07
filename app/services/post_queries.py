import uuid
from configs.graph_db import DatabaseConnection


class PostRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def create(self, title: str, content: str, timestamp: str, email: str):
        post_id: str = uuid.uuid4().hex

        query = """
        MATCH (u:User {email: $email})
        CREATE (p:Post {id: $post_id, title: $title, content: $content, timestamp: $timestamp})
        MERGE (u)-[:POSTED]->(p)
        RETURN p
        """
        return self.db.execute_query(query, {"post_id": post_id, "title": title, "content": content, "timestamp": timestamp, "email": email})

    def posts(self):
        query = "MATCH (p:Post) RETURN p.id, p.content, p.timestamp"
        return self.db.execute_query(query)

    def delete(self, title: str):
        query = """
        MATCH (p:Post {title: $title})
        DETACH DELETE p
        """
        return self.db.execute_query(query, {"title": title})
