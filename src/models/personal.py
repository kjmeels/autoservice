from sqlalchemy import Column, INT, VARCHAR
from sqlalchemy_utils import EmailType
from . import Base


class Person(Base):
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    surname = Column(VARCHAR(64), nullable=False)
    email = Column(EmailType, nullable=False)
