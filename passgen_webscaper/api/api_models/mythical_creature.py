from pydantic import BaseModel, Field, EmailStr
from .py_object_id import PyObjectId
from bson import ObjectId
from typing import Optional


class MythicalCreatureModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "dragon"
            }
        }
