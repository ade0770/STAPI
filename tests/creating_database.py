


# Создаем строку подключения
# url = "postgresql+asyncpg://andrew_adm:Pasw@localhost:5432/mydb"


from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = "postgresql+asyncpg://andrew_adm:Pasw@localhost:5432/mydb"

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()