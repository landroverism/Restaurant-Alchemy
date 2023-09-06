from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Review(Base):
   
    def customer(self):
        
        return session.query(Customer).filter(Customer.id == self.customer_id).first()

    def restaurant(self):
        return session.query(Restaurant).filter(Restaurant.id == self.restaurant_id).first()

    def full_review(self):
        
        return f"Rating: {self.rating} - Customer: {self.customer().full_name()} - Restaurant: {self.restaurant().name}"
