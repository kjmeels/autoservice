from sqlalchemy import Column, INT, VARCHAR, DATE

from . import Base


class Feedback(Base):
    id = Column(INT, primary_key=True)
    user_name = Column(VARCHAR(64), nullable=False)
    text = Column(VARCHAR(256), nullable=False)
    date = Column(DATE, nullable=False)
