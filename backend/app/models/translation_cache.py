from sqlalchemy import Column, Integer, String, Text
from .base import Base

class TranslationCache(Base):
    __tablename__ = "translation_cache"

    id = Column(Integer, primary_key=True, index=True)
    source_text_hash = Column(String, unique=True, index=True)
    source_lang = Column(String)
    target_lang = Column(String)
    translated_text = Column(Text)
