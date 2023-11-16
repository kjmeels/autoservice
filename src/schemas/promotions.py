from datetime import date
from typing import Optional

import ujson
from pydantic import BaseModel, Field, PositiveInt


class PromotionSchema(BaseModel):
    id: Optional[PositiveInt] = Field(
        title="ID",
    )

    type: str = Field(
        max_length=64,
        title="Type",
    )

    discount_percentage: int = Field(
        title="-%"
    )

    end_date: date = Field(
        title="End date"
    )

    class Config:
        title = "Promotions"
        json_schema_extra = {
            "example": {
                "id": 1,
                "type": "repost",
                "discount_percentage": 10,
                "end_date": "2023-11-23",
            }
        }
