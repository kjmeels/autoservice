from sqlalchemy import Column, VARCHAR, INT

from sqlalchemy_utils import EmailType, PhoneNumber

from . import Base


class Info(Base):
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    address = Column(VARCHAR(128), nullable=False)
    phone_number = Column(INT, nullable=False)
    email = Column(EmailType, nullable=False)
