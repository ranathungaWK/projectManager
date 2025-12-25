from pydantic import BaseModel , EmailStr


#schema for signup(creating user account)
class UserCreate(BaseModel):
    username : str
    email : EmailStr 
    password : str 

#schema for login
class UserLogin(BaseModel):
    username : str 
    password : str 

#schema for response model 
class User(BaseModel):
    id : int 
    username : str 
    email : EmailStr