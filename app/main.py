import logging
import uvicorn
from starlette.routing import Match
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from routers import health, posts, users

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    logger.info("Started the server!")
    yield
    # shutdown
    logger.info("Shutdown the server!")


app = FastAPI(
    title="Social Network",
    version="0.0.1",
    contact={"name": "Kaushik", "email": "13kaushikk@gmail.com"},
    debug=True,
    lifespan=lifespan,
)


@app.middleware("https")
async def log_middlewear(request: Request, call_next):
    logger.info(f"{request.method} {request.url}")
    routes = request.app.router.routes
    logger.info("Params: ")
    for route in routes:
        match, scope = route.matches(request)
        if match == Match.FULL:
            for name, value in scope["path_params"].items():
                logger.info(f"{name}: {value}")
    logger.info("Headers: ")
    for name, value in request.headers.items():
        logger.info(f"{name}: {value}")

    response = await call_next(request)
    logger.info(f"{request.method} {request.url} {response.status_code}")
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/v1")
app.include_router(posts.router, prefix="/v1")
app.include_router(users.router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# from services.user_queries import UserRepository
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


# if __name__ == "__main__":
#     user_repo = UserRepository()
#     # post_repo = PostRepository()

#     print("Creating Users...")
#     user_repo.create(name="Alice", user_name="Alice_@12",
#                      email="alice@example.com", age=25)
#     user_repo.create(name="Bob", user_name="Bob_@12",
#                      email="bob@example.com",  age=28)

#     print()
#     print("Users in Database:")
#     for record in user_repo.all_users():
#         print(record)

#     # print()
#     # print("Creating Posts...")
#     # post_repo.create("Title-1", "Hello, world!", "2025-02-05T10:00:00",
#     #                  "alice@example.com")
#     # post_repo.create("Title-2", "Neo4j is awesome!",
#     #                  "2025-02-05T12:00:00", "bob@example.com")

#     # print()
#     # print("Posts in Database:")
#     # for record in post_repo.posts():
#     #     print(record)

#     # print()
#     # print("Updating Alice's email...")
#     # user_repo.update("alice@newdomain.com", "alice@newdomain.com")

#     # print()
#     # print("Deleting User Bob...")
#     # user_repo.delete("2")

#     user_repo.db.close()
