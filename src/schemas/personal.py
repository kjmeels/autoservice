from typing import Optional

from pydantic import BaseModel, Field, root_validator, EmailStr
from pydantic.types import PositiveInt


class PersonDeleteSchema(BaseModel):
    id: Optional[PositiveInt] = Field(
        title="ID",
    )

    class Config:
        title = "Person"
        json_schema_extra = {
            "example": {
                "id": 1,
            }
        }


class PersonalListSchema(BaseModel):
    id: Optional[PositiveInt] = Field(
        title="ID",
    )
    name: str = Field(
        max_length=64,
        title="Name",
    )
    surname: str = Field(
        max_length=64,
        title="Surname"
    )
    email: EmailStr | None = Field(
        max_length=256,
        title="Email"
    )

    @classmethod
    def email_validator(cls, values: dict) -> dict:
        if values.get("email"):
            email = values.get("email")
            if email.endswith(".com"):
                values["email"] = email.replace(".com", ".ru")
        return values

    class Config:
        title = "Person"
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Ivan",
                "surname": "Ivanov",
                "email": "ivanov@mail.ru"
            }
        }
