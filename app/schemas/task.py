from asyncio import Task
from turtle import title
from pydantic import BaseModel
from datetime import datetime 
from enum import Enum

from app.models import project 

class TaskStatus(str , Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class TaskCreate(BaseModel):
    title : str
    description : str | None = None
    project_id : int 

class TaskStatusUpdate(BaseModel):
    status : TaskStatus

class Task(BaseModel):
    id : int 
    title : str
    description : str | None = None  
    status : TaskStatus
    project_id : int 
    owner_id : int 
    create_at : datetime 

    class Config:
        from_attributes = True