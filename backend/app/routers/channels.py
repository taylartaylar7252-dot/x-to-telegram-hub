from fastapi import APIRouter
from app.schemas.channel import ChannelCreate

router = APIRouter(prefix="/api/channels", tags=["channels"])

@router.post("/")
def add_channel(data: ChannelCreate):
    # şimdilik mock
    return {"status": "ok", "channel": data.channel_id}
