import motor.motor_asyncio
from urllib.parse import quote_plus
from info import DATABASE_NAME, IMDB, IMDB_TEMPLATE, MELCOW_NEW_USERS, P_TTI_SHOW_OFF, SINGLE_BUTTON, SPELL_CHECK_REPLY, PROTECT_CONTENT, AUTO_DELETE, AUTO_FFILTER, MAX_BTN

# Function to construct the MongoDB URI
def construct_mongo_uri(username, password, host='localhost', port=27017, database='mydb'):
    username = quote_plus(username)
    password = quote_plus(password)
    return f"mongodb://{username}:{password}@{host}:{port}/{database}"

# Replace with your actual database credentials
DATABASE_URI = construct_mongo_uri('your_username', 'your_password', 'your_host', 'your_port', DATABASE_NAME)

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.grp = self.db.groups

    # ... rest of your Database class methods ...

    # Make sure to include all the methods of your Database class here
    # ...

# Rest of the code (if any)
# ...

# Create the database object
db = Database(DATABASE_URI, DATABASE_NAME)
