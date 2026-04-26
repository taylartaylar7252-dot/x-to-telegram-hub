from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    telegram_id: str
    plan_type: str
    is_vip: bool
    category_change_count: int

    class Config:
        from_attributes = True
