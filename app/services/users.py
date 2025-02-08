import uuid
from configs.graph_db import DatabaseConnection
from schemas.users import UserSchema
from exceptions.exceptions import UserNotFoundException, UserAlreadyExistsException


class UserService:
    def __init__(self):
        self.db = DatabaseConnection()

    def create(self, user: UserSchema):
        user_id: str = uuid.uuid4().hex

        label_check_query = "MATCH (u:User) RETURN COUNT(u) AS count"
        label_check_result = self.db.execute_query(label_check_query)
        user_count = label_check_result[0]["count"] if label_check_result else 0

        if user_count == 0:
            print("No 'User' nodes exist! Creating a sample user first...")
            self.db.execute_query(
                "CREATE (:User {id: 'init', name: 'Init User', email: 'init@example.com', user_name: 'init@1', age: 99, timestamp: 1738992796.789765})"
            )

        check_query = "MATCH (u:User {email: $email}) RETURN u"
        existing_user = self.db.execute_query(
            check_query, {"email": user.email})

        if existing_user:
            raise UserAlreadyExistsException(
                "User with this email already exists")

        query = """
        CREATE (u:User {id: $user_id, name: $name, user_name: $user_name, email: $email, age: $age, timestamp: $timestamp})
        RETURN u.id AS id, u.name AS name, u.email AS email, u.age AS age, u.timestamp AS timestamp
        """
        return self.db.execute_query(query, {"user_id": user_id, "name": user.name, "user_name": user.user_name, "email": user.email, "age": user.age, "timestamp": user.timestamp})

    def all_users(self):
        query = "MATCH (u:User) RETURN u.id AS id, u.name AS name, u.user_name AS user_name, u.email AS email, u.age AS age, u.timestamp AS timestamp"
        return list(self.db.execute_query(query))

    def user(self, user_name: str):
        query = """
        MATCH (u:User) WHERE u.user_name IS NOT NULL AND u.user_name = $user_name
        RETURN u.id AS id, u.name AS name, u.user_name AS user_name, u.email AS email, u.age AS age, u.timestamp AS timestamp
        """
        result = self.db.execute_query(query, {"user_name": user_name})
        if not result:
            raise UserNotFoundException(f"User with username '{
                                        user_name}' not found")
        return result

    def update(self, old_email: str, new_email: str):
        query = """
        MATCH (u:User) WHERE u.email IS NOT NULL AND u.email = $old_email
        SET u.email = $new_email
        RETURN u.id AS id, u.name AS name, u.user_name AS user_name, u.email AS email, u.age AS age, u.timestamp AS timestamp
        """
        result = self.db.execute_query(
            query, {"old_email": old_email, "new_email": new_email})
        if not result:
            raise UserNotFoundException(
                f"User with email '{old_email}' not found")
        return result

    def delete(self, user_name: str):
        query = """
        MATCH (u:User) WHERE u.user_name IS NOT NULL AND u.user_name = $user_name
        DETACH DELETE u
        RETURN "User deleted"
        """
        result = self.db.execute_query(query, {"user_name": user_name})
        if not result:
            raise UserNotFoundException(
                f"User with username '{user_name}' not found")
        return result
