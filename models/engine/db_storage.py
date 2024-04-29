#!/usr/bin/python3
"""This module defines the DBStorage class."""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Represents a database storage engine."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        objs = {}
        if cls:
            for obj in self.__session.query(eval(cls)).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objs[key] = obj
        else:
            for cls in Base.__subclasses__():
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def get(self, cls, id):
        """Retrieve an object from the database by its class and id."""
        return self.__session.query(eval(cls)).get(id)

    def count(self, cls=None):
        """Count the number of objects in the database."""
        if cls:
            return self.__session.query(eval(cls)).count()
        else:
            count = 0
            for cls in Base.__subclasses__():
                count += self.__session.query(cls).count()
            return count
