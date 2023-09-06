from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):


    def favorite_restaurant(self):
       
        highest_rating = -1
        favorite = None
        for review in self.reviews():
            if review.rating > highest_rating:
                highest_rating = review.rating
                favorite = review.restaurant()
        return favorite

    def add_review(self, restaurant, rating):
        # Implement this method to create a new review for the restaurant
        new_review = Review(customer_id=self.id, restaurant_id=restaurant.id, rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
    
        session.query(Review).filter(Review.customer_id == self.id, Review.restaurant_id == restaurant.id).delete()
        session.commit()

    def reviews(self):
        
        return session.query(Review).filter(Review.customer_id == self.id).all()

    def restaurants(self):
       
        reviewed_restaurants = set()
        for review in self.reviews():
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)
  
  