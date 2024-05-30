from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="12345",
    host="localhost",
    database="eJournal",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    group_name = Column(String)


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, primary_key=False)
    subject = Column(String)
    score = Column(String)


Base.metadata.create_all(engine)
