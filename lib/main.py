from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module import Base, Customer, Restaurant, Review

# Define the database file path (assuming it's in the current directory)
database_url = 'sqlite:///ham_database.db'

# Create an SQLAlchemy engine
engine = create_engine(database_url)

# Create the tables in the database if they don't exist
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    # Entry point for running the application
    pass
