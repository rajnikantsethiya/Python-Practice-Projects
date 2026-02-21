from pydantic import BaseModel, Field, field_validator
from typing import Optional

class User(BaseModel):
    name: str = Field(...) # ... in Field meaning Optional
    age: int = Field(..., ge= 18, le= 100) # Greater equal or lessthan equal
    team: Optional[str] = 'Tech'

class Company(BaseModel):
    department: str = Field(...) 
    employees: int
    revenue: float = Field(
        ...,
        ge=100000
    )

    @field_validator('employees') # Decorators
    def ValidateEmployee(cls, v):
        if v < 10:
            raise ValueError('Minimum 10 employees needed for a company')
        return v

data = {
    'department': 'Technical',
    "employees": 20,
    "revenue": 2000000
}
# cmp = Company(data)# Error: BaseModel.__init__() takes 1 positional argument but 2 were given
# print(cmp) 
cmp = Company(**data)
print(cmp)
