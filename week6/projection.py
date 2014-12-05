from connection import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    date = Column(String)
    time = Column(String)

    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="projection")

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.id, self.movie_id, self.type, self.date, self.time)

    def __repr__(self):
        return self.__str__()
