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

    class Config:
        title = "Details"
        json_schema_extra = {
            "example": {
                "id": 1,
                "detail_category": "new",
                "detail_model": "AB7",
                "detail_price": 200.0,
                "is_available": True,
            }
        }
