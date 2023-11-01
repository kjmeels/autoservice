from typing import Optional

import ujson
from pydantic import BaseModel, Field, PositiveInt


class ServiceSchema(BaseModel):
    service_id: Optional[PositiveInt] = Field(
        title="number №",
    )

    service_name: str = Field(
        title="name of service",
        max_length=64,
    )

    service_price: Optional[PositiveInt] = Field(
        title="price",
    )

    class Config:
        json_dump = ujson.dump
        json_loads = ujson.loads
        title = "Services"
        schema_extra = {
            "example": {
                "service_id": 1,
                "service_name": "cleaning",
                "service_price": 250,
            }
        }
