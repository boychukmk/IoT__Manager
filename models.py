from peewee import *
import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase



load_dotenv()

db = PostgresqlDatabase(
    os.getenv('DATABASE_NAME'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    host=os.getenv('DATABASE_HOST'),
    port=int(os.getenv('DATABASE_PORT'))
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

