from typing import Any, Optional, List

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from readconfig import get_config

class DB:
    def __init__(self):
        config, err = get_config()

        if err:
            raise Exception

        self.engine = create_engine("sqlite:///"+config.db, connect_args={"check_same_thread": False})

        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        self.Base = declarative_base()

database: List[DB] = []

def init():
    assert database == []
    database.append(DB())
    # import is needed for registering moels
    # noinspection PyUnresolvedReferences
    from . import models