#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, query, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """ Class DBStorage """

    __engine = None
    __session = None

    def __init__(self):
        """ Constructor """
        user = environ["HBNB_MYSQL_USER"]
        password = environ["HBNB_MYSQL_PWD"]
        host = environ["HBNB_MYSQL_HOST"]
        database = environ["HBNB_MYSQL_DB"]
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), pool_pre_ping=True)
        if (environ.get("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models import State, City, Place, Amenity, User, Review
        if cls is None:
            return {
                "State": self.__session.query(State).all(),
                "City": self.__session.query(City).all(),
                "Place": self.__session.query(Place).all(),
                "Amenity": self.__session.query(Amenity).all(),
                "User": self.__session.query(User).all(),
                "Review": self.__session.query(Review).all()
            }
        else:
            return self.__session.query(cls).all()
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
