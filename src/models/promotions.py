from sqlalchemy import Column, VARCHAR, INT, DATE

from . import Base


class Promotion(Base):
    id = Column(INT, primary_key=True)
    type = Column(VARCHAR(64), nullable=False)
    discount_percentage = Column(INT, nullable=False)
    end_date = Column(DATE, nullable=False)
