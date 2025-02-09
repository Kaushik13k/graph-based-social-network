from fastapi import APIRouter, HTTPException
from schemas.message import MessageSchema
from services.message import MessageService
from exceptions.exceptions import UserNotFoundError, MessageEncryptionError, DatabaseQueryError

router = APIRouter()
message_service = MessageService()


@router.post("/messages/send")
def send_message(message: MessageSchema):
    try:
        return message_service.send_message(message)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except MessageEncryptionError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except DatabaseQueryError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception:
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred.")


@router.get("/messages/recieve")
def get_messages(sender_username: str, receiver_username: str):
    try:
        return message_service.get_messages(sender_username, receiver_username)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except DatabaseQueryError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception:
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred.")
