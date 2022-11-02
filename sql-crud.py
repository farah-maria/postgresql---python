from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create class-based model for programmer table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to db directly, ask 4 session.
# create new instance of sessionmaker, then point 2 the db (our engine)
Session = sessionmaker(db)
# opens a session by calling Session() subclass defined above
session = Session()

# creating the db using declarative_base subclass
base.metadata.create_all(db)

# create records for programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British"
    famous_for="First programmer"
)

# add each instance of programmers to our session
session.add(ada_lovelace)

# commit session to db
session.commit