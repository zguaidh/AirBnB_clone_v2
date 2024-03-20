#!/usr/bin/python3
"""DBStorage module"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """MySQL database engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the class
        """
        USER = getenv('HBNB_MYSQL_USER')
        USER_PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DATABASE = getenv('HBNB_MYSQL_DB')
        _env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, USER_PWD, HOST, DATABASE), pool_pre_ping=True)

        if _env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Fetches all the data from the database
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = '{}.{}'.format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            classes = [State, City, Amenity, Review, Place, User]
            for _cls in classes:
                query = self.__session.query(_cls)
                for elem in query:
                    key = '{}.{}'.format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic

    def new(self, obj):
        """Adds the obj into the session
        """
        self.__session.add(obj)

    def save(self):
        """Saves the current session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the obj from the session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the database
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        self.__session.close()
