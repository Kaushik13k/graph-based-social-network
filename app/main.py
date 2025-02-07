from services.post_queries import PostRepository
from services.user_queries import UserRepository
# import asyncio
# from models.socialnetwork import SocialNetwork


# async def main():
#     social_graph = SocialNetwork()
#     social_graph.add_user("user_1")

#     social_graph.add_user("user_2")
#     social_graph.add_connection("user_1", "user_2")

#     print("Friends of user_1:", social_graph.get_friends("user_1"))

#     social_graph.add_post("user_1", "Hello world!")
#     print("Posts by user_1:", social_graph.graph.nodes["user_1"]["posts"])
# asyncio.run(main())


if __name__ == "__main__":
    user_repo = UserRepository()
    post_repo = PostRepository()

    # print("Creating Users...")
    # user_repo.create("Alice", "alice@example.com", 25)
    # user_repo.create("Bob", "bob@example.com", 28)

    # print()
    # print("Users in Database:")
    # for record in user_repo.all_users():
    #     print(record)

    print()
    print("Creating Posts...")
    post_repo.create("Title-1", "Hello, world!", "2025-02-05T10:00:00",
                     "alice@example.com")
    post_repo.create("Title-2", "Neo4j is awesome!",
                     "2025-02-05T12:00:00", "bob@example.com")

    print()
    print("Posts in Database:")
    for record in post_repo.posts():
        print(record)

    # print()
    # print("Updating Alice's email...")
    # user_repo.update("alice@newdomain.com", "alice@newdomain.com")

    # print()
    # print("Deleting User Bob...")
    # user_repo.delete("2")

    user_repo.db.close()
