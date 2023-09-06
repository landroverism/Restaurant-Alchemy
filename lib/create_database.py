from sqlalchemy import create_engine
from Customer import Base, Customer, Restaurant, Review 

# Defining the database file path 
database_url = 'sqlite:///ham_database.db'

# Creating SQLAlchemy engine
engine = create_engine(database_url)

# creating tables in the database
Base.metadata.create_all(engine)
