from sqlite3 import complete_statement
from pydantic import BaseModel

class ProjectProgressReport(BaseModel):
    project_id: int
    project_name: str
    total_tasks: int
    completed_tasks: int 
    pending_tasks: int 
    progress_percent : float

class TaskStatusSummary(BaseModel):
    todo:int
    in_progress:int
    done:int

class userOverviewReport(BaseModel):
    total_projects:int
    total_tasks:int
    completed_tasks:int