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

    feedback_text: str = Field(
        title="comment",
        max_length=64,
    )

    feedback_date: datetime = Field(
        title="Feedback date",
    )

    class Config:
        json_dumps = ujson.dumps
        json_loads = ujson.loads
        title = "Feedbacks"
        schema_extra = {
            "example": {
                "id": 1,
                "user_name": "Misha",
                "feedback_text": "Good service! Good personal! Nice promotions!",
                "feedback_date": "2023-11-28",
            }
        }
