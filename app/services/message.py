from configs.graph_db import DatabaseConnection
from schemas.message import MessageSchema
from utils.encryption import AESEncryption
from exceptions.exceptions import UserNotFoundError, DatabaseQueryError
from typing import List, Dict, Optional


class MessageService:
    def __init__(self):
        self.db = DatabaseConnection()

    def get_user_id(self, username: str) -> Optional[str]:
        query = "MATCH (u:User {user_name: $user_name}) RETURN u.id AS user_id LIMIT 1"
        result = self.db.execute_query(query, {"user_name": username})

        if not result:
            raise UserNotFoundError(username)

        return result[0]["user_id"]

    def send_message(self, message: MessageSchema) -> Dict:
        try:
            sender_id = self.get_user_id(message.sender_username)
            receiver_id = self.get_user_id(message.receiver_username)
            encrypted_content = AESEncryption.encrypt(message.content)

            query = """
            MATCH (sender:User {id: $sender_id}), (receiver:User {id: $receiver_id})
            CREATE (m:Message {id: apoc.create.uuid(), content: $content, timestamp: $timestamp})
            MERGE (sender)-[:SENT]->(m)
            MERGE (m)-[:TO]->(receiver)
            RETURN m
            """
            return self.db.execute_query(query, {
                "sender_id": sender_id,
                "receiver_id": receiver_id,
                "content": encrypted_content,
                "timestamp": message.timestamp
            })

        except Exception as e:
            raise DatabaseQueryError(str(e))

    def get_messages(self, sender_username: str, receiver_username: str) -> List[Dict]:
        try:
            sender_id = self.get_user_id(sender_username)
            receiver_id = self.get_user_id(receiver_username)

            query = """
            MATCH (s:User {id: $sender_id})-[:SENT]->(m:Message)-[:TO]->(r:User {id: $receiver_id})
            RETURN m.content AS content, m.timestamp AS timestamp
            ORDER BY m.timestamp DESC
            """
            results = self.db.execute_query(
                query, {"sender_id": sender_id, "receiver_id": receiver_id})

            if not results:
                return {"message": "No messages found between these users."}

            return [
                {"content": AESEncryption.decrypt(
                    msg["content"]), "timestamp": msg["timestamp"]}
                for msg in results
            ]
        except Exception as e:
            raise DatabaseQueryError(str(e))
