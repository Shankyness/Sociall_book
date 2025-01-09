from sqlalchemy import text
from database import engine

def fetch_data():
    with engine.connect() as connection:
        query = text("SELECT * FROM user3102")
        result = connection.execute(query)
        
        for row in result:
            print(row)  # Print rows as dictionaries

if __name__ == "__main__":
    fetch_data()
