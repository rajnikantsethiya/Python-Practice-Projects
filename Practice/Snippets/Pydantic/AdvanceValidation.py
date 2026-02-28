from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

# Validate username, age, daterange

class User(BaseModel):
    username: str

    @field_validator('username', mode='before')
    def checkCase(v):
        if v.username.istitle():
            return v
        raise ValueError("Name must be capitalize")

class Age(BaseModel):
    age: int

    @field_validator('age')
    def checkAdult(v):
        if v.age > 18:
            return v
        raise ValueError("Age must be 18+")

class DateRange(BaseModel):
    start: datetime
    end: datetime

    @model_validator('start', 'end', mode='after')
    def checkRange(v):
        if v.start < v.end:
            raise ValueError("Start date must be greater than end date")
        return v
