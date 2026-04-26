from sqlalchemy import Column, Integer, String, ForeignKey, Date
from .base import Base

class DailyTranslation(Base):
    __tablename__ = "daily_translations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    date = Column(Date)
    count = Column(Integer, default=0)
