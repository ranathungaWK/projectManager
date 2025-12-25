from pydantic import BaseModel
from datetime import datetime
from enum import Enum 


class ProjectCreate(BaseModel):
    name: str 
    description : str

class Project(BaseModel):
    id : int
    name: str 
    description : str
    status : str
    create_at : datetime

    class Config:
        from_attributes = True

class ProjectStatus(str , Enum):
    ongoing = "ongoing"
    paused = "paused"
    ended = "ended"

class ProjectStatusUpdate(BaseModel):
    status: ProjectStatus
