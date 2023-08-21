#!/usr/bin/python3
from models.base_model import Base
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv, environ
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the database"""
        user = environ["HBNB_MYSQL_USER"]
        password = environ["HBNB_MYSQL_PWD"]
        host = environ["HBNB_MYSQL_HOST"]
        database = environ["HBNB_MYSQL_DB"]

        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    user, password, host, database),
                echo=False, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        "this method must return a dictionary with requested info"
        new_dict = {}
        obj = []
        if cls is None:
            obj.extend(self.__session.query(State).all())
            obj.extend(self.__session.query(User).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Amenity).all())
        else:
            obj = (self.__session.query(cls).all())
        for item in obj:
            new_dict[f"{item.__class__.__name__}.{item.id}"] = item
        return new_dict


    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
