from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from .base import Base
from sqlalchemy.sql import func

class ContentLog(Base):
    __tablename__ = "content_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    tweet_id = Column(String)
    category = Column(String)
    sent_channel = Column(String)
    status = Column(String, default="pending")
    raw_tweet_data = Column(Text, nullable=True)
    error_message = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
