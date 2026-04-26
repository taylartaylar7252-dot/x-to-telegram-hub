from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .base import Base

class XFollowing(Base):
    __tablename__ = "x_followings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    x_user_id = Column(String)
    username = Column(String)
    display_name = Column(String, nullable=True)
    last_checked = Column(DateTime(timezone=True), nullable=True)
