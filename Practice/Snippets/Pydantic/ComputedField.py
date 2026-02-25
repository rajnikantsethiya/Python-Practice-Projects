from pydantic import BaseModel, computed_field

class Company(BaseModel):
    clients: int
    costToClient: float

    @computed_field
    @property
    def calcRevenue(self) -> float:
        return self.clients * self.costToClient
    
cmp = Company(clients=10, costToClient=1000)
print(cmp.calcRevenue)
print(cmp.model_dump())
