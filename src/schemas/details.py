from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class DetailSchema(BaseModel):
    id: Optional[PositiveInt] = Field(
        title="ID",
    )

    category: str = Field(
        max_length=64,
        title="Type",
    )

    model: str = Field(
        max_length=64,
        title="Model",
    )

    price: float = Field(
        title="Price",
        description="Detail price in $",
    )

    is_available: bool = Field(
        title="is_available",
        description="Has in storage",

    )

    car_id:  Optional[PositiveInt] = Field(
        title="Car",
        description="car that equipped with this detail"
    )

    class Config:
        title = "Details"
        json_schema_extra = {
            "example": {
                "id": 1,
                "category": "new",
                "model": "AB7",
                "price": 200.0,
                "is_available": True,
                "car_id": 1,
            }
        }
