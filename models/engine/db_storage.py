#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, query, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv, environ


class DBStorage:
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        user = environ["HBNB_MYSQL_USER"]
        password = environ["HBNB_MYSQL_PWD"]
        host = environ["HBNB_MYSQL_HOST"]
        database = environ["HBNB_MYSQL_DB"]
        db_url = f"mysql+mysqldb://{user}:{password}@{host}/{database}"
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        "this method must return a dictionary with requested info"
        from models import State, City, Place, Amenity, User, Review
        obj_dict = {}
        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Amenity).all())
            obj.extend(self.__session.query(User).all())
            obj.extend(self.__session.query(Review).all())
        else:
            obj = self.__session.query(cls).all()
        for item in obj:
            key = f"{item.__class__.__name__}.{obj.id}"
            obj_dict[key] = item
        return obj_dict

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
        from models import State, City, Place, Amenity, User, Review
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
