from typing import List

from sqlalchemy import Column, INT, VARCHAR
from sqlalchemy.orm import relationship, Mapped

from . import Base


class Car(Base):
    id = Column(INT, primary_key=True)
    brand = Column(VARCHAR(64), nullable=False)
    model = Column(VARCHAR(64), nullable=False)
    engine_type = Column(VARCHAR(64), nullable=False)
    drive_type = Column(VARCHAR(64), nullable=False)
    year_of_production = Column(INT, nullable=False)
    vin = Column(INT, nullable=False)

    # details: Mapped[List[INT]] = relationship()
