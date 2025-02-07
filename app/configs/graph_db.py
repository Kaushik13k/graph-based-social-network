from neo4j import GraphDatabase
from constants.envs import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.driver = GraphDatabase.driver(
                NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        return cls._instance

    def execute_query(self, query: str, parameters: dict = None):
        with self.driver.session() as session:
            try:
                result = session.run(query, parameters)

                return [record.data() for record in result]
            except Exception as e:
                print(f"Database Error: {e}")
                return []

    def close(self):
        self.driver.close()
