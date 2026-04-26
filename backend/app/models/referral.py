from sqlalchemy import Column, Integer, ForeignKey, Boolean
from .base import Base

class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True, index=True)
    referrer_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    referred_user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    is_activated = Column(Boolean, default=False)
