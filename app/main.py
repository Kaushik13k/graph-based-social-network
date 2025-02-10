import uvicorn
from fastapi import FastAPI, HTTPException
from models.socialnetwork import SocialNetworkOps

app = FastAPI()
sn = SocialNetworkOps()


@app.post("/users/")
def add_user(user_id: str, name: str, username: str, email: str, age: int):
    """Add User"""
    sn.add_user(user_id, name, username, email, age)
    return {"message": "User added successfully"}


@app.get("/users/")
def get_all_nodes():
    """Get All Users"""
    nodes = list(sn.graph.nodes.keys())
    return {"nodes": nodes}


@app.post("/users/{user1}/connect/{user2}")
def add_connection(user1: str, user2: str):
    """Create Connection Between Two Users"""
    sn.add_connection(user1, user2)
    return {"message": f"User {user1} is now connected to {user2}"}


@app.get("/users/{user_id}/connections")
def get_connections(user_id: str):
    """Get User Connections"""
    connections = sn.get_connections(user_id)
    return {"connections": connections}


@app.post("/posts/")
def add_post(user_id: str, post_id: str, title: str, content: str):
    """Add Post"""
    sn.add_post(user_id, post_id, title, content)
    return {"message": "Post added successfully"}


@app.get("/posts/")
def get_all_posts():
    """Get All Posts"""
    posts = [
        node_id for node_id, node in sn.graph.nodes.items()
        if node.node_type == "post"
    ]
    return {"posts": posts}


@app.get("/users/{user_id}/posts")
def get_posts(user_id: str):
    """Get Posts by User"""
    posts = sn.get_posts(user_id)
    return {"posts": posts}


@app.post("/posts/{post_id}/like")
def like_post(user_id: str, post_id: str):
    """Like a Post"""
    author = sn.get_post_author(post_id)
    if not author:
        raise HTTPException(status_code=404, detail="Post not found")

    connections = sn.get_connections(user_id)
    if author not in connections:
        raise HTTPException(
            status_code=403, detail="You must be connected to the author to like this post")

    sn.like_post(user_id, post_id)
    return {"message": "Post liked successfully"}


@app.get("/posts/{post_id}/likes")
def get_who_liked_post(post_id: str):
    """Get Who Liked a Post"""
    liked_users = sn.get_who_liked_post(post_id)
    return {"liked_by": liked_users}


@app.get("/posts/{post_id}/like_count")
def get_post_like_count(post_id: str):
    """Get Like Count on a Post"""
    like_count = sn.get_post_like_count(post_id)
    return {"like_count": like_count}


@app.get("/posts/{post_id}/author")
def get_post_author(post_id: str):
    """Get Post Author"""
    author = sn.get_post_author(post_id)
    return {"author": author}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
