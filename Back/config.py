import os

from dotenv import load_dotenv

load_dotenv()

db_schema = os.getenv("db_schema")
db_username = os.getenv("db_username")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")

main_db_uri = (
    "mysql://"
    + db_username
    + ":"
    + db_password
    + "@"
    + db_host
    + ":3306/"
    + db_schema
    + "?charset=utf8"
)

class Config:
    SQLALCHEMY_DATABASE_URI = main_db_uri