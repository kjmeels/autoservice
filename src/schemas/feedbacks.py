from datetime import datetime
from typing import Optional

import ujson
from pydantic import BaseModel, Field, PositiveInt


class FeedbackSchema(BaseModel):
    id: Optional[PositiveInt] = Field(
        title="ID",
    )

    user_name: str = Field(
        title="user name",
        dicriptions="user, who wrote comment",
    )

    text: str = Field(
        title="comment",
        max_length=64,
    )

    date: datetime = Field(
        title="Feedback date",
    )

    class Config:
        title = "Feedbacks"
        json_schema_extra = {
            "example": {
                "id": 1,
                "user_name": "Misha",
                "text": "Good service! Good personal! Nice promotions!",
                "date": "2023-05-05 23:00",
            }
        }
