import uuid
from configs.graph_db import DatabaseConnection


class UserRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def create(self, name: str, email: str, age: int):
        user_id: str = uuid.uuid4().hex

        check_user_label = "MATCH (u:User) RETURN COUNT(u) AS count"
        label_check_result = self.db.execute_query(check_user_label)

        user_count = label_check_result[0]["count"] if label_check_result else 0

        if user_count == 0:
            print("No 'User' nodes exist! Creating a sample user first...")
            self.db.execute_query(
                "CREATE (:User {id: 'init', name: 'Init User', email: 'init@example.com', age: 99})"
            )

        check_query = "MATCH (u:User {email: $email}) RETURN u"
        existing_user = self.db.execute_query(check_query, {"email": email})

        if existing_user:
            return {"error": "User with this email already exists"}

        query = """
        CREATE (u:User {id: $user_id, name: $name, email: $email, age: $age})
        RETURN u.id AS id, u.name AS name, u.email AS email, u.age AS age
        """
        return self.db.execute_query(query, {"user_id": user_id, "name": name, "email": email, "age": age})

    def all_users(self):
        query = "MATCH (u:User) RETURN u.id AS id, u.name AS name, u.email AS email, u.age AS age"
        return list(self.db.execute_query(query))

    def user(self, email: str):
        query = """
        MATCH (u:User) WHERE EXISTS(u.email) AND u.email = $email
        RETURN u.id AS id, u.name AS name, u.email AS email, u.age AS age
        """
        result = self.db.execute_query(query, {"email": email})
        return list(result) if result.peek() else {"error": "User not found"}

    def update(self, old_email: str, new_email: str):
        query = """
        MATCH (u:User) WHERE EXISTS(u.email) AND u.email = $old_email
        SET u.email = $new_email
        RETURN u.id AS id, u.name AS name, u.email AS email, u.age AS age
        """
        return list(self.db.execute_query(query, {"old_email": old_email, "new_email": new_email}))

    def delete(self, email: str):
        query = """
        MATCH (u:User) WHERE EXISTS(u.email) AND u.email = $email
        DETACH DELETE u
        RETURN "User deleted"
        """
        return self.db.execute_query(query, {"email": email})
