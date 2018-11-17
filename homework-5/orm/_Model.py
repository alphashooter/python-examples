from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///test.db')
Session = sessionmaker(bind=engine)


@as_declarative(bind=engine)
class Model(object):
    __session__ = Session()

    @classmethod
    def __init_subclass__(cls, **kwargs):
        cls.metadata.create_all()

    def __init__(self):
        self.__session = Session()

    def delete(self):
        self.__session__.delete(self)
        self.__session__.commit()

    def commit(self):
        self.__session__.add(self)
        self.__session__.commit()

    @classmethod
    def enumerate(cls):
        return cls.__session__.query(cls)
