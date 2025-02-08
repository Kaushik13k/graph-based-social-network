
from fastapi import APIRouter, HTTPException
from schemas.posts import PostSchema
from services.posts import PostService
from exceptions.exceptions import PostNotFoundException
from utils.api_response import success, error

router = APIRouter()
post_service = PostService()


@router.post("/posts", tags=["Create Post"], responses={404: {"description": "Not found"}})
def create_post(post: PostSchema):
    try:
        result = post_service.create(post)
        if not result:
            raise PostNotFoundException(
                "Error creating post. Please check the entered data.")
        return success(message="Post created successfully", response=result)
    except Exception as e:
        return error(str(e))


@router.get("/posts", tags=["Get All Posts"], responses={404: {"description": "Not found"}})
def get_all_posts():
    try:
        result = post_service.get()
        if not result:
            raise PostNotFoundException("No posts found")
        return success(message="All posts fetched successfully", response=result)
    except Exception as e:
        return error(str(e))


@router.get("/posts/search", tags=["Search Posts by Hashtag"], responses={404: {"description": "Not found"}})
def search_by_hashtag(hashtag: str):
    try:
        result = post_service.search_hashtag(hashtag)
        return success(message="Posts fetched successfully", response=result)
    except PostNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        return error(str(e))


@router.delete("/posts", tags=["Delete Post"], responses={404: {"description": "Not found"}})
def delete_post(title: str):
    try:
        result = post_service.delete(title)
        return success(message="Post deleted successfully", response=result)
    except PostNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        return error(str(e))
