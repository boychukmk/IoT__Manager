from peewee import *
import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase


load_dotenv()
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = int(os.getenv('DB_PORT'))

db = PostgresqlDatabase(
    db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)
class BaseModel(Model):
    class Meta:
        database = db

class ApiUser(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

class Location(BaseModel):
    name = CharField()

class Device(BaseModel):
    name = CharField()
    type = CharField()
    login = CharField()
    password = CharField()
    location = ForeignKeyField(Location, backref='devices')
    api_user = ForeignKeyField(ApiUser, backref='devices')

def initialize_db():
    """
    Initialize the database, connecting and creating tables if they do not exist.
    """
    if db.is_closed():
        print("Connecting to the database...")
        db.connect()
    else:
        print("Database is already connected.")
    print("Creating tables...")
    db.create_tables([ApiUser, Location, Device], safe=True)

