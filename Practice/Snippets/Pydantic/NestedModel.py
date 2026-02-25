from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class User(BaseModel):
    name: str = Field(...)
    age: int = Field(..., ge=18)
    address: Address

address = Address(
    city="Jaora",
    state="MP",
    pincode="411056"
)

userData = {
    "name": "Raj",
    "age": "30",
    "address": address
}

usr = User(**userData)
print(usr)
    