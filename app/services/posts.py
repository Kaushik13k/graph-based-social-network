from typing import List, Dict
from schemas.posts import PostSchema
from configs.graph_db import DatabaseConnection
from exceptions.exceptions import PostNotFoundException


class PostService:
    def __init__(self):
        self.db = DatabaseConnection()

    def create(self, post: PostSchema) -> Dict:
        check_query = """
        MATCH (p:Post {title: $title}) 
        RETURN p
        """
        create_query = """
        MATCH (u:User {user_name: $user_name})
        CREATE (p:Post {id: $post_id, title: $title, content: $content, timestamp: $timestamp})
        MERGE (u)-[:POSTED]->(p)
        WITH p
        UNWIND $hashtags AS tag_name
        MERGE (h:Hashtag {name: tag_name})
        MERGE (p)-[:HAS_TAG]->(h)
        RETURN p
        """
        try:
            existing_post = self.db.execute_query(
                check_query, {"title": post.title})

            if existing_post:
                return {"error": "A post with this title already exists."}

            return self.db.execute_query(create_query, post.model_dump())

        except Exception as e:
            raise Exception(f"Error creating post: {str(e)}")

    def get(self) -> List[Dict]:
        query = "MATCH (p:Post) RETURN p.id AS id, p.title AS title, p.content AS content, p.timestamp AS timestamp"
        try:
            return list(self.db.execute_query(query))
        except Exception as e:
            raise Exception(f"Error fetching posts: {str(e)}")

    def search_hashtag(self, hashtag: str) -> List[Dict]:
        query = """
        MATCH (p:Post)-[:HAS_TAG]->(h:Hashtag {name: $hashtag})
        RETURN p.id AS id, p.title AS title, p.content AS content, p.timestamp AS timestamp
        """
        try:
            result = self.db.execute_query(query, {"hashtag": hashtag})
            if not result:
                raise PostNotFoundException(
                    f"No posts found for hashtag '{hashtag}'")
            return result
        except PostNotFoundException as e:
            raise e
        except Exception as e:
            raise Exception(f"Error searching posts by hashtag: {str(e)}")

    def delete(self, title: str) -> Dict:
        query = """
        MATCH (p:Post {title: $title})
        DETACH DELETE p
        RETURN COUNT(p) AS deleted_count
        """
        try:
            result = self.db.execute_query(query, {"title": title})
            if not result:
                raise PostNotFoundException(
                    f"Post with title '{title}' not found")
            return result
        except PostNotFoundException as e:
            raise e
        except Exception as e:
            raise Exception(f"Error deleting post: {str(e)}")
