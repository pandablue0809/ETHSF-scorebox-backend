from sqlalchemy.types import Boolean, Integer, String, Text
from sqlalchemy import Column
from supp.db import Base


class EncryptTable(Base):

    __tablename__ = 'encrypt'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    wallet = Column(String(64), nullable=False)
    oracle = Column(String(16), nullable=False)
    blockchain = Column(String(16), nullable=False)
    is_encrypted = Column(Boolean, nullable=False)
    permit = Column(String(16), nullable=True)
    score_int = Column(Integer, nullable=False)
    score_blurb = Column(Text, nullable=False)
    timestamp = Column(Integer, nullable=False)