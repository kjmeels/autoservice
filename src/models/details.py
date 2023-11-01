from sqlalchemy import Column, INT, VARCHAR, BOOLEAN, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Detail(Base):
    id = Column(INT, primary_key=True)
    category = Column(VARCHAR(64), nullable=False)
    model = Column(VARCHAR(64), nullable=False)
    price = Column(INT, nullable=False)
    is_available = Column(BOOLEAN, server_default="f")
    # car_id = Column(INT, ForeignKey("car.id", ondelete="CASCADE"), nullable=False)
    # car = relationship("Car", back_populates="details")
