import os

import pymysql
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

pymysql.install_as_MySQLdb()
engine: sqlalchemy.engine.base.Engine = create_engine(
    os.getenv("SA_DB_URL"), pool_recycle=3600
)
session: sqlalchemy.orm.session.sessionmaker = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

base = declarative_base()
