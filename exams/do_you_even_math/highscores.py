from connection import Base
from sqlalchemy import Column, Integer, String


class Player(Base):
    __tablename__ = "highscores"
    id = Column(Integer, primary_key=True)
    playername = Column(String)
    score = Column(Integer)

    def __str__(self):
        return "{} - {} points".format(self.playername, self.score)

    def __repr__(self):
        return self.__str__()
