from typing import Optional

import ujson
from pydantic import BaseModel, Field, PositiveInt


class ServiceSchema(BaseModel):
    id: Optional[PositiveInt] = Field(
        title="number №",
    )

    name: str = Field(
        title="name of service",
        max_length=64,
    )

    price: Optional[PositiveInt] = Field(
        title="price",
    )

    class Config:
        title = "Services"
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "cleaning",
                "price": 250,
            }
        }
