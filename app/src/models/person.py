from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, Float
from src.database import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=False)
    email = Column(String(30), unique=True, index=True)
    gender = Column(String(10))
    birth_date = Column(Date, nullable=False)
    address = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    cpf = Column(String(11), nullable=False)

    account = relationship("Account", back_populates=("owner"))