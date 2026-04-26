from pydantic import BaseModel

class ChannelCreate(BaseModel):
    channel_id: str
    title: str
