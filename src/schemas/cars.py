from typing import Optional

import ujson
from pydantic import BaseModel, Field, PositiveInt


class CarSchema(BaseModel):
    id: Optional[PositiveInt] = Field(
        title="ID",
    )

    # transport_category: str = Field(
    #     max_length=64,
    #     title="Type",
    # )

    brand: str = Field(
        max_length=64,
        title="Brand",
    )
    model: str = Field(
        max_length=64,
        title="Model",
    )
    engine_type: str = Field(
        max_length=64,
        title="Engine type",
    )
    drive_type: str = Field(
        max_length=64,
        title="Drive type",
    )

    year_of_production: Optional[PositiveInt] = Field(
        title="Year",
        description="Year of car",
    )

    vin: Optional[PositiveInt] = Field(
        title="VIN",
        description="VIN code of car",
    )

    class Config:
        title = "Cars"
        json_schema_extra = {
            "example": {
                "id": 1,
                "brand": "BMW",
                "model": "318i",
                "engine_type": "petrol",
                "drive_type": "automatic",
                "year_of_production": 2009,
                "vin": 12345678,
            }
        }
