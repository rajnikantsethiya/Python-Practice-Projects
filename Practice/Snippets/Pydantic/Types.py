from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

usr = User(id=1, name="Raj", email="r@r.com")
print(usr)



