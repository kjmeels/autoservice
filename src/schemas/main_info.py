import ujson
from pydantic import BaseModel, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class InfoSchema(BaseModel):
    name: str = Field(
        ...,  # элепсис - для указания того, что этот аргумент - обязательный
        title="Name",
        description="Autoservice name",
        max_length=64,
    )

    address: str = Field(
        ...,
        title="Address",
        description="address of autoservice",
        max_length=64,
    )

    phone_number: PhoneNumber = Field(
        title="Phonenumber",
        description="phonenumber of autoservice",
    )

    email: EmailStr | None = Field(
        max_length=256,
        title="Email",
    )

    class Config:
        json_dumps = ujson.dumps
        json_loads = ujson.loads
        title = "Info"
        schema_extra = {
            "example": {
                "name": "Autoservice Name",
                "address": "Mayakovskogo 28a",
                "phone_number": "+375445214785",
                "email": "Autoservice@mail.ru"
            }
        }

