from sqlalchemy import Column, Integer, String
from database import Base

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    favorite_show = Column(String(100), nullable=False)