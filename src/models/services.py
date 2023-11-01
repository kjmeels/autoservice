from sqlalchemy import Column, INT, VARCHAR

from . import Base


class Service(Base):
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    price = Column(INT, nullable=False)
