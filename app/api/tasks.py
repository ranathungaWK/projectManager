from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.auth import router
from app.db.session import get_db
from app.models import project
from app.models.task import Task
from app.models.project import Project
from app.schemas.task import TaskCreate, Task as TaskModel, TaskStatusUpdate
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/tasks" , tags=["Tasks"])

@router.post("/create" , response_model=TaskModel , status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate , db : Session = Depends(get_db) , current_user:User = Depends(get_current_user)) -> TaskModel:
    """create a new task"""

    project = db.query(Project).filter(Project.id == task.project_id , Project.owner_id == current_user.id).first()

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Project not found")
    
    new_task = Task( 
        title = task.title,
        description = task.description ,
        project_id = task.project_id,
        owner_id = current_user.id   
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/list/{project_id}", response_model=list[TaskModel])
def list_tasks(project_id: int , db:Session = Depends(get_db) , current_user:User = Depends(get_current_user)) -> list:
    """list all tasks"""
    return db.query(Task).filter(Task.project_id == project_id , Task.owner_id == current_user.id).all()


@router.patch("/status/{task_id}" , response_model=TaskModel)
def update_task_status(task_id:int , payload:TaskStatusUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> TaskModel:
    """Update the status of a task."""
    task = db.query(Task).filter(Task.id == task_id , Task.owner_id == current_user.id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.status = payload.status
    db.commit()
    db.refresh(task)

    return task 