1. Install Requirements.txt
2. pytest -v

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
AES_SECRET_KEY

DELETE DB - MATCH (n) DETACH DELETE n;
Check if DB is empty - MATCH (n) RETURN labels(n), properties(n) LIMIT 5;
