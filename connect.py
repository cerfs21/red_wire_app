# connect v0.2:
#   Use constants for path to user database
#   Move docstring to the top of the file

'''
2 tables used:
- 'USERS':
    - ID
    - Name
- 'CONNECTIONS':
    - ID
    - Datetime
    - User ID
'''

# Import librairies
from datetime import datetime
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Import constants
from utils import USER_PATH, USER_DB

Base = declarative_base()

class User(Base):
    __tablename__ = "USERS"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    connections = relationship("Connection", back_populates="user")

    def __repr__(self):
       return f"User({self.name})"


class Connection(Base):
    __tablename__ = "CONNECTIONS"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("USERS.id"))

    user = relationship("User", back_populates="connections")
    def __repr__(self):
       return f"Connection({self.user.name} at {self.date})"


def create_session():
    engine = create_engine(f"sqlite:///{USER_PATH+USER_DB}", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_user_or_create_it(session, user_name):
    """Given a user's name, find the user in the database
    if it exists, or if it doesn't, create it.

    Args:
        session: SQLAlchemy session
        user_name (str)
    
    Returns:
        User: the requested user.
    """
    user = (
        session
        .query(User)
        .filter_by(name=user_name)
        .first()
    )
    if user is None:
        user = User(name=user_name)
        session.add(user)
    
    return user


def register_new_connection(session, user_name):
    user = get_user_or_create_it(session, user_name)

    date = datetime.today()
    connection = Connection(date=date, user=user)
    session.add(connection)

    return connection


def get_last_connection_date(session, user_name):
    last_connection = (
        session
        .query(Connection)
        .join(User)
        .filter(User.name == user_name)
        .order_by(Connection.date.desc())
        .first()
    )

    if last_connection is None:
        return None
    else:
        return last_connection.date
