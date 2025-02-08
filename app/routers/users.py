from typing import Optional
from fastapi import APIRouter, HTTPException
from schemas.users import UserSchema
from services.users import UserService
from exceptions.exceptions import UserNotFoundException, UserAlreadyExistsException
from utils.api_response import success, error

router = APIRouter()
user_service = UserService()


@router.post("/users", tags=["Create users"], responses={404: {"description": "Not found"}})
def create_user(user: UserSchema):
    try:
        result = user_service.create(user)
        return success(message="User created successfully", response=result)
    except UserAlreadyExistsException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        return error(str(e))


@router.get("/users", tags=["Get All users / Search By username"], responses={404: {"description": "Not found"}})
def get_all_users(username: Optional[str] = None):
    try:
        if not username:
            users = user_service.all_users()
            return success(message="All users fetched successfully", response=users)
        else:
            user = user_service.user(username)
            if not user:
                raise UserNotFoundException(
                    f"User with username '{username}' not found")
            return success(message="User fetched successfully", response=user)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        return error(str(e))


@router.put("/users", tags=["Update users"], responses={404: {"description": "Not found"}})
def update_user(old_email: str, new_email: str):
    try:
        result = user_service.update(old_email, new_email)
        return success(message="User updated successfully", response=result)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        return error(str(e))


@router.delete("/users", tags=["Delete users"], responses={404: {"description": "Not found"}})
def delete_user(username: str):
    try:
        result = user_service.delete(username)
        return success(message="User deleted successfully", response=result)
    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        return error(str(e))
