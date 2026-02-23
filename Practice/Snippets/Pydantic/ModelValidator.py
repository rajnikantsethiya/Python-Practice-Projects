from pydantic import BaseModel, field_validator, model_validator

class Signup(BaseModel):
    password: str
    confirmPassword: str # LEVEL 1 Check 

    @field_validator('password', 'confirmPassword') # Level 2 Check 
    def minimumLen(cls, values):
        if len(values) < 8:
            raise ValueError("Password must be minimum of 8 characters")
        return values
    
    @model_validator(mode='after') # Level 3 check 
    def MatchPass(cls, values):
        if (values.password != values.confirmPassword):
            raise ValueError("Passwords doesnt match")
        return values
    
sign = Signup(password='12345678', confirmPassword='12345678')
print(sign)
    
