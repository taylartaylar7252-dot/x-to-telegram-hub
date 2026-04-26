from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .base import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    stripe_subscription_id = Column(String, unique=True, nullable=True)
    stripe_customer_id = Column(String, unique=True, nullable=True)
    plan_type = Column(String)
    status = Column(String, default="active")
    current_period_end = Column(DateTime(timezone=True), nullable=True)
    canceled_at = Column(DateTime(timezone=True), nullable=True)
