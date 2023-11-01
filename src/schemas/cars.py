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

    car_brand: str = Field(
        max_length=64,
        title="Brand",
    )
    car_model: str = Field(
        max_length=64,
        title="Model",
    )
    car_engine_type: str = Field(
        max_length=64,
        title="Engine type",
    )
    car_drive_type: str = Field(
        max_length=64,
        title="Drive type",
    )

    car_year_of_production: Optional[PositiveInt] = Field(
        title="Year",
        description="Year of car",
    )

    car_vin: Optional[PositiveInt] = Field(
        title="VIN",
        description="VIN code of car",
    )

    class Config:
        json_dumps = ujson.dumps
        json_loads = ujson.loads
        title = "Cars"
        schema_extra = {
            "example": {
                "id": 1,
                # "transport_category": "car",
                "car_brand": "BMW",
                "car_model": "318i",
                "car_engine_type": "petrol",
                "car_drive_type": "automatic",
                "car_year_of_production": 2009,
                "car_vin": 12345678,

            }
        }
