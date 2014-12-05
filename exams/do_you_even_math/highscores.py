from connection import Base
from sqlalchemy import Column, Integer, String


class Highscore(Base):
    __tablename__ = "highscores"
    id = Column(Integer, primary_key=True)
    playername = Column(String)
    score = Column(Integer)
