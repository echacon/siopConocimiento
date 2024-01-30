# declarative_base.py
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://ussgo:usuario_sgo_@127.0.0.1:3306/bdsgo")
Session = sessionmaker(bind=engine)
