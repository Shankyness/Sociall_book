
from sqlalchemy import create_engine
import urllib.parse

# Replace the following placeholders with actual values
DATABASE_NAME = 'adding_books'
USERNAME = 'myuser1'
PASSWORD = 'Shishank@0107'
HOST = 'localhost'
PORT = '5432'  # Default PostgreSQL port

# URL-encode the password to handle special characters
encoded_password = urllib.parse.quote(PASSWORD)

DATABASE_URL = f"postgresql://{USERNAME}:{encoded_password}@{HOST}:{PORT}/{DATABASE_NAME}"

engine = create_engine(DATABASE_URL)
