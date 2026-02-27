from pydantic import BaseModel
from typing import List, Union

# This is how interdependencies of models work

class City(BaseModel):
    name: str

class State(BaseModel):
    name: str
    city: City

class Country(BaseModel):
    name: List[str]
    state: State

class Industry(BaseModel):
    type: str
    country: Country

class Employee(BaseModel):
    name: str
    belongsTo: Union[Country, Industry]


