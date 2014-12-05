from connection import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    row = Column(Integer)
    cow = Column(Integer)

    projection_id = Column(Integer, ForeignKey("projections.id"))
    projection = relationship("Projection", backref="reservations")

    def __str__(self):
        return "{} - {} - {} - {} -{}".format(self.id, self.username, self.projection_id, self.row, self.cow)

    def __repr__(self):
        return self.__str__()
