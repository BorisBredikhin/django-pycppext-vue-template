from database.database import database
from sqlalchemy import Column, Integer, String, Float


class User(database[0].Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    password = Column(String)
    raiting = Column(Float, default=0)