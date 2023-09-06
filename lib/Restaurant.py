from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants' 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def reviews(self, session):  
        return session.query(Review).filter(Review.restaurant_id == self.id).all()

    def customers(self, session):  
        customers_set = set()
        for review in self.reviews(session):
            customers_set.add(review.customer(session))
        return list(customers_set)

    @classmethod
    def fanciest(cls, session):
        restaurants = session.query(Restaurant).all()
        fanciest = None
        max_avg_rating = -1
        for restaurant in restaurants:
            ratings = [review.rating for review in restaurant.reviews(session)]
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                if avg_rating > max_avg_rating:
                    max_avg_rating = avg_rating
                    fanciest = restaurant
        return fanciest

    def all_reviews(self, session):
        review_strings = []
        for review in self.reviews(session):
            review_strings.append(review.full_review())
        return review_strings
