from connection import Base
from movie import Movie
from projection import Projection
from reservation import Reservation
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


class Cinema():
    def __init__(self, engine):
        self.engine = engine
        self.session = Session(bind=engine)

    def add_movies(self, name, rating):
        movie = Movie(name=name, rating=rating)
        self.session.add(movie)
        self.session.commit()

    def add_projection(self, movie_id, type, date, time):
        projection = Projection(movie_id=movie_id, type=type, date=date, time=time)
        self.session.add(projection)
        self.session.commit()

    def show_movies(self):
        movies = self.session.query(Movie).order_by(Movie.rating.desc()).all()
        for movie in movies:
            print(movie)

    def show_movie_projections(self, id):
        res = self.session.query(Projection).filter(Projection.movie_id == id).all()
        for i in res:
            print(i)

    def show_seats(self):
        hall = [['.' for x in range(10)] for x in range(10)]
        result = ""
        for row in hall:
            for seat in row:
                result += seat + " "
            result += "\n"
        print(result)


def main():
    engine = create_engine("sqlite:///cinema.db")
    Base.metadata.create_all(engine)
    test = Cinema(engine)
    #test.add_movies("Fast and Furious", 5.5)
    #test.add_movies("Gladiator", 7)
    #test.add_movies("The Hangover", 8)
    #test.add_movies("American pie", 6)
    #test.add_projection(1, "3D", "10.12.2014", "18:20")
    #test.add_projection(1, "2D", "10.12.2014", "15:20")
    #test.add_projection(2, "2D", "11.12.2014", "15:20")
    #test.add_projection(2, "3D", "11.12.2014", "15:20")
    #test.add_projection(3, "2D", "11.12.2014", "15:20")
    #test.add_projection(3, "3D", "10.12.2014", "20:20")
    #test.add_projection(3, "4D", "10.12.2014", "21:20")
    #test.show_movies()
    #print(test.show_movie_projections(1))
    test.show_seats()
if __name__ == '__main__':
    main()
