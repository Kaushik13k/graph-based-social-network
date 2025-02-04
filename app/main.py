import asyncio
from models.socialnetwork import SocialNetwork


async def main():
    social_graph = SocialNetwork()
    social_graph.add_user("user_1")

    social_graph.add_user("user_2")
    social_graph.add_connection("user_1", "user_2")

    print("Friends of user_1:", social_graph.get_friends("user_1"))

    social_graph.add_post("user_1", "Hello world!")
    print("Posts by user_1:", social_graph.graph.nodes["user_1"]["posts"])
asyncio.run(main())
